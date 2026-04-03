"""
Advanced Features Module for PyLearn
Includes syntax highlighting, themes, and enhanced code editor features.
"""

from kivy.uix.textinput import TextInput
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivy.metrics import dp


class SyntaxHighlightedEditor(TextInput):
    """Enhanced text input with syntax highlighting for Python code."""
    
    # Python keywords
    KEYWORDS = {
        'if', 'else', 'elif', 'while', 'for', 'def', 'class', 'return',
        'import', 'from', 'as', 'try', 'except', 'finally', 'with', 'lambda',
        'yield', 'pass', 'break', 'continue', 'True', 'False', 'None', 'and',
        'or', 'not', 'in', 'is', 'assert', 'del', 'global', 'nonlocal', 'raise'
    }
    
    # Built-in functions
    BUILTINS = {
        'print', 'len', 'range', 'list', 'dict', 'tuple', 'set', 'str', 'int',
        'float', 'bool', 'type', 'isinstance', 'sum', 'min', 'max', 'sorted',
        'enumerate', 'zip', 'map', 'filter', 'input', 'open', 'file', 'super',
        'property', 'staticmethod', 'classmethod', 'all', 'any', 'abs', 'round'
    }
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = "RobotoMono-Regular"
        self.font_size = dp(12)
        self.multiline = True


class ThemeManager:
    """Manage application themes (Dark, Light, High Contrast)."""
    
    THEMES = {
        'dark': {
            'bg': (0.08, 0.09, 0.15, 1),
            'text': (0.85, 0.92, 1, 1),
            'button_primary': (0.22, 0.35, 0.75, 1),
            'button_success': (0.15, 0.55, 0.35, 1),
            'button_danger': (0.75, 0.15, 0.15, 1),
            'accent': (0.4, 0.8, 1, 1),
            'success': (0.5, 1, 0.6, 1),
            'error': (1, 0.45, 0.45, 1),
        },
        'light': {
            'bg': (0.95, 0.95, 0.97, 1),
            'text': (0.1, 0.1, 0.1, 1),
            'button_primary': (0.2, 0.4, 0.8, 1),
            'button_success': (0.1, 0.6, 0.3, 1),
            'button_danger': (0.8, 0.1, 0.1, 1),
            'accent': (0.2, 0.5, 0.9, 1),
            'success': (0.1, 0.7, 0.2, 1),
            'error': (0.9, 0.2, 0.2, 1),
        },
        'high_contrast': {
            'bg': (0.0, 0.0, 0.0, 1),
            'text': (1.0, 1.0, 1.0, 1),
            'button_primary': (0.0, 0.2, 1.0, 1),
            'button_success': (0.0, 1.0, 0.0, 1),
            'button_danger': (1.0, 0.0, 0.0, 1),
            'accent': (1.0, 1.0, 0.0, 1),
            'success': (0.0, 1.0, 0.0, 1),
            'error': (1.0, 0.0, 0.0, 1),
        }
    }
    
    def __init__(self, theme_name='dark'):
        self.current_theme = theme_name
        self.theme_data = self.THEMES.get(theme_name, self.THEMES['dark'])
    
    def get_color(self, color_name):
        """Get color from current theme."""
        return self.theme_data.get(color_name, (1, 1, 1, 1))
    
    def set_theme(self, theme_name):
        """Change the current theme."""
        if theme_name in self.THEMES:
            self.current_theme = theme_name
            self.theme_data = self.THEMES[theme_name]
            return True
        return False
    
    def get_all_themes(self):
        """Return list of available themes."""
        return list(self.THEMES.keys())


