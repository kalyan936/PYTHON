from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.app import App
import sys
import io
import traceback


def _rounded_bg(widget, r, g, b, a=1, radius=8):
    """Attach a rounded-rectangle background canvas instruction to widget."""
    with widget.canvas.before:
        Color(r, g, b, a)
        rect = RoundedRectangle(pos=widget.pos, size=widget.size, radius=[dp(radius)])
    widget.bind(
        pos=lambda *_: setattr(rect, "pos", widget.pos),
        size=lambda *_: setattr(rect, "size", widget.size),
    )
    return rect


def safe_exec(code):
    """Execute code safely and capture output."""
    output_buf = io.StringIO()
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = output_buf
    sys.stderr = output_buf

    # Restrict dangerous builtins
    safe_globals = {
        "__builtins__": {
            "print": print,
            "range": range,
            "len": len,
            "int": int,
            "float": float,
            "str": str,
            "bool": bool,
            "list": list,
            "dict": dict,
            "tuple": tuple,
            "set": set,
            "enumerate": enumerate,
            "zip": zip,
            "map": map,
            "filter": filter,
            "sorted": sorted,
            "reversed": reversed,
            "sum": sum,
            "min": min,
            "max": max,
            "abs": abs,
            "round": round,
            "type": type,
            "isinstance": isinstance,
            "input": lambda _="": "",
        }
    }

    try:
        exec(compile(code, "<editor>", "exec"), safe_globals)
    except Exception:
        traceback.print_exc()
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr

    return output_buf.getvalue()


class CodeLabel(Label):
    """A label tuned for code-like monospace content that wraps correctly."""
    def __init__(self, **kwargs):
        kwargs.setdefault("font_size", dp(12))
        kwargs.setdefault("color", (0.85, 0.92, 1, 1))
        kwargs.setdefault("halign", "left")
        kwargs.setdefault("valign", "top")
        kwargs.setdefault("markup", False)
        super().__init__(**kwargs)
        self.bind(width=self._update_text_size, texture_size=self._update_height)

    def _update_text_size(self, *_):
        self.text_size = (self.width, None)

    def _update_height(self, *_):
        self.height = self.texture_size[1]


class PracticeScreen(Screen):
    """Full-screen view for lesson practice (code editor)."""

    def __init__(self, lesson, lesson_index, **kwargs):
        super().__init__(**kwargs)
        self.lesson = lesson
        self.lesson_index = lesson_index
        self._build()

    def _build(self):
        self.clear_widgets()
        root = BoxLayout(orientation="vertical", padding=dp(12), spacing=dp(8))

        # ── top bar with navigation buttons ────────────
        top = BoxLayout(size_hint_y=None, height=dp(50), spacing=dp(8))
        
        back_btn = Button(
            text="← Back to Lessons",
            size_hint=(None, 1),
            width=dp(130),
            background_color=(0.18, 0.20, 0.30, 1),
            background_normal="",
            font_size=dp(11),
        )
        back_btn.bind(on_press=self._go_back)
        top.add_widget(back_btn)

        theory_btn = Button(
            text="← Theory",
            size_hint=(None, 1),
            width=dp(90),
            background_color=(0.25, 0.35, 0.65, 1),
            background_normal="",
            font_size=dp(11),
            bold=True,
        )
        theory_btn.bind(on_press=self._go_theory)
        top.add_widget(theory_btn)

        title_lbl = Label(
            text=f"⌨️ {self.lesson['title']} - Practice",
            font_size=dp(14),
            bold=True,
            color=(0.7, 0.85, 1, 1),
            halign="left",
            valign="middle",
        )
        title_lbl.bind(size=lambda w, _: setattr(w, "text_size", (w.width, None)))
        top.add_widget(title_lbl)

        run_btn = Button(
            text="▶ Run",
            size_hint=(None, 1),
            width=dp(80),
            background_color=(0.15, 0.65, 0.35, 1),
            background_normal="",
            font_size=dp(12),
            bold=True,
        )
        run_btn.bind(on_press=self._run_code)
        top.add_widget(run_btn)
        
        root.add_widget(top)

        # ── code editor ────────────────────────────────
        self.code_input = TextInput(
            text=self.lesson["practice"],
            font_name="RobotoMono-Regular",
            font_size=dp(12),
            background_color=(0.1, 0.12, 0.18, 1),
            foreground_color=(0.85, 0.95, 1, 1),
            cursor_color=(0.4, 0.8, 1, 1),
            multiline=True,
            size_hint_y=0.55,
            padding=[dp(10), dp(10)],
        )
        root.add_widget(self.code_input)

        # ── output section ─────────────────────────────
        output_label = Label(
            text="Output:",
            font_size=dp(12),
            color=(0.5, 0.5, 0.7, 1),
            size_hint_y=None,
            height=dp(22),
            halign="left",
        )
        root.add_widget(output_label)

        self.output_box = TextInput(
            text="(Click 'Run' to execute code)",
            font_name="RobotoMono-Regular",
            font_size=dp(12),
            background_color=(0.06, 0.08, 0.12, 1),
            foreground_color=(0.5, 1, 0.6, 1),
            readonly=True,
            multiline=True,
            size_hint_y=0.35,
            padding=[dp(10), dp(10)],
        )
        root.add_widget(self.output_box)

        # ── clear button ───────────────────────────────
        clear_btn = Button(
            text="Clear Output",
            size_hint_y=None,
            height=dp(38),
            background_color=(0.25, 0.15, 0.15, 1),
            background_normal="",
            font_size=dp(12),
        )
        clear_btn.bind(on_press=lambda _: setattr(self.output_box, "text", ""))
        root.add_widget(clear_btn)

        self.add_widget(root)

    def _run_code(self, *args):
        """Execute the code and show output."""
        code = self.code_input.text
        result = safe_exec(code)
        self.output_box.text = result if result else "(no output)"
        self.output_box.foreground_color = (
            (1, 0.45, 0.45, 1) if "Error" in result or "Traceback" in result
            else (0.5, 1, 0.6, 1)
        )

    def _go_back(self, *_):
        """Go back to lessons list."""
        App.get_running_app().root.current = "lesson"

    def _go_theory(self, *_):
        """Go back to theory screen."""
        sm = App.get_running_app().root
        screen_name = f"theory_{self.lesson_index}"
        sm.current = screen_name
