import os
import sys

# Add the project root to PYTHONPATH for development.
sys.path.append(
    os.path.dirname(os.path.dirname(__file__))
)

from orbit.interpreter import Interpreter, InterpreterError, run_file
from orbit.parser import parse_program, ParserError
from orbit.lexer import LexerError


def repl():
    interpreter = Interpreter()

    print("OrbitLang REPL")
    print("Type 'exit' to quit.")

    while True:
        try:
            code = input(">>> ")

            if code.strip() in ("exit", "quit"):
                break

            if not code.strip():
                continue

            program = parse_program(code)

            interpreter.run(program)

        except (LexerError, ParserError) as error:
            print(f"Orbit error: {error.message}")
            print(
                f"  --> <repl>:{error.line}:{error.column}"
            )

        except InterpreterError as error:
            print(f"Orbit error: {error}")

        except KeyboardInterrupt:
            print()
            break

def main():
    if len(sys.argv) < 2:
        print("Usage: orbit run <file.orbit>")
        print("       orbit repl")
        return

    command = sys.argv[1]

    if command == "run":
        if len(sys.argv) < 3:
            print("Usage: orbit run <file.orbit>")
            return

        filename = sys.argv[2]

        try:
            run_file(filename)

        except (LexerError, ParserError) as error:
            print(f"Orbit error: {error.message}")
            print(
                f"  --> {filename}:{error.line}:{error.column}"
            )

        except InterpreterError as error:
            print(f"Orbit error: {error}")

    elif command == "repl":
        repl()

    else:
        print("Unknown command:", command)


if __name__ == "__main__":
    main()