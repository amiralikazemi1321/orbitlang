from orbit.parser import *

variables = {}


def eval_value(v):
    if isinstance(v, Number):
        return v.value
    if isinstance(v, Variable):
        return variables.get(v.name, 0)


def run_block(block):

    for stmt in block:

        if isinstance(stmt, Assign):
            variables[stmt.name] = eval_value(stmt.value)

        elif isinstance(stmt, Print):
            print(eval_value(stmt.value))

        elif isinstance(stmt, If):

            left = variables.get(stmt.var, 0)

            ok = (
                (stmt.op == "==" and left == stmt.val) or
                (stmt.op == ">" and left > stmt.val) or
                (stmt.op == "<" and left < stmt.val)
            )

            if ok:
                run_block(stmt.body)
            elif stmt.else_body:
                run_block(stmt.else_body)


def run_ast(program):
    print("AST SIZE:", len(program.statements))
    run_block(program.statements)
