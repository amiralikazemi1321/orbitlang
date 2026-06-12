import sys
import os

# اضافه کردن مسیر پروژه به PYTHONPATH برای توسعه
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from orbit.interpreter import run_file

def main():
    if len(sys.argv) < 3:
        print("Usage: orbit run <file.orbit>")
        return

    command = sys.argv[1]
    filename = sys.argv[2]

    if command == "run":
        run_file(filename)
    else:
        print("Unknown command:", command)

if __name__ == "__main__":
    main()
