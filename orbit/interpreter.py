from orbit.ast import (
    Number,
    String,
    Boolean,
    Variable,
    BinaryOp,
    UnaryOp,
    Assign,
    Show,
    Input,
    If,
    While,
    Program,
    Repeat,
)

from orbit.parser import parse_program


class InterpreterError(Exception):
    pass


class Interpreter:

    def __init__(self):
        self.variables = {}

    # =========================================================
    # Program
    # =========================================================

    def run(self, program):
        if not isinstance(program, Program):
            raise InterpreterError(
                "Expected a Program node."
            )

        self.run_block(program.statements)

    # =========================================================
    # Block
    # =========================================================

    def run_block(self, statements):
        for statement in statements:
            self.execute(statement)

    # =========================================================
    # Statements
    # =========================================================

    def execute(self, statement):

        if isinstance(statement, Assign):
            value = self.evaluate(
                statement.value
            )

            self.variables[
                statement.name
            ] = value

            return


        if isinstance(statement, Show):
            value = self.evaluate(
                statement.value
            )

            print(value)

            return


        if isinstance(statement, If):

            condition = self.evaluate(
                statement.condition
            )

            if self.is_truthy(condition):
                self.run_block(
                    statement.body
                )

                return

            for (
                elif_condition,
                elif_body,
            ) in statement.elif_branches or []:

                condition = self.evaluate(
                    elif_condition
                )

                if self.is_truthy(condition):
                    self.run_block(
                        elif_body
                    )

                    return

            if statement.else_body is not None:
                self.run_block(
                    statement.else_body
                )

            return


        if isinstance(statement, While):

            while self.is_truthy(
                self.evaluate(
                    statement.condition
                )
            ):
                self.run_block(
                    statement.body
                )

            return


        if isinstance(statement, Repeat):

            count = self.evaluate(
                statement.count
            )

            if not isinstance(count, int):
                raise InterpreterError(
                    "Repeat count must be an integer."
                )

            if count < 0:
                raise InterpreterError(
                    "Repeat count cannot be negative."
                )

            for _ in range(count):
                self.run_block(
                    statement.body
                )

            return


        raise InterpreterError(
            f"Unknown statement: "
            f"{type(statement).__name__}"
        )

    # =========================================================
    # Expressions
    # =========================================================

    def evaluate(self, expression):

        if isinstance(expression, Number):
            return expression.value


        if isinstance(expression, String):
            return expression.value


        if isinstance(expression, Boolean):
            return expression.value


        if isinstance(expression, Variable):

            if expression.name not in self.variables:
                raise InterpreterError(
                    f"Undefined variable: "
                    f"{expression.name}"
                )

            return self.variables[
                expression.name
            ]


        # ==========================
        # INPUT SUPPORT
        # ==========================

        if isinstance(expression, Input):

            prompt = self.evaluate(
                expression.prompt
            )

            return input(prompt)


        if isinstance(expression, BinaryOp):

            return self.evaluate_binary(
                expression
            )


        if isinstance(expression, UnaryOp):

            return self.evaluate_unary(
                expression
            )


        raise InterpreterError(
            f"Unknown expression: "
            f"{type(expression).__name__}"
        )

    # =========================================================
    # Binary operations
    # =========================================================

    def evaluate_binary(self, expression):

        operator = expression.operator


        if operator == "and":

            left = self.evaluate(
                expression.left
            )

            if not self.is_truthy(left):
                return False

            right = self.evaluate(
                expression.right
            )

            return self.is_truthy(right)


        if operator == "or":

            left = self.evaluate(
                expression.left
            )

            if self.is_truthy(left):
                return True

            right = self.evaluate(
                expression.right
            )

            return self.is_truthy(right)


        left = self.evaluate(
            expression.left
        )

        right = self.evaluate(
            expression.right
        )


        if operator == "+":
            return left + right


        if operator == "-":
            return left - right


        if operator == "*":
            return left * right


        if operator == "/":

            if right == 0:
                raise InterpreterError(
                    "Division by zero."
                )

            return left / right


        if operator == "%":

            if right == 0:
                raise InterpreterError(
                    "Modulo by zero."
                )

            return left % right


        if operator == "==":
            return left == right


        if operator == "!=":
            return left != right


        if operator == "<":
            return left < right


        if operator == ">":
            return left > right


        if operator == "<=":
            return left <= right


        if operator == ">=":
            return left >= right


        raise InterpreterError(
            f"Unknown operator: {operator}"
        )

    # =========================================================
    # Unary operations
    # =========================================================

    def evaluate_unary(self, expression):

        value = self.evaluate(
            expression.operand
        )

        if expression.operator == "-":
            return -value


        if expression.operator == "not":
            return not self.is_truthy(value)


        raise InterpreterError(
            f"Unknown unary operator: "
            f"{expression.operator}"
        )

    # =========================================================
    # Truthiness
    # =========================================================

    def is_truthy(self, value):
        return bool(value)

    # =========================================================
    # File execution
    # =========================================================

    def run_file(self, filename):

        with open(
            filename,
            "r",
            encoding="utf-8",
        ) as file:
            code = file.read()

        program = parse_program(code)

        self.run(program)


# =============================================================
# Public API
# =============================================================

def run_file(filename):

    interpreter = Interpreter()

    interpreter.run_file(filename)