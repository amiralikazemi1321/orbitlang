def tokenize(code):
    tokens = []

    current = ""

    for char in code:

        if char.isspace():

            if current:
                tokens.append(current)
                current = ""

        elif char in "+-*/=(){}<>":

            if current:
                tokens.append(current)
                current = ""

            tokens.append(char)

        else:
            current += char


    if current:
        tokens.append(current)


    return tokens
