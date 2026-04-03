from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.app import App


def _rounded_bg(widget, r, g, b, a=1, radius=8):
    with widget.canvas.before:
        Color(r, g, b, a)
        rect = RoundedRectangle(pos=widget.pos, size=widget.size, radius=[dp(radius)])
    widget.bind(
        pos=lambda *_: setattr(rect, "pos", widget.pos),
        size=lambda *_: setattr(rect, "size", widget.size),
    )
    return rect


class TheoryLabel(Label):
    """A label tuned for theory text that wraps and sizes correctly."""
    def __init__(self, **kwargs):
        kwargs.setdefault("font_size", dp(13))
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


class TheoryScreen(Screen):
    """Full-screen view for lesson theory content."""

    def __init__(self, lesson, lesson_index, **kwargs):
        super().__init__(**kwargs)
        self.lesson = lesson
        self.lesson_index = lesson_index
        self._build()

    def _build(self):
        self.clear_widgets()
        root = BoxLayout(orientation="vertical", padding=dp(12), spacing=dp(8))

        # ── top bar ─────────────────────────────────
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

        practice_btn = Button(
            text="Practice →",
            size_hint=(None, 1),
            width=dp(90),
            background_color=(0.15, 0.55, 0.35, 1),
            background_normal="",
            font_size=dp(11),
            bold=True,
        )
        practice_btn.bind(on_press=self._go_practice)
        top.add_widget(practice_btn)

        title_lbl = Label(
            text=f"📖 {self.lesson['title']}",
            font_size=dp(14),
            bold=True,
            color=(0.7, 0.85, 1, 1),
            halign="left",
            valign="middle",
        )
        title_lbl.bind(size=lambda w, _: setattr(w, "text_size", (w.width, None)))
        top.add_widget(title_lbl)

        root.add_widget(top)

        # ── scrollable theory content ────────────────
        scroll = ScrollView(do_scroll_x=False, bar_width=dp(4))

        content_box = BoxLayout(
            orientation="vertical",
            padding=[dp(14), dp(10)],
            size_hint_y=None,
        )
        content_box.bind(minimum_height=content_box.setter("height"))

        _rounded_bg(content_box, 0.10, 0.12, 0.20, radius=10)

        theory_lbl = TheoryLabel(
            text=self.lesson["theory"],
            size_hint_y=None,
        )
        content_box.add_widget(theory_lbl)

        scroll.add_widget(content_box)
        root.add_widget(scroll)

        self.add_widget(root)

    def _go_back(self, *_):
        App.get_running_app().root.current = "lesson"

    def _go_practice(self, *_):
        sm = App.get_running_app().root
        screen_name = f"practice_{self.lesson_index}"
        if not sm.has_screen(screen_name):
            from practice_screen import PracticeScreen
            detail = PracticeScreen(self.lesson, self.lesson_index, name=screen_name)
            sm.add_widget(detail)
        sm.current = screen_name
