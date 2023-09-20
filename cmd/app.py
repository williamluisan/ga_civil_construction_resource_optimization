import sys
import os
import textwrap

# Add the path to the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.main import Main

def main():
    argv = sys.argv

    argv_passed = False
    argv_second = None
    if len(argv) == 1 or len(argv) == 2:
        argv_passed = True
        if len(argv) == 2:
            if argv[1] == 'pygad' or argv[1] == 'deap':
                argv_second = argv[1]
            else:
                argv_passed = False

    if argv_passed == True:
        if argv_second == 'pygad':
            Main.execute_pygad()
        elif argv_second == 'deap':
            Main.execute_deap()
        else:
            Main.execute()

    if argv_passed == False:
        message = """
            Usage: python cmd/app.py <options>\n
            Options
                - (empty)\t: using original tailored algorithm by the author
                - pygad\t: using PyGad library
        """
        print(textwrap.dedent(message).strip())

if __name__ == "__main__":
    main()
