OrbitLang 🪐

OrbitLang is a small interpreted programming language implemented in Python.

It uses a Python-inspired syntax while keeping the language itself small and easy to understand. OrbitLang includes its own lexer, parser, AST, interpreter, and command-line interface.

«Simple syntax. Small language. Built from scratch.»

---

✨ Features

Language

- Variables
- Numbers
- Strings
- Booleans
- User input with "input()"
- Output with "show"
- Arithmetic operators
- Comparison operators
- Logical operators
- "if / elif / else"
- One-line conditions
- "while" loops
- "repeat" loops
- Indentation-based blocks
- Comments

Implementation

- Custom lexer
- Custom parser
- Abstract Syntax Tree (AST)
- Tree-walk interpreter
- Command-line interface
- Test programs

---

🚀 Quick Start

Clone the repository:

git clone https://github.com/amiralikazemi1321/orbitlang.git
cd orbitlang

Install OrbitLang:

pip install -e .

Run an OrbitLang program:

orbit run examples/test.orbit

You can also run your own programs:

orbit run program.orbit

---

📖 Example

A simple OrbitLang program:

name = input("What is your name? ")

if name == "Amir":
    show "Hello, Amir!"
else:
    show "Hello, " + name

OrbitLang programs use a Python-inspired syntax with indentation-based blocks.

---

🧩 Syntax

Variables

x = 10
name = "Orbit"

show x
show name

Output:

10
Orbit

---

Input

User input can be read with "input()":

name = input("What is your name? ")

show name

Example output:

What is your name? Amir
Amir

---

Arithmetic

OrbitLang supports basic arithmetic operations:

x = 10
y = 5

show x + y
show x - y
show x * y
show x / y
show x % y

---

Comparisons

Supported comparison operators:

==
!=
<
>
<=
>=

Example:

x = 10

if x > 5:
    show "x is bigger"

---

Conditions

Multi-line conditions:

x = 10

if x == 10:
    show "correct"
else:
    show "wrong"

One-line conditions are also supported:

if x > 5: show "big"

---

"elif"

x = 15

if x > 20:
    show "large"
elif x > 10:
    show "medium"
else:
    show "small"

---

Logical Operators

OrbitLang supports:

and
or
not

Example:

x = 10

if x > 5 and x < 20:
    show "correct"

---

"while"

x = 0

while x <= 5:
    show x
    x = x + 1

---

"repeat"

The "repeat" statement runs a block a specified number of times:

repeat 5:
    show "hello"

One-line form:

repeat 3: show "Orbit"

---

💬 Comments

Comments start with "#":

# This is a comment

x = 10
show x

The "#" character inside strings is preserved:

show "hello # world"

---

🧠 How OrbitLang Works

OrbitLang follows a traditional interpreter pipeline:

Orbit source code
       │
       ▼
     Lexer
       │
       ▼
     Tokens
       │
       ▼
     Parser
       │
       ▼
      AST
       │
       ▼
   Interpreter
       │
       ▼
     Output

Lexer

The lexer converts OrbitLang source code into tokens.

It handles:

- Indentation
- Strings
- Numbers
- Keywords
- Operators
- Comments

Parser

The parser converts the token stream into an Abstract Syntax Tree (AST).

For example:

x = 10

is represented conceptually as:

Assign
 ├── name: x
 └── value: Number(10)

Interpreter

The interpreter walks the AST and executes the program.

It currently handles:

- Variables
- Expressions
- Input
- Output
- Arithmetic
- Comparisons
- Logical operations
- Conditions
- Loops

---

📁 Project Structure

OrbitLang/
│
├── orbit/
│   ├── __init__.py
│   ├── ast.py
│   ├── cli.py
│   ├── interpreter.py
│   ├── lexer.py
│   └── parser.py
│
├── examples/
│   └── test.orbit
│
├── tests/
│   ├── test_basic.orbit
│   ├── test_elif.orbit
│   ├── test_repeat.orbit
│   └── test_while.orbit
│
├── pyproject.toml
├── README.md
└── LICENSE

---

🧪 Testing

OrbitLang programs can be used as test cases.

Run an individual test:

orbit run tests/test_basic.orbit

Run all tests:

for f in tests/*.orbit; do
    echo "=== $f ==="
    orbit run "$f" || exit 1
done

---

🛠️ Development

OrbitLang is implemented in Python.

The main components are:

orbit/
├── lexer.py        # Source code → tokens
├── parser.py       # Tokens → AST
├── ast.py          # AST node definitions
├── interpreter.py  # AST execution
└── cli.py          # Command-line interface

The project is intentionally structured so that the main stages of a programming language implementation are easy to explore.

---

🗺️ Roadmap

Planned and possible future improvements include:

- Functions
- Lists
- Dictionaries
- "break" and "continue"
- Better error messages
- Imports and modules
- Standard library
- More comprehensive testing
- Improved developer tooling

The roadmap may change as the language evolves.

---

🎯 Philosophy

OrbitLang is not intended to replace Python.

The goal is to build a small programming language while exploring how programming languages work internally.

The project focuses on the core stages of an interpreted language:

Lexing
   ↓
Parsing
   ↓
AST
   ↓
Interpretation

OrbitLang is intentionally kept relatively small so that its implementation remains understandable and approachable.

---

🤝 Contributing

Ideas, bug reports, improvements, and experiments are welcome.

If you are interested in programming languages, interpreters, parsers, or compilers, feel free to explore the project and contribute.

---

📜 License

OrbitLang is licensed under the MIT License.

See ""LICENSE"" (LICENSE) for the full license text.

---

OrbitLang — a small language exploring the world of programming languages. 🪐