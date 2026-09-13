# OrbitLang 🪐

OrbitLang is a small interpreted programming language implemented in Python.

It uses a Python-inspired syntax while keeping the language itself small and understandable. OrbitLang includes its own lexer, parser, Abstract Syntax Tree (AST), tree-walk interpreter, command-line interface, interactive REPL, and graphical installer.

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
* `break`
* `continue`
* Functions with `func`
* Function parameters
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
* Graphical installer built with Tkinter
* Lexer error handling
* Parser error handling
* Interpreter error handling
* Example programs
* Language-level test programs

---

## 🚀 Quick Start

### Requirements

* Python 3.10 or newer
* A terminal

Clone the repository:

```bash
git clone https://github.com/amiralikazemi1321/orbitlang.git
cd orbitlang
```

Install OrbitLang:

```bash
pip install .
```

After installation, the `orbit` command will be available from your terminal.

---

## ▶️ Running OrbitLang

Create a file with the `.orbit` extension:

```orbit
show "Hello, OrbitLang!"
```

Save it as:

```text
hello.orbit
```

Then run:

```bash
orbit run hello.orbit
```

Output:

```text
Hello, OrbitLang!
```

---

## 💻 REPL

OrbitLang provides an interactive REPL:

```bash
orbit repl
```

Example:

```text
OrbitLang REPL
Type 'exit' to quit.
>>> show "Hello"
Hello
>>> show 10 + 5
15
>>> exit
```

The current REPL is designed for single-line interaction. Multiline interactive blocks are planned for a future version.

---

# 📦 Installer

OrbitLang includes a graphical installer built with Tkinter.

The installer provides a simple way to install OrbitLang without manually configuring the project.

### Installer Features

* Graphical installation interface
* Python version check
* Custom installation directory
* Installation progress
* OrbitLang CLI setup
* PATH configuration
* Installation completion screen
* Installation cancellation

### Running the Installer

From the root of the repository:

```bash
python installer/installer.py
```

The installer will guide you through the installation process.

> **Note:** OrbitLang requires Python to run. The installer does not install Python automatically.

On some Linux distributions, Tkinter may be provided as a separate system package.

For Fedora:

```bash
sudo dnf install python3-tkinter
```

### After Installation

Open a new terminal and run:

```bash
orbit repl
```

Or execute an OrbitLang program:

```bash
orbit run program.orbit
```

---

# 📖 Language Syntax

## Variables

Variables can be created with a simple assignment:

```orbit
name = "Amir"
age = 13

show name
show age
```

---

## Data Types

OrbitLang currently supports:

* Numbers
* Strings
* Booleans

Examples:

```orbit
age = 13
name = "Amir"
active = true
```

---

## Typed Assignments

Variables can optionally specify their type:

```orbit
number age = 13
string name = "Amir"
boolean active = true
```

The interpreter checks that the assigned value matches the declared type.

---

## Output

Use `show` to print a value:

```orbit
show "Hello"
show 10
show 5 + 3
```

---

## Input

Use `input()` to read user input:

```orbit
name = input("What is your name? ")

show name
```

---

## Arithmetic

OrbitLang supports common arithmetic operators:

```orbit
x = 10
y = 5

show x + y
show x - y
show x * y
show x / y
```

---

## Comparisons

Comparison operators can be used in expressions and conditions:

```orbit
x = 10

show x == 10
show x != 5
show x > 5
show x < 20
show x >= 10
show x <= 10
```

---

## Conditions

OrbitLang uses indentation to define blocks:

```orbit
x = 10

if x > 5:
    show "x is bigger"
```

One-line conditions are also supported:

```orbit
if x > 5: show "x is bigger"
```

---

## `elif` and `else`

```orbit
x = 15

if x > 20:
    show "big"
elif x > 10:
    show "medium"
else:
    show "small"
```

They can also be written in one-line form:

```orbit
if x > 20: show "big"
elif x > 10: show "medium"
else: show "small"
```

---

## Logical Operators

OrbitLang supports:

* `and`
* `or`
* `not`

Example:

```orbit
age = 13

if age > 10 and age < 18:
    show "teenager"
```

---

## `while` Loops

```orbit
x = 0

while x < 5:
    show x
    x = x + 1
```

One-line loops are also supported:

```orbit
while x < 5: x = x + 1
```

---

## `repeat` Loops

`repeat` executes a block a specified number of times:

```orbit
repeat 5:
    show "Hello"
```

One-line form:

```orbit
repeat 3: show "Orbit"
```

---

## `for` Loops

OrbitLang supports `for` loops with iterables such as `range()`:

```orbit
for i in range(5):
    show i
```

Output:

```text
0
1
2
3
4
```

One-line form:

