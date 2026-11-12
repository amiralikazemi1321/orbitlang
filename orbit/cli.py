
import sys

from orbit.interpreter import (
    Interpreter,
    InterpreterError,
    run_file,
)
from orbit.parser import (
    parse_program,
    ParserError,
)
from orbit.lexer import LexerError


def print_error(error, filename=None):
    print(f"Orbit error: {error.message}")

    if filename is None:
        filename = "<repl>"

    print(f"  --> {filename}:{error.line}:{error.column}")


def repl():
    interpreter = Interpreter()

    print("OrbitLang REPL")
    print("Type 'exit' or 'quit' to quit.")

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
            print_error(error)

        except InterpreterError as error:
            print(f"Orbit error: {error}")

        except KeyboardInterrupt:
            print()
            break

        except EOFError:
            print()
            break


def print_usage():
    print("OrbitLang")
    print()
    print("Usage:")
    print("  orbit run <file.orbit>")
    print("  orbit repl")


def main():
    args = sys.argv[1:]

    if not args:
        print_usage()
        return

    command = args[0]

    if command == "run":
        if len(args) < 2:
            print("Usage: orbit run <file.orbit>")
            return

        filename = args[1]

        try:
            run_file(filename)

        except (LexerError, ParserError) as error:
            print_error(error, filename)

        except InterpreterError as error:
            print(f"Orbit error: {error}")

        except (OSError, EOFError) as error:
            print(f"Orbit error: {error}")

        except KeyboardInterrupt:
            print("\nExecution interrupted.")

    elif command == "repl":
        repl()

    elif command in ("help", "--help", "-h"):
        print_usage()

    elif command in ("version", "--version", "-v"):
        print("OrbitLang 0.1.0")

    else:
        print(f"Unknown command: {command}")
        print()
        print_usage()


if __name__ == "__main__":
    main()
