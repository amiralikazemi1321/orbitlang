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
    ListLiteral,
    Index,
    IndexAssign,
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


class IndexOutOfRangeError(InterpreterError):
    def __init__(self, index, line=None, column=None):
        self.index = index
        self.line = line
        self.column = column

        super().__init__(f"List index out of range: {index}")


class InvalidIndexTypeError(InterpreterError):
    def __init__(self, index, line=None, column=None):
        self.index = index
        self.line = line
        self.column = column

        super().__init__(
            f"List index must be an integer, "
            f"got {type(index).__name__}."
        )


class InvalidAssignmentTargetError(InterpreterError):
    def __init__(self, target_type, line=None, column=None):
        self.target_type = target_type
        self.line = line
        self.column = column

        super().__init__(
            f"Cannot assign to indexed value of type {target_type}."
        )


class Interpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    # =========================================================
    # Program
    # =========================================================

    def run(self, program):
        if not isinstance(program, Program):
            raise InterpreterError("Expected a Program node.")

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
            value = self.evaluate(statement.value)
            self.variables[statement.name] = value
            return

        if isinstance(statement, IndexAssign):
            value = self.evaluate(statement.value)
            collection = self.evaluate(statement.collection)
            index = self.evaluate(statement.index)

            if not isinstance(index, int) or isinstance(index, bool):
                raise InvalidIndexTypeError(index)

            if not isinstance(collection, list):
                raise InvalidAssignmentTargetError(
                    type(collection).__name__
                )

            try:
                collection[index] = value
            except IndexError:
                raise IndexOutOfRangeError(index) from None

            return

        if isinstance(statement, Show):
            print(self.evaluate(statement.value))
            return

        if isinstance(statement, If):
            condition = self.evaluate(statement.condition)

            if self.is_truthy(condition):
                self.run_block(statement.body)
                return

            for elif_condition, elif_body in (
                statement.elif_branches or []
            ):
                if self.is_truthy(self.evaluate(elif_condition)):
                    self.run_block(elif_body)
                    return

            if statement.else_body is not None:
                self.run_block(statement.else_body)

            return

        if isinstance(statement, While):
            while self.is_truthy(
                self.evaluate(statement.condition)
            ):
                try:
                    self.run_block(statement.body)
                except ContinueSignal:
                    continue
                except BreakSignal:
                    break

            return

        if isinstance(statement, Repeat):
            count = self.evaluate(statement.count)

            if not isinstance(count, int) or isinstance(count, bool):
                raise InterpreterError(
                    "Repeat count must be an integer."
                )

            if count < 0:
                raise InterpreterError(
                    "Repeat count cannot be negative."
                )

            for _ in range(count):
                try:
                    self.run_block(statement.body)
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
                    self.run_block(statement.body)
                except ContinueSignal:
                    continue
                except BreakSignal:
                    break

            return

        if isinstance(statement, TypedAssign):
            value = self.evaluate(statement.value)

            if statement.type_name == "number":
                if (
                    not isinstance(value, (int, float))
                    or isinstance(value, bool)
                ):
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
            f"Unknown statement: {type(statement).__name__}"
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
                    f"Undefined variable: {expression.name}"
                )

            return self.variables[expression.name]

        if isinstance(expression, ListLiteral):
            return [
                self.evaluate(element)
                for element in expression.elements
            ]

        if isinstance(expression, Index):
            collection = self.evaluate(expression.collection)
            index = self.evaluate(expression.index)

            if not isinstance(index, int) or isinstance(index, bool):
                raise InvalidIndexTypeError(index)

            if not isinstance(collection, (list, str)):
                raise InterpreterError(
                    "Indexing requires a list or string."
                )

            try:
                return collection[index]
            except IndexError:
                raise IndexOutOfRangeError(index) from None

        if isinstance(expression, Input):
            prompt = self.evaluate(expression.prompt)
            return input(prompt)

        if isinstance(expression, TypeOf):
            value = self.evaluate(expression.value)

            if isinstance(value, bool):
                return "boolean"

            if isinstance(value, (int, float)):
                return "number"

            if isinstance(value, str):
                return "string"

            if isinstance(value, list):
                return "list"

            return "unknown"

        if isinstance(expression, Call):
            return self.evaluate_call(expression)

        if isinstance(expression, BinaryOp):
            return self.evaluate_binary(expression)

        if isinstance(expression, UnaryOp):
            return self.evaluate_unary(expression)

        raise InterpreterError(
            f"Unknown expression: {type(expression).__name__}"
        )

    # =========================================================
    # Function calls
    # =========================================================

    def evaluate_call(self, expression):
        if expression.name in self.functions:
            function = self.functions[expression.name]

            if len(expression.arguments) != len(function.parameters):
                raise InterpreterError(
                    f"Function '{expression.name}' expects "
                    f"{len(function.parameters)} arguments."
                )

            arguments = [
                self.evaluate(argument)
                for argument in expression.arguments
            ]

            old_variables = self.variables
            self.variables = old_variables.copy()

            for parameter, argument in zip(
                function.parameters,
                arguments,
            ):
                self.variables[parameter] = argument

            try:
                self.run_block(function.body)
            except ReturnSignal as signal:
                return signal.value
            finally:
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
                return range(arguments[0], arguments[1])

            if len(arguments) == 3:
                return range(
                    arguments[0],
                    arguments[1],
                    arguments[2],
                )

            raise InterpreterError(
                "range() expects 1 to 3 arguments."
            )

        if expression.name == "int":
            arguments = [
                self.evaluate(argument)
                for argument in expression.arguments
            ]

            if len(arguments) != 1:
                raise InterpreterError(
                    "int() expects 1 argument."
                )

            try:
                return int(arguments[0])
            except (ValueError, TypeError):
                raise InterpreterError(
                    f"Cannot convert {arguments[0]!r} to an integer."
                ) from None

        raise InterpreterError(
            f"Unknown function: {expression.name}"
        )

    # =========================================================
    # Binary operations
    # =========================================================

    def evaluate_binary(self, expression):
        operator = expression.operator

        if operator == "and":
            left = self.evaluate(expression.left)

            if not self.is_truthy(left):
                return False

            return self.is_truthy(
                self.evaluate(expression.right)
            )

        if operator == "or":
            left = self.evaluate(expression.left)

            if self.is_truthy(left):
                return True

            return self.is_truthy(
                self.evaluate(expression.right)
            )

        left = self.evaluate(expression.left)
        right = self.evaluate(expression.right)

        if operator == "+":
            return left + right

        if operator == "-":
            return left - right

        if operator == "*":
            return left * right

        if operator == "/":
            if right == 0:
                raise InterpreterError("Division by zero.")

            return left / right

        if operator == "%":
            if right == 0:
                raise InterpreterError("Modulo by zero.")

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
        value = self.evaluate(expression.operand)

        if expression.operator == "-":
            return -value

        if expression.operator == "not":
            return not self.is_truthy(value)

        raise InterpreterError(
            f"Unknown unary operator: {expression.operator}"
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
        with open(filename, "r", encoding="utf-8") as file:
            code = file.read()

        program = parse_program(code)
        self.run(program)


# =============================================================
# Public API
# =============================================================

def run_file(filename):
    interpreter = Interpreter()
    interpreter.run_file(filename)