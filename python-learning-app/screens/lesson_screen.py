from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.app import App

# ─────────────────────────────────────────────
#  FULL PYTHON COURSE  (theory + practice pairs)
# ─────────────────────────────────────────────
LESSONS = [
    # ── 1 ──────────────────────────────────────
    {
        "title": "1. Variables & Data Types",
        "theory": """\
WHAT IS A VARIABLE?
━━━━━━━━━━━━━━━━━━
A variable is a named container that holds a value in memory.
Python is dynamically typed — you never need to declare a type.

BUILT-IN TYPES
━━━━━━━━━━━━━━
  int    – whole numbers         x = 10
  float  – decimal numbers       pi = 3.14159
  str    – text (use '' or "")   name = "Alice"
  bool   – True or False         flag = True
  None   – absence of value      result = None

TYPE CHECKING
━━━━━━━━━━━━
Use type() to inspect a variable:
  type(42)      → <class 'int'>
  type(3.14)    → <class 'float'>
  type("hi")    → <class 'str'>

TYPE CONVERSION
━━━━━━━━━━━━━━
  int("5")    → 5
  float(3)    → 3.0
  str(100)    → "100"
  bool(0)     → False   (0, "", [], None are falsy)

NAMING RULES
━━━━━━━━━━━━
• Use snake_case: my_variable ✓
• Must start with a letter or _
• Cannot use keywords (if, for, while …)
• Case-sensitive: Name ≠ name
""",
        "practice": """\
# ── Variables & Data Types ──────────────────

# Assigning different types
age = 25
height = 5.9
name = "Bob"
is_student = True
nothing = None

print(age, type(age))
print(height, type(height))
print(name, type(name))
print(is_student, type(is_student))
print(nothing, type(nothing))

# ── Type Conversion ──────────────────────────
text_number = "42"
converted = int(text_number)
print(converted + 8)        # 50

print(float("3.14"))        # 3.14
print(str(100) + " items")  # 100 items

# ── Falsy values ─────────────────────────────
for val in [0, "", [], None, False, 0.0]:
    print(f"bool({val!r}) = {bool(val)}")

# ── Multiple assignment ───────────────────────
a, b, c = 1, 2, 3
print(a, b, c)

x = y = z = 0
print(x, y, z)
""",
    },
    # ── 2 ──────────────────────────────────────
    {
        "title": "2. Strings",
        "theory": """\
STRINGS IN PYTHON
━━━━━━━━━━━━━━━━━
Strings are immutable sequences of characters.
Use single quotes ' or double quotes " — both work.
For multi-line text use triple quotes \"\"\"...\"\"\".

COMMON OPERATIONS
━━━━━━━━━━━━━━━━━
  s = "Hello, World!"
  len(s)          → 13         (length)
  s.upper()       → "HELLO, WORLD!"
  s.lower()       → "hello, world!"
  s.strip()                    (remove leading/trailing spaces)
  s.replace("World","Python")  → "Hello, Python!"
  s.split(", ")   → ["Hello", "World!"]
  ", ".join(["a","b","c"])  → "a, b, c"

INDEXING & SLICING
━━━━━━━━━━━━━━━━━━
  s[0]     → 'H'          (first character)
  s[-1]    → '!'          (last character)
  s[0:5]   → 'Hello'      (slice: start inclusive, end exclusive)
  s[::2]   → every 2nd character
  s[::-1]  → reversed string

F-STRINGS  (Python 3.6+, preferred)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  name = "Alice"
  age  = 30
  f"My name is {name} and I am {age} years old."
  f"2 + 2 = {2 + 2}"          # expressions work too
  f"Pi ≈ {3.14159:.2f}"       # format specifiers

ESCAPE SEQUENCES
━━━━━━━━━━━━━━━━
  \\n   newline       \\t   tab
  \\'   single quote  \\\\ backslash
""",
        "practice": """\
# ── String Operations ───────────────────────

s = "  Hello, Python!  "
print(s.strip())               # Hello, Python!
print(s.strip().upper())       # HELLO, PYTHON!
print(s.strip().replace("Python", "World"))

# ── Slicing ──────────────────────────────────
text = "abcdefgh"
print(text[2:5])     # cde
print(text[::-1])    # hgfedcba  (reversed)
print(text[::2])     # aceg

# ── Splitting & joining ───────────────────────
csv = "Alice,Bob,Charlie,Diana"
names = csv.split(",")
print(names)
print(" | ".join(names))

# ── F-strings ────────────────────────────────
name  = "Aditya"
score = 87.5
print(f"Student: {name}")
print(f"Score:   {score:.1f}%")
print(f"Grade:   {'A' if score >= 90 else 'B' if score >= 75 else 'C'}")

# ── Useful checks ────────────────────────────
email = "user@example.com"
print(email.startswith("user"))   # True
print(email.endswith(".com"))     # True
print("@" in email)               # True
print(email.count("."))           # 1
""",
    },
    # ── 3 ──────────────────────────────────────
    {
        "title": "3. Control Flow (if/elif/else)",
        "theory": """\
MAKING DECISIONS
━━━━━━━━━━━━━━━━
Python uses if / elif / else to branch logic.
Indentation (4 spaces) defines the block — no braces needed.

SYNTAX
━━━━━━
  if condition:
      # block runs when condition is True
  elif another_condition:
      # checked only if first was False
  else:
      # runs when none of the above matched

COMPARISON OPERATORS
━━━━━━━━━━━━━━━━━━━━
  ==   equal to           !=   not equal
  <    less than          >    greater than
  <=   less or equal      >=   greater or equal

LOGICAL OPERATORS
━━━━━━━━━━━━━━━━━
  and   both must be True
  or    at least one must be True
  not   inverts the boolean

TRUTHINESS
━━━━━━━━━━
Falsy: 0, 0.0, "", [], {}, None, False
Everything else is truthy.

TERNARY (one-liner)
━━━━━━━━━━━━━━━━━━━
  label = "even" if n % 2 == 0 else "odd"
""",
        "practice": """\
# ── if / elif / else ─────────────────────────

score = 73

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score} → Grade {grade}")

# ── Logical operators ─────────────────────────
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

# ── Ternary expression ────────────────────────
n = 7
parity = "even" if n % 2 == 0 else "odd"
print(f"{n} is {parity}")

# ── Nested conditions ─────────────────────────
temp = 28
humid = 80

if temp > 35:
    print("Very hot")
elif temp > 25:
    if humid > 75:
        print("Hot and humid")
    else:
        print("Warm")
else:
    print("Pleasant")

# ── FizzBuzz (classic) ────────────────────────
for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
""",
    },
    # ── 4 ──────────────────────────────────────
    {
        "title": "4. Loops (for & while)",
        "theory": """\
FOR LOOPS
━━━━━━━━━
Iterate over any iterable (list, string, range, dict…):

  for item in collection:
      # do something with item

  range(stop)           → 0, 1, …, stop-1
  range(start, stop)    → start, start+1, …, stop-1
  range(start, stop, step)  → with custom step

WHILE LOOPS
━━━━━━━━━━━
Repeat as long as condition is True:

  while condition:
      # do something
      if exit_condition:
          break

LOOP CONTROL
━━━━━━━━━━━━
  break      – exit the loop entirely
  continue   – skip to next iteration
  else       – runs after normal completion (not break)

NESTED LOOPS
━━━━━━━━━━━━━
  for i in range(3):
      for j in range(3):
          print(f"({i}, {j})")
""",
        "practice": """\
# ── Simple for loop ──────────────────────────
for i in range(5):
    print(f"Iteration {i}")

# ── Loop over strings ────────────────────────
for letter in "Python":
    print(letter)

# ── range() with start, stop, step ──────────
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# ── while loop ───────────────────────────────
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# ── break and continue ───────────────────────
for i in range(10):
    if i == 3:
        continue  # skip 3
    if i == 7:
        break     # stop at 7
    print(i)

# ── for-else (runs if no break) ──────────────
for i in range(5):
    print(i)
else:
    print("Loop completed normally")

# ── Nested loops ─────────────────────────────
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j}", end="  ")
    print()  # newline
""",
    },
    # ── 5 ──────────────────────────────────────
    {
        "title": "5. Functions",
        "theory": """\
DEFINING FUNCTIONS
━━━━━━━━━━━━━━━━━━
Functions let you reuse code and organize logic.

  def function_name(param1, param2):
      \"\"\"Docstring: brief description.\"\"\"
      # function body
      return result

RETURN VALUES
━━━━━━━━━━━━━━
  return    – exits function, returns value
  return    – (no value) returns None

PARAMETERS & ARGUMENTS
━━━━━━━━━━━━━━━━━━━━━━
  def greet(name):       # name is a parameter
      print(f"Hi {name}")

  greet("Alice")         # "Alice" is an argument

DEFAULT PARAMETERS
━━━━━━━━━━━━━━━━━━
  def power(x, n=2):
      return x ** n

  power(3)     → 9    (uses default n=2)
  power(3, 3)  → 27   (overrides default)

KEYWORD ARGUMENTS
━━━━━━━━━━━━━━━━━
  def info(name, age):
      print(f"{name} is {age}")

  info(name="Bob", age=30)
  info(age=30, name="Bob")  # order doesn't matter

*ARGS & **KWARGS
━━━━━━━━━━━━━━━━
  def sum_all(*args):        # accepts any number
      return sum(args)
  sum_all(1, 2, 3)  → 6

  def info(**kwargs):        # accepts key=value pairs
      for k, v in kwargs.items():
          print(f"{k}: {v}")
""",
        "practice": """\
# ── Simple function ──────────────────────────
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))

# ── Function with default parameter ────────
def power(x, n=2):
    return x ** n

print(power(3))      # 9
print(power(3, 3))   # 27

# ── Multiple return values ───────────────────
def divmod_custom(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divmod_custom(17, 5)
print(f"{q} remainder {r}")

# ── Function using *args ────────────────────
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))
print(sum_all(10, 20, 30, 40))

# ── Function using **kwargs ─────────────────
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")

# ── Nested functions ──────────────────────
def outer(x):
    def inner(y):
        return x + y
    return inner

add_5 = outer(5)
print(add_5(10))  # 15
""",
    },
    # ── 6 ──────────────────────────────────────
    {
        "title": "6. Lists & Tuples",
        "theory": """\
LISTS  (mutable)
━━━━━━━━━━━━━━━
Ordered, changeable collection of items.

  lst = [1, 2, 3, "text", True]
  lst[0]         → 1
  lst[-1]        → True
  lst[1:3]       → [2, 3]  (slice)

COMMON LIST METHODS
━━━━━━━━━━━━━━━━━━━
  lst.append(4)        → [1, 2, 3, "text", True, 4]
  lst.insert(0, 99)    → insert at index
  lst.remove(2)        → remove first occurrence
  lst.pop()            → remove & return last item
  lst.pop(0)           → remove & return at index
  lst.sort()           → sort in place
  lst.reverse()        → reverse in place
  lst.clear()          → remove all items

TUPLES  (immutable)
━━━━━━━━━━━━━━━━━━
Ordered, unchangeable collection.

  tup = (1, 2, 3, "text")
  tup[0]       → 1
  tup[1:3]     → (2, 3)
  len(tup)     → 4

  # Cannot modify:
  tup[0] = 99  → ERROR

UNPACKING
━━━━━━━━━━
  a, b, c = [1, 2, 3]
  x, *rest, z = [1, 2, 3, 4, 5]  → x=1, rest=[2,3,4], z=5
""",
        "practice": """\
# ── Creating and accessing lists ────────────
fruits = ["apple", "banana", "cherry"]
print(fruits[0])     # apple
print(fruits[-1])    # cherry
print(fruits[1:3])   # ['banana', 'cherry']

# ── List methods ────────────────────────────
fruits.append("date")
print(fruits)  # ['apple', 'banana', 'cherry', 'date']

fruits.insert(1, "blueberry")
print(fruits)  # apple, blueberry, banana, cherry, date

fruits.remove("cherry")
print(fruits)

# ── Looping over lists ───────────────────────
numbers = [10, 20, 30, 40]
for num in numbers:
    print(num)

# ── List comprehension ───────────────────────
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# ── Tuples ──────────────────────────────────
coords = (10, 20)
print(coords[0])   # 10

# Cannot modify tuples
# coords[0] = 15   # ERROR

# ── Tuple unpacking ─────────────────────────
x, y = (5, 10)
print(f"x={x}, y={y}")

a, *rest, z = [1, 2, 3, 4, 5]
print(f"a={a}, rest={rest}, z={z}")
""",
    },
    # ── 7 ──────────────────────────────────────
    {
        "title": "7. Dictionaries & Sets",
        "theory": """\
DICTIONARIES  (key-value pairs, mutable)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  d = {"name": "Alice", "age": 30, "city": "NYC"}
  d["name"]      → "Alice"
  d.get("age")   → 30
  d.get("job", "unknown")  → "unknown"  (with default)

DICT METHODS
━━━━━━━━━━━━
  d["job"] = "Engineer"    → add/update
  d.pop("city")            → remove & return value
  d.keys()                 → dict_keys(['name', 'age', ...])
  d.values()               → dict_values(['Alice', 30, ...])
  d.items()                → [('name', 'Alice'), ('age', 30), ...]

SETS  (unordered, unique items, mutable)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  s = {1, 2, 3, 2, 1}   → {1, 2, 3}  (duplicates removed)
  s = set()             → empty set (not {})
  1 in s                → membership test

SET OPERATIONS
━━━━━━━━━━━━━━
  s.add(4)             → add element
  s.remove(2)          → remove element
  s1 | s2              → union
  s1 & s2              → intersection
  s1 - s2              → difference
""",
        "practice": """\
# ── Creating dictionaries ───────────────────
person = {"name": "Alice", "age": 30, "city": "NYC"}
print(person["name"])    # Alice
print(person.get("age")) # 30

# ── Updating dictionaries ───────────────────
person["job"] = "Engineer"
person["age"] = 31
print(person)

# ── Looping over dictionaries ───────────────
for key, value in person.items():
    print(f"{key}: {value}")

# ── Checking keys ────────────────────────────
if "name" in person:
    print("Name field exists")

# ── Sets ──────────────────────────────────────
unique_colors = {"red", "green", "blue", "red"}
print(unique_colors)  # {'red', 'green', 'blue'}

# ── Set operations ───────────────────────────
s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1 | s2)  # union: {1, 2, 3, 4, 5}
print(s1 & s2)  # intersection: {3}
print(s1 - s2)  # difference: {1, 2}

# ── Set methods ──────────────────────────────
s1.add(4)
print(s1)
s1.remove(2)
print(s1)
""",
    },
]


