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
    Repeat,
    Program,
)


class ParserError(Exception):
    pass


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    # =========================================================
    # Token helpers
    # =========================================================

    def current(self):
        return self.tokens[self.position]

    def peek(self, offset=1):
        index = self.position + offset

        if index >= len(self.tokens):
            return self.tokens[-1]

        return self.tokens[index]

    def advance(self):
        token = self.current()
        self.position += 1
        return token

    def check(self, token_type):
        return self.current().type == token_type

    def match(self, token_type):
        if self.check(token_type):
            return self.advance()

        return None

    def expect(self, token_type):
        if not self.check(token_type):
            token = self.current()

            raise ParserError(
                f"Expected {token_type}, "
                f"got {token.type} "
                f"at line {token.line}, "
                f"column {token.column}"
            )

        return self.advance()

    def skip_newlines(self):
        while self.match("NEWLINE"):
            pass

    # =========================================================
    # Program
    # =========================================================

    def parse(self):
        statements = []

        self.skip_newlines()

        while not self.check("EOF"):
            statements.append(self.parse_statement())
            self.skip_newlines()

        return Program(statements)

    # =========================================================
    # Statements
    # =========================================================

    def parse_statement(self):
        token = self.current()

        if token.type == "SHOW":
            return self.parse_show()

        if token.type == "IF":
            return self.parse_if()

        if token.type == "WHILE":
            return self.parse_while()

        if token.type == "REPEAT":
            return self.parse_repeat()

        if token.type == "IDENTIFIER":
            return self.parse_assignment()

        raise ParserError(
            f"Unexpected token {token.type} "
            f"at line {token.line}, "
            f"column {token.column}"
        )

    # =========================================================
    # Assignment
    # =========================================================

    def parse_assignment(self):
        name = self.expect("IDENTIFIER").value

        self.expect_operator("=")

        value = self.parse_expression()

        self.match("NEWLINE")

        return Assign(name, value)

    # =========================================================
    # Show
    # =========================================================

    def parse_show(self):
        self.expect("SHOW")

        value = self.parse_expression()

        self.match("NEWLINE")

        return Show(value)

    # =========================================================
    # If / Elif / Else
    # =========================================================

    def parse_if(self):
        self.expect("IF")

        condition = self.parse_expression()

        self.expect("COLON")

        # -----------------------------------------------------
        # One-line IF
        # -----------------------------------------------------

        if not self.check("NEWLINE"):
            body = [self.parse_statement()]

            elif_branches = []

            while self.check("ELIF"):
                self.advance()

                elif_condition = self.parse_expression()

                self.expect("COLON")

                elif_body = [
                    self.parse_statement()
                ]

                elif_branches.append(
                    (elif_condition, elif_body)
                )

            else_body = None

            if self.check("ELSE"):
                self.advance()

                self.expect("COLON")

                else_body = [
                    self.parse_statement()
                ]

            return If(
                condition,
                body,
                elif_branches,
                else_body,
            )

        # -----------------------------------------------------
        # Multi-line IF
        # -----------------------------------------------------

        self.expect("NEWLINE")
        self.expect("INDENT")

        body = []

        self.skip_newlines()

        while not self.check("DEDENT"):
            body.append(
                self.parse_statement()
            )
            self.skip_newlines()

        self.expect("DEDENT")

        # -----------------------------------------------------
        # ELIF
        # -----------------------------------------------------

        elif_branches = []

        while self.check("ELIF"):
            self.advance()

            elif_condition = self.parse_expression()

            self.expect("COLON")

            if not self.check("NEWLINE"):
                elif_body = [
                    self.parse_statement()
                ]

            else:
                self.expect("NEWLINE")
                self.expect("INDENT")

                elif_body = []

                self.skip_newlines()

                while not self.check("DEDENT"):
                    elif_body.append(
                        self.parse_statement()
                    )
                    self.skip_newlines()

                self.expect("DEDENT")

            elif_branches.append(
                (elif_condition, elif_body)
            )

        # -----------------------------------------------------
        # ELSE
        # -----------------------------------------------------

        else_body = None

        if self.check("ELSE"):
            self.advance()

            self.expect("COLON")

            if not self.check("NEWLINE"):
                else_body = [
                    self.parse_statement()
                ]

            else:
                self.expect("NEWLINE")
                self.expect("INDENT")

                else_body = []

                self.skip_newlines()

                while not self.check("DEDENT"):
                    else_body.append(
                        self.parse_statement()
                    )
                    self.skip_newlines()

                self.expect("DEDENT")

        return If(
            condition,
            body,
            elif_branches,
            else_body,
        )

    # =========================================================
    # While
    # =========================================================

    def parse_while(self):
        self.expect("WHILE")

        condition = self.parse_expression()

        self.expect("COLON")

        # -----------------------------------------------------
        # One-line WHILE
        # -----------------------------------------------------

        if not self.check("NEWLINE"):
            body = [
                self.parse_statement()
            ]

            return While(
                condition,
                body,
            )

        # -----------------------------------------------------
        # Multi-line WHILE
        # -----------------------------------------------------

        self.expect("NEWLINE")
        self.expect("INDENT")

        body = []

        self.skip_newlines()

        while not self.check("DEDENT"):
            body.append(
                self.parse_statement()
            )
            self.skip_newlines()

        self.expect("DEDENT")

        return While(
            condition,
            body,
        )

    # =========================================================
    # Repeat
    # =========================================================

    def parse_repeat(self):
        self.expect("REPEAT")

        count = self.parse_expression()

        self.expect("COLON")

        # -----------------------------------------------------
        # One-line REPEAT
        # -----------------------------------------------------

        if not self.check("NEWLINE"):
            body = [
                self.parse_statement()
            ]

            return Repeat(
                count,
                body,
            )

        # -----------------------------------------------------
        # Multi-line REPEAT
        # -----------------------------------------------------

        self.expect("NEWLINE")
        self.expect("INDENT")

        body = []

        self.skip_newlines()

        while not self.check("DEDENT"):
            body.append(
                self.parse_statement()
            )
            self.skip_newlines()

        self.expect("DEDENT")

        return Repeat(
            count,
            body,
        )

    # =========================================================
    # Expressions
    # =========================================================

    def parse_expression(self):
        return self.parse_or()

    def parse_or(self):
        left = self.parse_and()

        while self.check("OR"):
            operator = self.advance().value
            right = self.parse_and()

            left = BinaryOp(
                left,
                operator,
                right,
            )

        return left

    def parse_and(self):
        left = self.parse_comparison()

        while self.check("AND"):
            operator = self.advance().value
            right = self.parse_comparison()

            left = BinaryOp(
                left,
                operator,
                right,
            )

        return left

    def parse_comparison(self):
        left = self.parse_term()

        while (
            self.check_operator("==")
            or self.check_operator("!=")
            or self.check_operator("<")
            or self.check_operator(">")
            or self.check_operator("<=")
            or self.check_operator(">=")
        ):
            operator = self.advance().value
            right = self.parse_term()

            left = BinaryOp(
                left,
                operator,
                right,
            )

        return left

    def parse_term(self):
        left = self.parse_factor()

        while (
            self.check_operator("+")
            or self.check_operator("-")
        ):
            operator = self.advance().value
            right = self.parse_factor()

            left = BinaryOp(
                left,
                operator,
                right,
            )

        return left

    def parse_factor(self):
        left = self.parse_unary()

        while (
            self.check_operator("*")
            or self.check_operator("/")
            or self.check_operator("%")
        ):
            operator = self.advance().value
            right = self.parse_unary()

            left = BinaryOp(
                left,
                operator,
                right,
            )

        return left

    def parse_unary(self):
        if self.check_operator("-"):
            operator = self.advance().value

            return UnaryOp(
                operator,
                self.parse_unary(),
            )

        if self.check("NOT"):
            operator = self.advance().value

            return UnaryOp(
                operator,
                self.parse_unary(),
            )

        return self.parse_primary()

    def parse_primary(self):
        token = self.current()

        if token.type == "NUMBER":
            self.advance()
            return Number(token.value)

        if token.type == "STRING":
            self.advance()
            return String(token.value)

        if token.type == "TRUE":
            self.advance()
            return Boolean(True)

        if token.type == "FALSE":
            self.advance()
            return Boolean(False)

        if token.type == "INPUT":
            self.advance()

            self.expect("LPAREN")

            prompt = self.parse_expression()

            self.expect("RPAREN")

            return Input(prompt)

        if token.type == "IDENTIFIER":
            self.advance()
            return Variable(token.value)

        if token.type == "LPAREN":
            self.advance()

            expression = self.parse_expression()

            self.expect("RPAREN")

            return expression

        raise ParserError(
            f"Expected expression, "
            f"got {token.type} "
            f"at line {token.line}, "
            f"column {token.column}"
        )

    # =========================================================
    # Operators
    # =========================================================

    def check_operator(self, operator):
        return (
            self.current().type == "OPERATOR"
            and self.current().value == operator
        )

    def expect_operator(self, operator):
        if not self.check_operator(operator):
            token = self.current()

            raise ParserError(
                f"Expected operator {operator!r}, "
                f"got {token.value!r} "
                f"at line {token.line}"
            )

        return self.advance()


# =============================================================
# Public API
# =============================================================

def parse_program(code):
    from orbit.lexer import Lexer

    tokens = Lexer(code).tokenize()

    parser = Parser(tokens)

    return parser.parse()