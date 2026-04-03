"""
Challenge & Exercise System for PyLearn
Provides programming challenges with test cases and difficulty levels.
"""

from enum import Enum
from typing import List, Callable
import traceback
import sys
import io


class Difficulty(Enum):
    """Challenge difficulty levels."""
    EASY = 1
    MEDIUM = 2
    HARD = 3
    EXPERT = 4


class Challenge:
    """Represents a single programming challenge."""
    
    def __init__(self, 
                 challenge_id: str,
                 title: str,
                 description: str,
                 starter_code: str,
                 difficulty: Difficulty,
                 test_cases: List[dict],
                 hints: List[str] = None,
                 tags: List[str] = None):
        
        self.challenge_id = challenge_id
        self.title = title
        self.description = description
        self.starter_code = starter_code
        self.difficulty = difficulty
        self.test_cases = test_cases
        self.hints = hints or []
        self.tags = tags or []
        self.solution = None
        self.user_attempt = None
        self.attempts_count = 0
    
    def run_tests(self, user_code: str) -> dict:
        """Run test cases against user code."""
        self.user_attempt = user_code
        self.attempts_count += 1
        
        results = {
            'passed': 0,
            'failed': 0,
            'total': len(self.test_cases),
            'test_results': [],
            'errors': []
        }
        
        for i, test in enumerate(self.test_cases):
            input_data = test.get('input')
            expected_output = test.get('expected_output')
            
            try:
                # Execute user code with test input
                actual_output = self._execute_code(user_code, input_data)
                
                if actual_output.strip() == str(expected_output).strip():
                    results['passed'] += 1
                    results['test_results'].append({
                        'test_num': i + 1,
                        'passed': True,
                        'input': input_data,
                        'expected': expected_output,
                        'actual': actual_output
                    })
                else:
                    results['failed'] += 1
                    results['test_results'].append({
                        'test_num': i + 1,
                        'passed': False,
                        'input': input_data,
                        'expected': expected_output,
                        'actual': actual_output
                    })
            
            except Exception as e:
                results['failed'] += 1
                results['errors'].append(f"Test {i+1}: {str(e)}")
                results['test_results'].append({
                    'test_num': i + 1,
                    'passed': False,
                    'error': str(e)
                })
        
        return results
    
    @staticmethod
    def _execute_code(code: str, input_data: str = "") -> str:
        """Execute code safely and return output."""
        output_buf = io.StringIO()
        old_stdout = sys.stdout
        old_stdin = sys.stdin
        old_stderr = sys.stderr
        
        sys.stdout = output_buf
        sys.stderr = output_buf
        sys.stdin = io.StringIO(input_data)
        
        safe_globals = {
            "__builtins__": {
                "print": print,
                "input": input,
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
                "any": any,
                "all": all,
            }
        }
        
        try:
            exec(compile(code, "<challenge>", "exec"), safe_globals)
        except Exception as e:
            traceback.print_exc()
        finally:
            sys.stdout = old_stdout
            sys.stdin = old_stdin
            sys.stderr = old_stderr
        
        return output_buf.getvalue()
    
    def get_hint(self, hint_num: int = 1) -> str:
        """Get a hint for the challenge."""
        if 0 < hint_num <= len(self.hints):
            return self.hints[hint_num - 1]
        return "No more hints available"


