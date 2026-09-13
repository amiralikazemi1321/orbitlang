# OrbitLang 🪐

OrbitLang is a small interpreted programming language implemented in Python.

It uses a Python-inspired syntax while keeping the language itself small and understandable. OrbitLang includes its own lexer, parser, AST, tree-walk interpreter, command-line interface, and interactive REPL.

> **Simple syntax. Small language. Built from scratch.**

---

## ✨ Features

### Language

* Variables
* Numbers
* Strings
* Booleans
* Typed assignments
* User input with `input()`
* Output with `show`
* Arithmetic operators
* Comparison operators
* Logical operators: `and`, `or`, `not`
* `if / elif / else`
* One-line conditions
* `while` loops
* `repeat` loops
* `for` loops
* `range()`
* `break` and `continue`
* Functions with `func`
* `return`
* Indentation-based blocks
* Comments

### Tooling & Implementation

* Custom lexer
* Custom parser
* Abstract Syntax Tree (AST)
* Tree-walk interpreter
* Command-line interface
* Interactive REPL
* Lexer and parser error handling
* Interpreter error handling
* Example programs and test programs

---

## 🚀 Quick Start

### Clone the repository

```bash
git clone https://github.com/amiralikazemi1321/orbitlang.git
cd orbitlang
```

### Install OrbitLang

```bash
pip install -e .
```

### Run an OrbitLang program

```bash
orbit run examples/test.orbit
```

You can also run your own programs:

```bash
orbit run program.orbit
```

### Start the REPL

OrbitLang includes an interactive REPL:

```bash
orbit repl
```

Example:

```text
OrbitLang REPL
Type 'exit' to quit.
>>> show "hello"
hello
>>> for i in range(5): show i
0
1
2
3
4
>>> exit
```

---

## 📖 Example

A simple OrbitLang program:

```orbit
name = input("What is your name? ")

if name == "Amir":
    show "Hello, Amir!"
else:
    show "Hello, " + name
```

OrbitLang uses Python-inspired syntax with indentation-based blocks, but it is its own language with its own lexer, parser, AST, and interpreter.

---

## 🧩 Syntax

### Variables

```orbit
x = 10
name = "Orbit"

show x
show name
```

Output:

```text
10
Orbit
```

### Input

User input can be read with `input()`:

```orbit
name = input("What is your name? ")
show name
```

Example output:

```text
What is your name? Amir
Amir
```

### Typed Assignments

OrbitLang supports explicit types:

```orbit
number age = 13
string name = "Amir"
boolean active = true
```

The interpreter checks that assigned values match the declared type.

### Arithmetic

OrbitLang supports basic arithmetic operations:

```orbit
x = 10
y = 5

show x + y
show x - y
show x * y
show x / y
show x % y
```

### Comparisons

Supported comparison operators:

```text
==
!=
<
>
<=
>=
```

Example:

```orbit
x = 10

if x > 5:
    show "x is bigger"
```

### Conditions

Multi-line conditions:

```orbit
x = 10

if x == 10:
    show "correct"
else:
    show "wrong"
```

One-line conditions are also supported:

```orbit
if x > 5: show "big"
```

### `elif`

```orbit
x = 15

if x > 20:
    show "large"
elif x > 10:
    show "medium"
else:
    show "small"
```

### Logical Operators

OrbitLang supports:

```text
and
or
not
```

Example:

```orbit
x = 10

if x > 5 and x < 20:
    show "correct"
```

### `while`

```orbit
x = 0

while x <= 5:
    show x
    x = x + 1
```

### `repeat`

The `repeat` statement runs a block a specified number of times:

```orbit
repeat 5:
    show "hello"
```

One-line form:

```orbit
repeat 3: show "Orbit"
```

### `for`

OrbitLang supports iteration with `for` and `range()`:

```orbit
for i in range(5):
    show i
```

One-line form:

```orbit
for i in range(5): show i
```

### `break` and `continue`

Loops can be controlled with `break` and `continue`:

```orbit
for i in range(10):
    if i == 5:
        break
    show i
```

### Functions

Functions are defined with `func`:

```orbit
func greet(name):
    show "Hello, " + name

greet("Amir")
```

Functions can return values:

```orbit
func add(a, b):
    return a + b

result = add(10, 5)
show result
```

### Comments

Comments start with `#`:

```orbit
# This is a comment

x = 10
show x
```

The `#` character inside strings is preserved:

```orbit
show "hello # world"
```

---

## 🧠 How OrbitLang Works

OrbitLang follows a traditional interpreter pipeline:

```text
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
```

### Lexer

The lexer converts OrbitLang source code into tokens.

It handles:

* Indentation
* Strings and escape sequences
* Numbers
* Keywords
* Operators
* Comments
* Token positions

### Parser

The parser converts the token stream into an Abstract Syntax Tree (AST).

For example:

```orbit
x = 10
```

is represented conceptually as:

```text
Assign
 ├── name: x
 └── value: Number(10)
```

### Interpreter

The interpreter walks the AST and executes the program.

It currently handles:

* Variables
* Expressions
* Input and output
* Arithmetic
* Comparisons
* Logical operations
* Conditions
* Loops
* Functions
* Function calls
* Return values
* `break` and `continue`
* Type checking

---

## 📁 Project Structure

```text
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
```

---

## 🧪 Testing

OrbitLang programs can be used as test cases.

Run an individual test:

```bash
orbit run tests/test_basic.orbit
```

Run all tests:

```bash
for f in tests/*.orbit; do
    echo "=== $f ==="
    orbit run "$f" || exit 1
done
```

---

## 🛠️ Development

OrbitLang is implemented in Python.

The main components are:

```text
orbit/
├── lexer.py        # Source code → tokens
├── parser.py       # Tokens → AST
├── ast.py          # AST node definitions
├── interpreter.py  # AST execution
└── cli.py          # Command-line interface and REPL
```

The project is intentionally structured so that the main stages of a programming language implementation are easy to explore.

---

## 🗺️ Roadmap

Possible future improvements include:

* Lists
* Dictionaries
* Imports and modules
* Standard library
* More comprehensive automated testing
* Multiline REPL input
* Improved error messages and diagnostics
* Better developer tooling
* Additional language features

The roadmap may change as the language evolves.

---

## 🎯 Philosophy

OrbitLang is not intended to replace Python.

The goal is to build a small programming language while exploring how programming languages work internally.

The project focuses on the core stages of an interpreted language:

```text
Lexing
   ↓
Parsing
   ↓
AST
   ↓
Interpretation
```

OrbitLang is intentionally kept relatively small so that its implementation remains understandable and approachable.

---

## 🤝 Contributing

Ideas, bug reports, improvements, and experiments are welcome.

If you are interested in programming languages, interpreters, parsers, or compilers, feel free to explore the project and contribute.

---

## 📜 License

OrbitLang is licensed under the MIT License.

See [LICENSE](LICENSE) for the full license text.

---

**OrbitLang — a small language exploring the world of programming languages. 🪐**