def _rounded_bg(widget, r, g, b, a=1, radius=10):
    """Attach a rounded-rectangle background canvas instruction to widget."""
    with widget.canvas.before:
        Color(r, g, b, a)
        rect = RoundedRectangle(pos=widget.pos, size=widget.size, radius=[dp(radius)])
    widget.bind(
        pos=lambda *_: setattr(rect, "pos", widget.pos),
        size=lambda *_: setattr(rect, "size", widget.size),
    )
    return rect


class LessonCard(BoxLayout):
    """Card for each lesson in the lesson list."""

    def __init__(self, lesson, index, on_open, **kwargs):
        super().__init__(orientation="vertical", padding=dp(12), spacing=dp(4), **kwargs)
        self.size_hint_y = None
        self.height = dp(80)
        _rounded_bg(self, 0.13, 0.15, 0.24, radius=10)

        row = BoxLayout(spacing=dp(10))

        # index badge
        badge = Label(
            text=str(index + 1),
            font_size=dp(15),
            bold=True,
            color=(0.4, 0.8, 1, 1),
            size_hint=(None, 1),
            width=dp(32),
        )
        row.add_widget(badge)

        title_lbl = Label(
            text=lesson["title"],
            font_size=dp(14),
            bold=True,
            color=(0.9, 0.95, 1, 1),
            halign="left",
            valign="middle",
        )
        title_lbl.bind(size=lambda w, _: setattr(w, "text_size", (w.width, None)))
        row.add_widget(title_lbl)

        # Theory button
        theory_btn = Button(
            text="📖",
            size_hint=(None, None),
            size=(dp(45), dp(35)),
            background_color=(0.22, 0.35, 0.75, 1),
            background_normal="",
            font_size=dp(18),
        )
        theory_btn.bind(on_press=lambda _: on_open(lesson, index, "theory"))
        row.add_widget(theory_btn)

        # Practice button
        practice_btn = Button(
            text="⌨️",
            size_hint=(None, None),
            size=(dp(45), dp(35)),
            background_color=(0.15, 0.55, 0.35, 1),
            background_normal="",
            font_size=dp(18),
        )
        practice_btn.bind(on_press=lambda _: on_open(lesson, index, "practice"))
        row.add_widget(practice_btn)

        self.add_widget(row)


