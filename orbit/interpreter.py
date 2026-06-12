from orbit.parser import parse_program
from orbit.interpreter_ast import run_ast


def run_file(filename):
    with open(filename) as f:
        code = f.read()

    run_ast(parse_program(code))