class CodeAnalyzer:
    """Analyze Python code for complexity and issues."""
    
    @staticmethod
    def count_lines(code):
        """Count lines of code."""
        return len(code.strip().split('\n'))
    
    @staticmethod
    def count_functions(code):
        """Count function definitions."""
        return code.count('def ')
    
    @staticmethod
    def count_classes(code):
        """Count class definitions."""
        return code.count('class ')
    
    @staticmethod
    def count_imports(code):
        """Count import statements."""
        imports = code.count('import ')
        imports += code.count('from ')
        return imports
    
    @staticmethod
    def get_complexity_score(code):
        """Calculate code complexity score (0-100)."""
        score = 0
        
        # Lines of code
        lines = CodeAnalyzer.count_lines(code)
        score += min(lines // 10, 20)
        
        # Nested depth
        score += code.count('    ') // 50
        
        # Conditionals
        score += code.count('if ') * 5
        score += code.count('for ') * 5
        score += code.count('while ') * 5
        
        # Functions and classes
        score += CodeAnalyzer.count_functions(code) * 3
        score += CodeAnalyzer.count_classes(code) * 5
        
        return min(score, 100)
    
    @staticmethod
    def get_code_metrics(code):
        """Get comprehensive code metrics."""
        return {
            'lines': CodeAnalyzer.count_lines(code),
            'functions': CodeAnalyzer.count_functions(code),
            'classes': CodeAnalyzer.count_classes(code),
            'imports': CodeAnalyzer.count_imports(code),
            'complexity': CodeAnalyzer.get_complexity_score(code),
            'empty_lines': code.count('\n\n'),
            'comments': code.count('#'),
        }


class ProgressTracker:
    """Enhanced progress tracking with detailed statistics."""
    
    def __init__(self):
        self.lessons_completed = {}
        self.quiz_scores = {}
        self.code_executions = 0
        self.total_time = 0
        self.session_stats = {}
    
    def mark_lesson_complete(self, lesson_id, score=100):
        """Mark a lesson as complete with a score."""
        self.lessons_completed[lesson_id] = {
            'completed': True,
            'score': score,
            'timestamp': __import__('time').time()
        }
    
    def add_quiz_score(self, quiz_id, score):
        """Add a quiz score."""
        self.quiz_scores[quiz_id] = score
    
    def get_completion_rate(self, total_lessons=7):
        """Get overall completion percentage."""
        if total_lessons == 0:
            return 0
        return (len(self.lessons_completed) / total_lessons) * 100
    
    def get_average_score(self):
        """Get average score across all quizzes."""
        if not self.quiz_scores:
            return 0
        return sum(self.quiz_scores.values()) / len(self.quiz_scores)
    
    def get_statistics(self):
        """Get comprehensive statistics."""
        return {
            'lessons_completed': len(self.lessons_completed),
            'completion_rate': self.get_completion_rate(),
            'average_quiz_score': self.get_average_score(),
            'code_executions': self.code_executions,
            'total_time_minutes': self.total_time // 60,
        }


class SearchFeature:
    """Search functionality for lessons and code examples."""
    
    def __init__(self, lessons_data):
        self.lessons_data = lessons_data
        self.indexed_content = self._build_index()
    
    def _build_index(self):
        """Build searchable index of all content."""
        index = {}
        for i, lesson in enumerate(self.lessons_data):
            title = lesson.get('title', '').lower()
            theory = lesson.get('theory', '').lower()
            practice = lesson.get('practice', '').lower()
            
            # Index by lesson index
            index[i] = {
                'title': title,
                'theory': theory,
                'practice': practice,
                'all_text': f"{title} {theory} {practice}"
            }
        return index
    
    def search(self, query, search_type='all'):
        """Search for content."""
        query = query.lower()
        results = []
        
        for lesson_idx, content in self.indexed_content.items():
            matched = False
            
            if search_type in ['all', 'title'] and query in content['title']:
                matched = True
            if search_type in ['all', 'theory'] and query in content['theory']:
                matched = True
            if search_type in ['all', 'practice'] and query in content['practice']:
                matched = True
            
            if matched:
                results.append({
                    'lesson_index': lesson_idx,
                    'title': self.lessons_data[lesson_idx].get('title', 'Unknown'),
                    'match_type': search_type
                })
        
        return results


class CodeValidator:
    """Validate Python code for common errors."""
    
    @staticmethod
    def check_syntax(code):
        """Check if code has valid Python syntax."""
        try:
            compile(code, '<string>', 'exec')
            return True, "Syntax OK"
        except SyntaxError as e:
            return False, f"Syntax Error: {e.msg}"
    
    @staticmethod
    def check_style(code):
        """Check code style (PEP 8 basic rules)."""
        issues = []
        
        lines = code.split('\n')
        for i, line in enumerate(lines, 1):
            # Check line length
            if len(line) > 120:
                issues.append(f"Line {i}: Too long ({len(line)} chars, max 120)")
            
            # Check for tabs
            if '\t' in line:
                issues.append(f"Line {i}: Uses tabs instead of spaces")
            
            # Check trailing spaces
            if line and line[-1] == ' ':
                issues.append(f"Line {i}: Trailing whitespace")
        
        return issues
    
    @staticmethod
    def get_warnings(code):
        """Get code warnings and suggestions."""
        warnings = []
        
        # Check for bare except
        if 'except:' in code:
            warnings.append("Warning: Bare 'except' is not recommended. Specify exception type.")
        
        # Check for print debugging
        if 'print(' in code and 'debug' in code.lower():
            warnings.append("Tip: Use logging module instead of print for debugging")
        
        # Check for commented code
        if '#' in code and code.count('#') > len(code) / 100:
            warnings.append("Tip: Remove commented-out code before committing")
        
        return warnings


# ─────────────────────────────────────────────
#  Example Usage
# ─────────────────────────────────────────────

if __name__ == "__main__":
    # Theme example
    theme = ThemeManager('dark')
    print(f"Current theme: {theme.current_theme}")
    print(f"Available themes: {theme.get_all_themes()}")
    
    # Code analyzer example
    sample_code = """
def hello(name):
    print(f"Hello, {name}!")

for i in range(5):
    hello(f"User {i}")
"""
    
    metrics = CodeAnalyzer.get_code_metrics(sample_code)
    print(f"\nCode Metrics: {metrics}")
    
    # Code validator example
    valid, msg = CodeValidator.check_syntax(sample_code)
    print(f"Syntax Check: {msg}")
    print(f"Style Issues: {CodeValidator.check_style(sample_code)}")
