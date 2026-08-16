from dataclasses import dataclass


@dataclass
class Token:
    type: str
    value: object
    line: int
    column: int


KEYWORDS = {
    "show": "SHOW",
    "if": "IF",
    "else": "ELSE",
    "elif": "ELIF",
    "while": "WHILE",
    "repeat": "REPEAT",
    "true": "TRUE",
    "false": "FALSE",
    "and": "AND",
    "or": "OR",
    "not": "NOT",
    "input": "INPUT",
    "type": "TYPE",
}


class LexerError(Exception):
    pass


class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []

        self.line = 1
        self.column = 1

        # Indentation levels.
        # The first level is always zero.
        self.indent_stack = [0]

    def tokenize(self):
        lines = self.code.splitlines()

        for line_number, raw_line in enumerate(lines, start=1):
            self.line = line_number

            # Completely empty line
            if not raw_line.strip():
                continue

            # Remove comments while preserving strings.
            line = self._remove_comment(raw_line)

            # A line that contained only a comment
            if not line.strip():
                continue

            # Count indentation.
            indentation = self._get_indentation(line)

            content = line[indentation:]

            self._handle_indentation(indentation)

            self._tokenize_line(content)

            # Every logical source line ends with NEWLINE.
            self.tokens.append(
                Token(
                    "NEWLINE",
                    None,
                    self.line,
                    len(line) + 1,
                )
            )

        # Close all open indentation blocks.
        while len(self.indent_stack) > 1:
            self.indent_stack.pop()

            self.tokens.append(
                Token(
                    "DEDENT",
                    None,
                    self.line,
                    1,
                )
            )

        self.tokens.append(
            Token(
                "EOF",
                None,
                self.line + 1,
                1,
            )
        )

        return self.tokens

    # =========================================================
    # Indentation
    # =========================================================

    def _get_indentation(self, line):
        count = 0

        for char in line:
            if char == " ":
                count += 1

            elif char == "\t":
                # Treat a tab as four spaces.
                count += 4

            else:
                break

        return count

    def _handle_indentation(self, indentation):
        current = self.indent_stack[-1]

        # Increased indentation
        if indentation > current:
            self.indent_stack.append(indentation)

            self.tokens.append(
                Token(
                    "INDENT",
                    indentation,
                    self.line,
                    1,
                )
            )

            return

        # Decreased indentation
        if indentation < current:
            while (
                len(self.indent_stack) > 1
                and indentation < self.indent_stack[-1]
            ):
                self.indent_stack.pop()

                self.tokens.append(
                    Token(
                        "DEDENT",
                        None,
                        self.line,
                        1,
                    )
                )

            # Indentation must match an existing level.
            if indentation != self.indent_stack[-1]:
                raise LexerError(
                    f"Invalid indentation at line {self.line}"
                )

    # =========================================================
    # Comments
    # =========================================================

    def _remove_comment(self, line):
        result = []

        quote = None
        escaped = False

        for char in line:
            if escaped:
                result.append(char)
                escaped = False
                continue

            if char == "\\":
                result.append(char)
                escaped = True
                continue

            if char in ("'", '"'):
                if quote is None:
                    quote = char

                elif quote == char:
                    quote = None

                result.append(char)
                continue

            if char == "#" and quote is None:
                break

            result.append(char)

        return "".join(result)

    # =========================================================
    # Line tokenizer
    # =========================================================

    def _tokenize_line(self, line):
        i = 0

        while i < len(line):
            char = line[i]

            # Whitespace
            if char.isspace():
                i += 1
                continue

            # -------------------------------------------------
            # Numbers
            # -------------------------------------------------

            if char.isdigit():
                start = i

                while i < len(line) and line[i].isdigit():
                    i += 1

                value = int(line[start:i])

                self.tokens.append(
                    Token(
                        "NUMBER",
                        value,
                        self.line,
                        start + 1,
                    )
                )

                continue

            # -------------------------------------------------
            # Strings
            # -------------------------------------------------

            if char in ("'", '"'):
                i = self._read_string(line, i)
                continue

            # -------------------------------------------------
            # Identifiers / keywords
            # -------------------------------------------------

            if char.isalpha() or char == "_":
                start = i

                while i < len(line):
                    current = line[i]

                    if current.isalnum() or current == "_":
                        i += 1
                    else:
                        break

                value = line[start:i]

                token_type = KEYWORDS.get(
                    value,
                    "IDENTIFIER",
                )

                self.tokens.append(
                    Token(
                        token_type,
                        value,
                        self.line,
                        start + 1,
                    )
                )

                continue

            # -------------------------------------------------
            # Two-character operators
            # -------------------------------------------------

            if i + 1 < len(line):
                operator = line[i:i + 2]

                if operator in {
                    "==",
                    "!=",
                    "<=",
                    ">=",
                }:
                    self.tokens.append(
                        Token(
                            "OPERATOR",
                            operator,
                            self.line,
                            i + 1,
                        )
                    )

                    i += 2
                    continue

            # -------------------------------------------------
            # One-character operators
            # -------------------------------------------------

            if char in {
                "=",
                "+",
                "-",
                "*",
                "/",
                "%",
                "<",
                ">",
            }:
                self.tokens.append(
                    Token(
                        "OPERATOR",
                        char,
                        self.line,
                        i + 1,
                    )
                )

                i += 1
                continue

            # -------------------------------------------------
            # Punctuation
            # -------------------------------------------------

            punctuation = {
                ":": "COLON",
                "(": "LPAREN",
                ")": "RPAREN",
                ",": "COMMA",
            }

            if char in punctuation:
                self.tokens.append(
                    Token(
                        punctuation[char],
                        char,
                        self.line,
                        i + 1,
                    )
                )

                i += 1
                continue

            # -------------------------------------------------
            # Unknown character
            # -------------------------------------------------

            raise LexerError(
                f"Unexpected character {char!r} "
                f"at line {self.line}, "
                f"column {i + 1}"
            )

    # =========================================================
    # String reader
    # =========================================================

    def _read_string(self, line, start):
        quote = line[start]

        i = start + 1
        value = []

        escapes = {
            "n": "\n",
            "t": "\t",
            "r": "\r",
            "\\": "\\",
            "'": "'",
            '"': '"',
        }

        while i < len(line):
            char = line[i]

            # Closing quote
            if char == quote:
                self.tokens.append(
                    Token(
                        "STRING",
                        "".join(value),
                        self.line,
                        start + 1,
                    )
                )

                return i + 1

            # Escape sequence
            if char == "\\":
                i += 1

                if i >= len(line):
                    raise LexerError(
                        f"Unterminated string at line "
                        f"{self.line}, "
                        f"column {start + 1}"
                    )

                escaped_char = line[i]

                value.append(
                    escapes.get(
                        escaped_char,
                        escaped_char,
                    )
                )

                i += 1
                continue

            value.append(char)
            i += 1

        raise LexerError(
            f"Unterminated string at line "
            f"{self.line}, "
            f"column {start + 1}"
        )

