# PyLearn — Python Learning Application

A Kivy-based interactive Python course with lessons, theory, practice, quizzes, and progress tracking.

## How to Run

### 1. Install dependencies

```bash
pip install kivy==2.3.0 kivymd==1.2.0
```

> **Note:** On some systems you may also need:
> ```bash
> pip install kivy[base] kivy[full]
> ```

### 2. Run the app

```bash
cd python-learning-app
python main.py
```

The app opens in a 540×960 window (mobile-like). Resize freely.

## Project Structure

```
python-learning-app/
├── main.py                  # App entry point
├── requirements.txt
├── buildozer.spec           # Android build config (optional, for mobile packaging)
├── screens/
│   ├── home_screen.py       # Home / menu screen
│   ├── lesson_screen.py     # Lesson list screen
│   ├── theory_screen.py     # Per-lesson theory view
│   ├── practice_screen.py   # Per-lesson code editor / practice
│   ├── editor_screen.py     # Free-form code editor
│   ├── quiz_screen.py       # Quiz screen
│   ├── progress_screen.py   # Progress tracker
│   ├── Advance feature.py   # (Extra) Syntax highlight & matplotlib extras
│   ├── Challenges.py        # (Extra) Challenge/exercise system
│   └── __init__.py
└── utils/
    ├── storage.py           # JSON-backed key-value store helper
    └── __init__.py
```

## Bugs Fixed

| File | Issue | Fix |
|------|-------|-----|
| `main.py` | Imported `lessons_manager` (didn't exist) | Changed to `lesson_screen` |
| `main.py` | Imported `theory_screen` (didn't exist) | Removed — loaded dynamically |
| `main.py` | Imported `practice_screen` (didn't exist) | Removed — loaded dynamically |
| `main.py` | Added `TheoryScreen`/`PracticeScreen` to ScreenManager at startup | Removed — they're created on-demand per lesson |
| `main.py` | No `sys.path` setup so screen modules couldn't be found | Added `screens/` dir to `sys.path` |
| `screens/` | `theory_screen.py` was completely missing | Created new `theory_screen.py` with `TheoryScreen` class |
| `screens/` | `practice_screen.py` was missing (content existed in `Theorey screen.py`) | Copied to correct filename |
| `requirements.txt` | Included `buildozer` (Android packager, breaks desktop installs) and `cython` (not needed to run) | Removed both |
