"""
PyLearn - Python Learning Application
A Kivy-based interactive Python course with lessons, practice, quizzes, and progress tracking.
"""

import os
import sys

# Ensure the screens folder is on the path so all screen modules can be found
SCREENS_DIR = os.path.join(os.path.dirname(__file__), "screens")
if SCREENS_DIR not in sys.path:
    sys.path.insert(0, SCREENS_DIR)

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore

# Import all top-level screens
from home_screen import HomeScreen
from lesson_screen import LessonScreen
from editor_screen import EditorScreen
from quiz_screen import QuizScreen
from progress_screen import ProgressScreen
# theory_screen and practice_screen are loaded dynamically by lesson_screen.py
# as the user opens individual lessons -- no need to import them here.

# Set window properties
Window.size = (540, 960)  # Mobile-like dimensions
Window.clearcolor = (0.08, 0.09, 0.15, 1)  # Dark blue background


class PyLearnApp(App):
    """Main PyLearn Application."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "PyLearn - Learn Python"

        # Initialize storage for tracking progress
        self.storage = JsonStore("pylearn_data.json")

    def build(self):
        """Build and configure the app."""
        sm = ScreenManager()

        # Add all top-level screens to the screen manager
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LessonScreen(name="lesson"))
        sm.add_widget(EditorScreen(name="editor"))
        sm.add_widget(QuizScreen(name="quiz"))
        sm.add_widget(ProgressScreen(name="progress"))
        # Theory and Practice screens are added dynamically in lesson_screen.py

        # Set home as the default screen
        sm.current = "home"

        return sm


if __name__ == "__main__":
    app = PyLearnApp()
    app.run()