```orbit
for i in range(5): show i
```

### `range()`

`range()` supports one, two, or three integer arguments:

```orbit
range(5)
range(2, 5)
range(0, 10, 2)
```

---

## `break` and `continue`

`break` stops the current loop:

```orbit
for i in range(10):
    if i == 5:
        break

    show i
```

`continue` skips the rest of the current iteration:

```orbit
for i in range(5):
    if i == 2:
        continue

    show i
```

---

## Functions

Functions are declared using `func`:

```orbit
func greet(name):
    show name
```

Functions can receive parameters:

```orbit
func add(a, b):
    return a + b
```

They can then be called:

```orbit
result = add(10, 5)
show result
```

---

## `return`

`return` sends a value back from a function:

```orbit
func square(x):
    return x * x

show square(5)
```

A function can also return without a value:

```orbit
func hello():
    show "Hello"
    return
```

---

## Comments

Comments start with `#`:

```orbit
# This is a comment

x = 10  # This is also a comment
```

---

# 🧠 How OrbitLang Works

OrbitLang follows a traditional interpreter pipeline:

```text
OrbitLang source code
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

The lexer reads source code and converts it into tokens.

It handles:

* Keywords
* Identifiers
* Numbers
* Strings
* Operators
* Indentation
* New lines
* Comments

### Parser

The parser takes the tokens produced by the lexer and builds an Abstract Syntax Tree.

It is responsible for understanding OrbitLang's grammar and structure.

### AST

The AST represents the structure of a program using Python objects such as:

* `Number`
* `String`
* `Boolean`
* `Variable`
* `BinaryOp`
* `Assign`
* `If`
* `While`
* `For`
* `FunctionDef`
* `Return`
* `Call`

### Interpreter

The interpreter walks the AST and executes the program directly.

OrbitLang currently uses a tree-walk interpreter rather than compiling programs to machine code or another intermediate language.

---

# 📁 Project Structure

```text
OrbitLang/
├── orbit/
│   ├── __init__.py
│   ├── ast.py
│   ├── cli.py
│   ├── interpreter.py
│   ├── lexer.py
│   └── parser.py
├── installer/
│   └── installer.py
├── examples/
├── tests/
│   ├── test_basic.orbit
│   ├── test_break.orbit
│   ├── test_continue.orbit
│   ├── test_data_type.orbit
│   ├── test_elif.orbit
│   ├── test_for.orbit
│   ├── test_function.orbit
│   ├── test_input.orbit
│   ├── test_repeat.orbit
│   ├── test_return.orbit
│   └── test_while.orbit
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

---

# 🧪 Testing

OrbitLang includes test programs written in OrbitLang itself.

The tests are stored in the `tests/` directory and cover different language features and interpreter behavior.

### Run an individual test

```bash
orbit run tests/test_basic.orbit
```

For example:

```bash
orbit run tests/test_function.orbit
```

### Run all tests

On Linux and other Unix-like systems:

```bash
for f in tests/*.orbit; do
    echo "=== $f ==="
    orbit run "$f" || exit 1
done
```

The command stops if a test exits with an error.

### Current test suite

```text
tests/
├── test_basic.orbit
├── test_break.orbit
├── test_continue.orbit
├── test_data_type.orbit
├── test_elif.orbit
├── test_for.orbit
├── test_function.orbit
├── test_input.orbit
├── test_repeat.orbit
├── test_return.orbit
└── test_while.orbit
```

The tests currently cover:

* Basic variables and expressions
* `if / elif / else`
* `while`
* `repeat`
* `for`
* `range()`
* Functions
* `return`
* `break`
* `continue`
* Data types and typed assignments
* `input()`

The test programs are regular OrbitLang source files, so they exercise the same lexer, parser, interpreter, and CLI used by normal programs.

---

# 🛣️ Roadmap

Planned features and improvements include:

* Lists
* Dictionaries
* Imports and modules
* Standard library
* More comprehensive testing
* Multiline REPL support
* Better error diagnostics
* Improved tooling
* More language features
* Continued interpreter improvements

The roadmap may change as OrbitLang evolves.

---

# 🎯 Philosophy

OrbitLang is intentionally small.

The goal is not to create another Python replacement or a huge production language. The goal is to build a programming language from scratch and understand how its individual components work.

OrbitLang aims to be:

* Simple
* Understandable
* Consistent
* Small enough to study
* Powerful enough to build interesting programs

---

# 🤝 Contributing

Contributions, ideas, bug reports, and improvements are welcome.

If you find a bug or have an idea for OrbitLang, feel free to open an issue or submit a pull request.

---

# 📄 License

OrbitLang is released under the MIT License.

See [`LICENSE`](LICENSE) for the full license text.
