
````markdown
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
* User input with `input()`
* Output with `show`
* Arithmetic operations
* Comparisons
* Logical operators
* `if / elif / else`
* One-line conditions
* `while` loops
* `repeat` loops
* Indentation-based blocks
* Comments
* Python-based lexer, parser, AST, and interpreter
* Global `orbit` command for running programs from anywhere

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/amiralikazemi1321/orbitlang.git
cd orbitlang
````

Install OrbitLang:

```bash
pip install -e .
```

Now you can run OrbitLang programs from anywhere:

```bash
orbit run program.orbit
```

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

### Input

OrbitLang supports getting values from the user using `input()`.

```orbit
name = input("What is your name? ")

show name
```

Output:

```text
What is your name? Amir
Amir
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

Multi-line:

```orbit
x = 10

if x == 10:
    show "correct"
else:
    show "wrong"
```

One-line:

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

---

### `repeat`

```orbit
repeat 5:
    show "hello"
```

One-line:

```orbit
repeat 3: show "Orbit"
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

OrbitLang uses a simple interpreter pipeline:

```
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

The lexer converts source code into tokens.

It handles:

* indentation
* strings
* numbers
* keywords
* operators
* comments

### Parser

The parser converts tokens into an Abstract Syntax Tree (AST).

Example:

```orbit
x = 10
```

becomes:

```
Assign
 ├── name: x
 └── value: Number(10)
```

### Interpreter

The interpreter executes the AST.

It handles:

* variables
* expressions
* input
* output
* arithmetic
* comparisons
* conditions
* loops

---

## 📁 Project Structure

```
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

Run a test:

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

OrbitLang is written in Python.

Main components:

```
orbit/lexer.py
orbit/parser.py
orbit/ast.py
orbit/interpreter.py
orbit/cli.py
```

---

## 🗺️ Roadmap

Possible future features:

* Data types
* Functions
* Lists
* Dictionaries
* `break` and `continue`
* Better error messages
* Standard library
* Imports/modules
* More comprehensive testing
* Improved tooling

---

## 🎯 Philosophy

OrbitLang is not intended to replace Python.

Instead, it is a project for exploring how programming languages work while creating a small and enjoyable language.

The project focuses on:

```
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

See the repository for current license information.

---

## ⭐ Contributing

Ideas, bug reports, improvements, and experiments are welcome.

If you are interested in programming languages, interpreters, or compilers, OrbitLang is a small project for learning and experimenting.

---

**OrbitLang — a small language exploring the world of programming languages. 🪐**