class ChallengeLibrary:
    """Collection of programming challenges."""
    
    def __init__(self):
        self.challenges = {}
        self._load_default_challenges()
    
    def _load_default_challenges(self):
        """Load default challenges for each lesson."""
        
        # Lesson 1: Variables & Data Types
        self.add_challenge(Challenge(
            challenge_id="var_001",
            title="Type Converter",
            description="Convert a string number to integer and multiply by 2",
            starter_code="# Convert the input to int and multiply by 2\nnumber_str = \"42\"\n# TODO: Convert and multiply",
            difficulty=Difficulty.EASY,
            test_cases=[
                {"input": "", "expected_output": "84"},
                {"input": "", "expected_output": "84"}
            ],
            hints=[
                "Use int() to convert string to integer",
                "Use the multiplication operator (*)",
                "Print the result"
            ],
            tags=["variables", "types", "conversion"]
        ))
        
        # Lesson 2: Strings
        self.add_challenge(Challenge(
            challenge_id="str_001",
            title="String Reversal",
            description="Reverse a given string",
            starter_code="text = \"Hello, World!\"\n# TODO: Reverse and print",
            difficulty=Difficulty.EASY,
            test_cases=[
                {"input": "", "expected_output": "!dlroW ,olleH"},
                {"input": "", "expected_output": "!dlroW ,olleH"}
            ],
            hints=[
                "Use string slicing with [::-1]",
                "This creates a reversed copy of the string"
            ],
            tags=["strings", "slicing"]
        ))
        
        # Lesson 3: Control Flow
        self.add_challenge(Challenge(
            challenge_id="flow_001",
            title="Grade Calculator",
            description="Assign grades based on score (90:A, 80:B, 70:C, 60:D, <60:F)",
            starter_code="score = 85\n# TODO: Determine and print grade",
            difficulty=Difficulty.MEDIUM,
            test_cases=[
                {"input": "", "expected_output": "B"},
                {"input": "", "expected_output": "B"}
            ],
            hints=[
                "Use if/elif/else statements",
                "Compare score with thresholds",
                "Return appropriate grade"
            ],
            tags=["control_flow", "conditionals"]
        ))
        
        # Lesson 4: Loops
        self.add_challenge(Challenge(
            challenge_id="loop_001",
            title="Sum of Numbers",
            description="Calculate sum of first n natural numbers",
            starter_code="n = 10\n# TODO: Calculate sum of 1 to n\ntotal = 0",
            difficulty=Difficulty.EASY,
            test_cases=[
                {"input": "", "expected_output": "55"},
                {"input": "", "expected_output": "55"}
            ],
            hints=[
                "Use a for loop with range()",
                "Add each number to a running total",
                "Formula: n * (n + 1) / 2"
            ],
            tags=["loops", "iteration"]
        ))
        
        # Lesson 5: Functions
        self.add_challenge(Challenge(
            challenge_id="func_001",
            title="Factorial Calculator",
            description="Calculate factorial of a number",
            starter_code="# TODO: Define factorial function\ndef factorial(n):\n    pass\n\nprint(factorial(5))",
            difficulty=Difficulty.MEDIUM,
            test_cases=[
                {"input": "", "expected_output": "120"},
                {"input": "", "expected_output": "120"}
            ],
            hints=[
                "Base case: factorial(0) = 1",
                "Recursive case: n * factorial(n-1)",
                "Or use a loop to calculate"
            ],
            tags=["functions", "recursion"]
        ))
        
        # Lesson 6: Lists
        self.add_challenge(Challenge(
            challenge_id="list_001",
            title="List Processor",
            description="Find max, min, and average of a list",
            starter_code="numbers = [45, 23, 67, 12, 89, 34]\n# TODO: Find max, min, average",
            difficulty=Difficulty.MEDIUM,
            test_cases=[
                {"input": "", "expected_output": "89 12 45.0"},
                {"input": "", "expected_output": "89 12 45.0"}
            ],
            hints=[
                "Use max() for maximum",
                "Use min() for minimum",
                "Use sum() and len() for average"
            ],
            tags=["lists", "built-ins"]
        ))
        
        # Lesson 7: Dictionaries
        self.add_challenge(Challenge(
            challenge_id="dict_001",
            title="Word Counter",
            description="Count frequency of words in a string",
            starter_code="text = \"hello world hello python hello\"\n# TODO: Count word frequencies",
            difficulty=Difficulty.MEDIUM,
            test_cases=[
                {"input": "", "expected_output": "hello: 3, world: 1, python: 1"},
                {"input": "", "expected_output": "hello: 3, world: 1, python: 1"}
            ],
            hints=[
                "Split string into words",
                "Use a dictionary to count occurrences",
                "Iterate through words and increment counts"
            ],
            tags=["dictionaries", "strings"]
        ))
    
    def add_challenge(self, challenge: Challenge):
        """Add a challenge to the library."""
        self.challenges[challenge.challenge_id] = challenge
    
    def get_challenge(self, challenge_id: str) -> Challenge:
        """Get a specific challenge."""
        return self.challenges.get(challenge_id)
    
    def get_challenges_by_difficulty(self, difficulty: Difficulty) -> List[Challenge]:
        """Get all challenges of a specific difficulty."""
        return [c for c in self.challenges.values() if c.difficulty == difficulty]
    
    def get_challenges_by_tag(self, tag: str) -> List[Challenge]:
        """Get all challenges with a specific tag."""
        return [c for c in self.challenges.values() if tag in c.tags]
    
    def get_all_challenges(self) -> List[Challenge]:
        """Get all challenges."""
        return list(self.challenges.values())


class ChallengeProgress:
    """Track user progress on challenges."""
    
    def __init__(self):
        self.completed_challenges = {}
        self.challenge_scores = {}
        self.total_attempts = 0
    
    def complete_challenge(self, challenge_id: str, score: int, num_attempts: int):
        """Mark a challenge as completed."""
        self.completed_challenges[challenge_id] = True
        self.challenge_scores[challenge_id] = score
        self.total_attempts += num_attempts
    
    def is_completed(self, challenge_id: str) -> bool:
        """Check if a challenge is completed."""
        return challenge_id in self.completed_challenges
    
    def get_score(self, challenge_id: str) -> int:
        """Get score for a challenge."""
        return self.challenge_scores.get(challenge_id, 0)
    
    def get_completion_rate(self, total_challenges: int) -> float:
        """Get completion percentage."""
        if total_challenges == 0:
            return 0.0
        return (len(self.completed_challenges) / total_challenges) * 100
    
    def get_statistics(self) -> dict:
        """Get progress statistics."""
        return {
            'challenges_completed': len(self.completed_challenges),
            'total_attempts': self.total_attempts,
            'average_attempts': self.total_attempts / len(self.completed_challenges) if self.completed_challenges else 0,
            'average_score': sum(self.challenge_scores.values()) / len(self.challenge_scores) if self.challenge_scores else 0,
        }


# ─────────────────────────────────────────────
#  Example Usage
# ─────────────────────────────────────────────

if __name__ == "__main__":
    # Create library
    library = ChallengeLibrary()
    
    # Get a challenge
    challenge = library.get_challenge("var_001")
    
    print(f"Challenge: {challenge.title}")
    print(f"Difficulty: {challenge.difficulty.name}")
    print(f"Description: {challenge.description}")
    print(f"\nStarter Code:\n{challenge.starter_code}")
    
    # Example user code
    user_code = """
number_str = "42"
result = int(number_str) * 2
print(result)
"""
    
    # Run tests
    results = challenge.run_tests(user_code)
    print(f"\nTest Results:")
    print(f"Passed: {results['passed']}/{results['total']}")
    print(f"Failed: {results['failed']}/{results['total']}")
    
    if results['errors']:
        print(f"Errors: {results['errors']}")
    
    # Track progress
    progress = ChallengeProgress()
    if results['passed'] == results['total']:
        score = 100 - (challenge.attempts_count * 10)
        progress.complete_challenge("var_001", max(0, score), challenge.attempts_count)
    
    print(f"\nProgress: {progress.get_statistics()}")