class LessonScreen(Screen):
    """Main lesson list screen."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._build_ui()

    def _build_ui(self):
        self.clear_widgets()
        root = BoxLayout(orientation="vertical", padding=dp(14), spacing=dp(10))

        # ── top bar ──────────────────────────────
        top = BoxLayout(size_hint_y=None, height=dp(48), spacing=dp(8))
        back_btn = Button(
            text="← Home",
            size_hint=(None, 1),
            width=dp(90),
            background_color=(0.18, 0.20, 0.30, 1),
            background_normal="",
            font_size=dp(13),
        )
        back_btn.bind(on_press=lambda _: setattr(App.get_running_app().root, "current", "home"))
        top.add_widget(back_btn)

        top.add_widget(Label(
            text="📚  Python Course",
            font_size=dp(20),
            bold=True,
            color=(1, 1, 1, 1),
            halign="left",
        ))
        root.add_widget(top)

        # sub-header
        root.add_widget(Label(
            text=f"{len(LESSONS)} lessons  •  📖 for theory, ⌨️ for practice",
            font_size=dp(12),
            color=(0.55, 0.60, 0.80, 1),
            halign="left",
            size_hint_y=None,
            height=dp(20),
        ))

        # ── lesson list ──────────────────────────
        scroll = ScrollView(do_scroll_x=False, bar_width=dp(4))
        grid = BoxLayout(
            orientation="vertical",
            spacing=dp(8),
            size_hint_y=None,
            padding=[0, 0, 0, dp(20)],
        )
        grid.bind(minimum_height=grid.setter("height"))

        for i, lesson in enumerate(LESSONS):
            card = LessonCard(lesson, i, on_open=self._open_lesson)
            grid.add_widget(card)

        scroll.add_widget(grid)
        root.add_widget(scroll)
        self.add_widget(root)

    def _open_lesson(self, lesson, index, lesson_type):
        """Open either theory or practice screen."""
        sm = App.get_running_app().root

        if lesson_type == "theory":
            screen_name = f"theory_{index}"
            if not sm.has_screen(screen_name):
                from theory_screen import TheoryScreen
                detail = TheoryScreen(lesson, index, name=screen_name)
                sm.add_widget(detail)
        else:  # practice
            screen_name = f"practice_{index}"
            if not sm.has_screen(screen_name):
                from practice_screen import PracticeScreen
                detail = PracticeScreen(lesson, index, name=screen_name)
                sm.add_widget(detail)

        sm.current = screen_name
