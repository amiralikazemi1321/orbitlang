class Number:
    def __init__(self, value):
        self.value = int(value)


class Variable:
    def __init__(self, name):
        self.name = name


class Assign:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Print:
    def __init__(self, value):
        self.value = value


class If:
    def __init__(self, var, op, val, body, else_body=None):
        self.var = var
        self.op = op
        self.val = int(val)
        self.body = body
        self.else_body = else_body


class Program:
    def __init__(self, statements):
        self.statements = statements


def parse_program(code):
    lines = [l.strip() for l in code.split("\n") if l.strip()]
    stmts = []

    i = 0
    while i < len(lines):

        line = lines[i]
        tokens = line.split()

        # SET
        if tokens[0] == "set":
            stmts.append(Assign(tokens[1], Number(tokens[3])))
            i += 1
            continue

        # PRINT
        if tokens[0] == "print":
            v = tokens[1]
            stmts.append(Print(Number(v) if v.isdigit() else Variable(v)))
            i += 1
            continue

        # IF (simple + safe)
        if tokens[0] == "if":

            var = tokens[1]
            op = tokens[2]
            val = tokens[3].replace("{", "")

            i += 1
            body = []

            while i < len(lines) and lines[i] != "}":
                t = lines[i].split()

                if t[0] == "print":
                    body.append(Print(Number(t[1])))
                elif t[0] == "set":
                    body.append(Assign(t[1], Number(t[3])))

                i += 1

            i += 1

            else_body = None

            if i < len(lines) and lines[i].startswith("else"):
                i += 1
                else_body = []

                while i < len(lines) and lines[i] != "}":
                    t = lines[i].split()

                    if t[0] == "print":
                        else_body.append(Print(Number(t[1])))
                    elif t[0] == "set":
                        else_body.append(Assign(t[1], Number(t[3])))

                    i += 1

                i += 1

            stmts.append(If(var, op, val, body, else_body))
            continue

        i += 1

    return Program(stmts)
