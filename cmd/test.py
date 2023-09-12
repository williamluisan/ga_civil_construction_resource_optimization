import sys
import os

# Add the path to the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.main import Main
from modules.pygad import *

## test PyGad
def pygad():
    pygad_mod = Pygad()
    pygad_mod.execute()

if __name__ == "__main__":
    pygad()
