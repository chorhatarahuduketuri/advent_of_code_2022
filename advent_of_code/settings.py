import os
from pathlib import Path

PROJECT_ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent
PUZZLE_INPUT_PATH = PROJECT_ROOT / Path("puzzle_inputs")
