# OrbitLang 🪐

**OrbitLang** is a small, simple, and beginner-friendly programming language written in Python.

The goal of OrbitLang is to keep the readability and familiarity of Python-style syntax while making the language smaller and easier to understand.

> **Simple syntax. Small language. Easy to learn.**

---

## ✨ Features

OrbitLang currently supports:

* Variables
* Numbers
* Strings
* Booleans
* Arithmetic operations
* Comparisons
* Logical operators
* `if / elif / else`
* One-line conditions
* `while` loops
* `repeat` loops
* Indentation-based blocks
* Comments
* A Python-based lexer, parser, AST, and interpreter

---

## 🚀 Quick Start

Clone the repository:

```bash
git clone https://github.com/amiralikazemi1321/orbitlang.git
cd orbitlang
```

Run an OrbitLang program:

```bash
orbit run examples/test.orbit
```

You can also run a file directly through the Python entry point if you're working on the project locally.

---

## 📖 Syntax

OrbitLang intentionally uses a Python-like syntax.

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

---

### Arithmetic

```orbit
x = 10
y = 5

show x + y
show x - y
show x * y
show x / y
show x % y
```

---

### Comparisons

OrbitLang supports:

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

---

### Conditions

A normal multi-line condition:

```orbit
x = 10

if x == 10:
    show "correct"
else:
    show "wrong"
```

OrbitLang also supports short one-line conditions:

```orbit
if x > 5: show "big"
```

---

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

---

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

---

### `while`

```orbit
x = 0

while x <= 5:
    show x
    x = x + 1
```

Output:

```text
0
1
2
3
4
5
```

One-line loops are also supported:

```orbit
while x < 5: show x
```

---

### `repeat`

`repeat` is useful when you want to execute something a fixed number of times.

```orbit
repeat 5:
    show "hello"
```

Output:

```text
hello
hello
hello
hello
hello
```

One-line syntax:

```orbit
repeat 3: show "Orbit"
```

Output:

```text
Orbit
Orbit
Orbit
```

The repeat count can also be an expression:

```orbit
x = 2

repeat x + 1:
    show x
```

---

## 💬 Comments

Comments start with `#`.

```orbit
# This is a comment

x = 10
show x
```

Comments inside strings are preserved:

```orbit
show "hello # world"
```

---

## 🧠 How OrbitLang Works

OrbitLang is implemented as a small interpreter pipeline:

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

For example:

```orbit
x = 10
```

becomes a sequence containing tokens such as:

```text
IDENTIFIER
OPERATOR
NUMBER
NEWLINE
```

The lexer also handles:

* indentation
* strings
* numbers
* keywords
* operators
* comments

---

### Parser

The parser takes the tokens produced by the lexer and builds an **Abstract Syntax Tree (AST)**.

For example:

```orbit
x = 10
```

becomes an assignment node containing:

```text
Assign
 ├── name: x
 └── value: Number(10)
```

---

### Interpreter

The interpreter walks through the AST and executes the program.

It handles:

* variables
* expressions
* arithmetic
* comparisons
* conditions
* loops
* output

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
└── ...
```

---

## 🧪 Tests

OrbitLang includes small `.orbit` programs used to test the language.

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

The tests currently cover:

* basic expressions
* variables
* conditions
* `elif`
* `while`
* `repeat`

---

## 🛠️ Development

OrbitLang is written in **Python**.

The interpreter is intentionally kept small so that the implementation is easy to read and modify.

If you want to work on the language, the main components to look at are:

```text
orbit/lexer.py
orbit/parser.py
orbit/ast.py
orbit/interpreter.py
orbit/cli.py
```

---

## 🗺️ Roadmap

OrbitLang is still a small language and is actively being developed.

Possible future features include:

* Functions
* Lists
* Dictionaries
* More string operations
* `break` and `continue`
* Better error messages
* Standard library
* Imports/modules
* More comprehensive testing
* Improved tooling

The roadmap may change as the language evolves.

---

## 🎯 Philosophy

OrbitLang is not intended to replace Python.

Instead, it is a project for exploring how programming languages work while creating a language that is pleasant and simple to write.

The project focuses on understanding the fundamentals:

```text
Lexing
   ↓
Parsing
   ↓
AST
   ↓
Interpretation
```

---

## 📜 License

This project is currently under development.

See the repository for the current license information.

---

## ⭐ Contributing

Ideas, bug reports, improvements, and experiments are welcome.

If you're interested in programming languages, interpreters, or compilers, OrbitLang is a small project that can be a good place to experiment with these concepts.

---

**OrbitLang — a small language exploring the world of programming languages. 🪐**
