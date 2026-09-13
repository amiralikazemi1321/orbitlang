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
    TypeOf,
    TypedAssign,
    Call,
    For,
    Break,
    Continue,
    FunctionDef,
    Return,
)

from orbit.parser import parse_program


class InterpreterError(Exception):
    pass

class BreakSignal(Exception):
    pass

class ContinueSignal(Exception):
    pass

class ReturnSignal(Exception):
    def __init__(self, value):
        self.value = value

class Interpreter:

    def __init__(self):
        self.variables = {}
        self.functions = {}

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
                try:
                    self.run_block(
                        statement.body
                    )

                except ContinueSignal:
                    continue

                except BreakSignal:
                    break

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
                try:
                    self.run_block(
                        statement.body
                    )

                except ContinueSignal:
                    continue

                except BreakSignal:
                    break

            return

        if isinstance(statement, For):
            iterable = self.evaluate(statement.iterable)

            if not isinstance(iterable, range):
                raise InterpreterError(
                    "For loop requires a range."
                )

            for value in iterable:
                self.variables[statement.variable] = value

                try:
                    self.run_block(
                        statement.body
                    )

                except ContinueSignal:
                    continue

                except BreakSignal:
                    break

            return

        if isinstance(statement, TypedAssign):
            value = self.evaluate(statement.value)

            if statement.type_name == "number":
                if not isinstance(value, (int, float)) or isinstance(value, bool):
                    raise InterpreterError(
                        f"Expected number, got {type(value).__name__}."
                    )

            elif statement.type_name == "string":
                if not isinstance(value, str):
                    raise InterpreterError(
                        f"Expected string, got {type(value).__name__}."
                    )

            elif statement.type_name == "boolean":
                if not isinstance(value, bool):
                    raise InterpreterError(
                        f"Expected boolean, got {type(value).__name__}."
                    )

            self.variables[statement.name] = value

            return

        if isinstance(statement, Break):
            raise BreakSignal()


        if isinstance(statement, Continue):
            raise ContinueSignal()

        if isinstance(statement, FunctionDef):
            self.functions[statement.name] = statement
            return

        if isinstance(statement, Call):
            self.evaluate_call(statement)
            return

        if isinstance(statement, Return):
            value = None

            if statement.value is not None:
                value = self.evaluate(statement.value)

            raise ReturnSignal(value)

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

        if isinstance(expression, TypeOf):

            value = self.evaluate(
                expression.value
            )

            if isinstance(value, bool):
                return "boolean"

            if isinstance(value, int):
                return "number"

            if isinstance(value, float):
                return "number"

            if isinstance(value, str):
                return "string"

            return "unknown"

        if isinstance(expression, Call):
            return self.evaluate_call(expression)

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

    def evaluate_call(self, expression):
        if expression.name in self.functions:
            function = self.functions[expression.name]

            if len(expression.arguments) != len(function.parameters):
                raise InterpreterError(
                    f"Function '{expression.name}' expects "
                    f"{len(function.parameters)} arguments."
                )

            old_variables = self.variables

            self.variables = old_variables.copy()

            for parameter, argument in zip(
                function.parameters,
                expression.arguments,
            ):
                self.variables[parameter] = self.evaluate(argument)

            try:
                self.run_block(function.body)

            except ReturnSignal as signal:
                self.variables = old_variables
                return signal.value

            self.variables = old_variables

            return None
        
        if expression.name == "range":
            arguments = [
                self.evaluate(argument)
                for argument in expression.arguments
            ]

            if not all(
                isinstance(value, int)
                and not isinstance(value, bool)
                for value in arguments
            ):
                raise InterpreterError(
                    "range() arguments must be integers."
                )

            if len(arguments) == 1:
                return range(arguments[0])

            if len(arguments) == 2:
                return range(
                    arguments[0],
                    arguments[1],
                )

            if len(arguments) == 3:
                return range(
                    arguments[0],
                    arguments[1],
                    arguments[2],
                )

            raise InterpreterError(
                "range() expects 1 to 3 arguments."
            )

        raise InterpreterError(
            f"Unknown function: {expression.name}"
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