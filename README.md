# OrbitLang 🪐

OrbitLang is a small interpreted programming language written in Python.

It features Python-inspired syntax and its own lexer, parser, Abstract Syntax Tree (AST), and tree-walk interpreter. The project also includes a command-line interface, an interactive REPL, and a graphical installer built with Tkinter.

OrbitLang is an ongoing project focused on building a programming language from scratch and exploring how interpreters work.

## ✨ Features

### Language Features

- Variables and assignments
- Numbers, strings, and booleans
- Typed variable declarations
- Lists
- List and string indexing
- List element assignment
- User input with `input()`
- Integer conversion with `int()`
- Output with `show`
- Arithmetic operators
- Comparison operators
- Logical operators: `and`, `or`, `not`
- Conditional statements: `if`, `elif`, `else`
- One-line conditions
- `while` loops
- `repeat` loops
- `for` loops
- `range()`
- `break` and `continue`
- User-defined functions with `func`
- Function parameters and `return`
- Indentation-based blocks
- Comments

### Tooling

- Command-line interface
- Interactive REPL
- Graphical installer built with Tkinter
- Lexer, parser, and interpreter error handling
- Example programs
- Language-level test programs

## 🚀 Installation

### Requirements

- Python 3.10 or newer

Clone the repository:

```bash
git clone https://github.com/amiralikazemi1321/orbitlang.git
cd orbitlang
```

Install OrbitLang:

```bash
pip install .
```

## ▶️ Quick Start

Create a file named `hello.orbit`:

```orbit
name = "OrbitLang"

show "Hello, " + name + "!"
```

Run it:

```bash
orbit run hello.orbit
```

Expected output:

```text
Hello, OrbitLang!
```

## 💻 REPL

Start the interactive REPL:

```bash
orbit repl
```

You can enter and execute OrbitLang statements interactively.

Multiline REPL support is planned for a future version.

## 📦 Graphical Installer

OrbitLang includes a graphical installer implemented with Tkinter.

Run it from the repository root:

```bash
python installer/installer.py
```

On Fedora, install Tkinter if it is not already available:

```bash
sudo dnf install python3-tkinter
```

The installer is intended to simplify the installation process through a graphical interface.

## 📖 Language Syntax

### Variables

```orbit
name = "OrbitLang"
age = 13

show name
show age
```

### Typed Assignments

```orbit
number age = 13
string name = "OrbitLang"
boolean active = true
```

### Input

```orbit
name = input("What is your name? ")

show name
```

### Integer Conversion

`input()` returns text. Use `int()` to convert numeric input into an integer.

```orbit
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

show first + second
```

### Arithmetic

```orbit
x = 10
y = 5

show x + y
show x - y
show x * y
show x / y
```

### Conditions

```orbit
x = 10

if x > 5:
    show "x is greater than 5"
elif x == 5:
    show "x equals 5"
else:
    show "x is less than 5"
```

One-line conditions are also supported:

```orbit
if x > 5: show "Greater than 5"
```

### Logical Operators

OrbitLang supports `and`, `or`, and `not`.

```orbit
age = 13

if age > 10 and age < 18:
    show "Condition matched"
```

### While Loops

```orbit
i = 0

while i < 5:
    show i
    i = i + 1
```

### Repeat Loops

```orbit
repeat 3:
    show "OrbitLang"
```

### For Loops

```orbit
for i in range(5):
    show i
```

`range()` supports one, two, or three arguments.

```orbit
range(5)
range(2, 8)
range(0, 10, 2)
```

### Break and Continue

`break` exits the current loop.

```orbit
for i in range(10):
    if i == 5:
        break

    show i
```

`continue` skips the remaining statements in the current iteration.

```orbit
for i in range(5):
    if i == 2:
        continue

    show i
```

### Functions

Functions are declared with `func`.

```orbit
func add(a, b):
    return a + b

result = add(10, 5)
show result
```

Output:

```text
15
```

### Lists and Indexing

Lists can store multiple values:

```orbit
numbers = [10, 20, 30]

show numbers[0]
show numbers[1]
show numbers[2]
```

List indexing starts at zero.

Existing list elements can be reassigned:

```orbit
numbers = [10, 20, 30]

numbers[1] = 99

show numbers[1]
```

Output:

```text
99
```

String indexing is also supported.

### Comments

Use `#` to write comments:

```orbit
# This is a comment
show "Hello"
```

## 🧠 How It Works

OrbitLang uses a lexer, parser, AST, and tree-walk interpreter.

```text
Source Code
    |
    v
   Lexer
    |
    v
   Tokens
    |
    v
   Parser
    |
    v
    AST
    |
    v
 Interpreter
    |
    v
   Output
```

### Lexer

Reads source code and converts it into tokens.

### Parser

Processes tokens according to the language grammar and constructs an Abstract Syntax Tree.

### Abstract Syntax Tree

Represents the structure of the program using AST nodes.

### Interpreter

Walks the AST and executes the program.

OrbitLang is interpreted directly rather than compiled to machine code.

## 📁 Project Structure

```text
orbitlang/
├── examples/
│   └── program.orbit
├── installer/
│   └── installer.py
├── orbit/
│   ├── ast.py
│   ├── cli.py
│   ├── __init__.py
│   ├── interpreter.py
│   ├── lexer.py
│   └── parser.py
├── tests/
│   ├── test_basic.orbit
│   ├── test_break.orbit
│   ├── test_continue.orbit
│   ├── test_data_type.orbit
│   ├── test_elif.orbit
│   ├── test_for.orbit
│   ├── test_function.orbit
│   ├── test_index_assignment.orbit
│   ├── test_input.orbit
│   ├── test_list.orbit
│   ├── test_repeat.orbit
│   ├── test_return.orbit
│   └── test_while.orbit
├── LICENSE
├── main.py
├── pyproject.toml
└── README.md
```

## 🧪 Testing

OrbitLang includes programs written in OrbitLang to test language features.

Run an individual test:

```bash
orbit run tests/test_basic.orbit
```

Run all test programs on Linux:

```bash
for f in tests/*.orbit; do
    echo "=== $f ==="
    orbit run "$f" || exit 1
done
```

The test suite covers basic expressions, data types, control flow, loops, functions, input, lists, and indexed assignment.

This command stops when a program exits with a non-zero status. It does not automatically compare output against expected results.

## 🛣️ Roadmap

Planned improvements include:

- Dictionaries
- Imports and modules
- A standard library
- Multiline REPL support
- More comprehensive automated testing
- Improved error diagnostics
- Additional developer tooling

## 🎯 Philosophy

OrbitLang is a small project built to explore programming language implementation.

Its goal is to make the process of building an interpreter understandable while gradually developing a useful language of its own.

## 🤝 Contributing

Suggestions, bug reports, and contributions are welcome.

Feel free to open an issue or submit a pull request.

## 📄 License

OrbitLang is licensed under the MIT License. See [`LICENSE`](LICENSE) for details.
