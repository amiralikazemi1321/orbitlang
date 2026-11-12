# OrbitLang 🪐

**Simple syntax. Small language. Built from scratch.**

OrbitLang is a small interpreted programming language implemented in Python.

It features a Python-inspired syntax while keeping the language itself small and understandable. OrbitLang includes its own lexer, parser, Abstract Syntax Tree (AST), tree-walk interpreter, command-line interface, interactive REPL, and graphical installer.

## ✨ Features

### Language

- Variables and typed assignments
- Numbers, strings, and booleans
- Lists and dictionaries
- Arithmetic, comparison, and logical operators
- Membership operator (`in`)
- User input with `input()`
- Output with `show`
- Conditional statements (`if`, `elif`, `else`)
- One-line conditions
- `while`, `for`, and `repeat` loops
- `range()`
- `break` and `continue`
- Functions with `func`
- Function parameters and `return`
- List indexing and assignment
- Dictionary key access and assignment
- Dictionary operations
- Indentation-based blocks
- Comments

### Tooling & Implementation

- Custom lexer
- Custom parser
- Abstract Syntax Tree (AST)
- Tree-walk interpreter
- Command-line interface
- Interactive REPL
- Graphical installer built with Tkinter
- Lexer, parser, and interpreter error handling
- Example programs and language-level tests

---

## 📦 Installation

Prebuilt packages are available for Windows, macOS, and Linux.

**Download the latest release:**

[OrbitLang Releases](https://github.com/amiralikazemi1321/orbitlang/releases)

### Windows

1. Download `OrbitLang-Setup-0.1.0.exe`.
2. Run the installer.
3. Follow the installation instructions.

### macOS

1. Download `OrbitLang-0.1.0.dmg`.
2. Open the DMG file.
3. Copy or use the included `orbit` executable.

The macOS package currently provides a command-line executable, not a graphical application.

### Linux

1. Download `OrbitLang-0.1.0-x86_64.AppImage`.
2. Open a terminal in the download directory.
3. Make the file executable:

```bash
chmod +x OrbitLang-0.1.0-x86_64.AppImage
```

4. Run OrbitLang:

```bash
./OrbitLang-0.1.0-x86_64.AppImage version
```

To execute a program:

```bash
./OrbitLang-0.1.0-x86_64.AppImage run program.orbit
```

The Linux package currently targets x86_64 systems.

---

## 🐍 Installation from Source

You can also install OrbitLang directly from its source code.

### Requirements

- Python 3.10 or newer
- pip
- A terminal

Clone the repository:

```bash
git clone https://github.com/amiralikazemi1321/orbitlang.git
cd orbitlang
```

Install OrbitLang:

```bash
pip install .
```

After installation, the `orbit` command will be available in your terminal.

---

## 🚀 Quick Start

Create a file with the `.orbit` extension:

```orbit
show "Hello, OrbitLang!"
```

Save it as `hello.orbit`.

Run it:

```bash
orbit run hello.orbit
```

Output:

```text
Hello, OrbitLang!
```

---

## 💻 REPL

OrbitLang provides an interactive Read-Eval-Print Loop:

```bash
orbit repl
```

Example:

```text
OrbitLang REPL
Type 'exit' or 'quit' to quit.
>>> show "Hello"
Hello
>>> show 10 + 5
15
>>> exit
```

The current REPL is designed for single-line interaction. Multiline interactive blocks are planned for a future version.

---

## 📖 Language Syntax

### Variables

Variables can be created with a simple assignment:

```orbit
name = "Alex"
age = 25

show name
show age
```

### Data Types

OrbitLang supports:

- Numbers
- Strings
- Booleans
- Lists
- Dictionaries

```orbit
age = 25
name = "Alex"
active = true

numbers = [10, 20, 30]

person = {
    "name": "Alex",
    "age": 25
}
```

### Typed Assignments

Variables can optionally specify their type:

```orbit
number age = 25
string name = "Alex"
boolean active = true
```

The interpreter checks that the assigned value matches the declared type.

### Output

Use `show` to print a value:

```orbit
show "Hello"
show 10
show 5 + 3
```

### Input

Use `input()` to read user input:

```orbit
name = input("What is your name? ")

show name
```

### Arithmetic

OrbitLang supports common arithmetic operators:

```orbit
x = 10
y = 5

show x + y
show x - y
show x * y
show x / y
```

### Comparisons

```orbit
x = 10

show x == 10
show x != 5
show x > 5
show x < 20
show x >= 10
show x <= 10
```

### Conditions

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

### `elif` and `else`

```orbit
x = 15

if x > 20:
    show "big"
elif x > 10:
    show "medium"
else:
    show "small"
```

One-line form:

```orbit
if x > 20: show "big"
elif x > 10: show "medium"
else: show "small"
```

### Logical Operators

OrbitLang supports:

- `and`
- `or`
- `not`

Example:

```orbit
age = 15

if age > 10 and age < 18:
    show "teenager"
```

### `while` Loops

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

### `repeat` Loops

`repeat` executes a block a specified number of times:

```orbit
repeat 5:
    show "Hello"
```

One-line form:

```orbit
repeat 3: show "Orbit"
```

### `for` Loops

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

#### `range()`

`range()` supports one, two, or three integer arguments:

```orbit
range(5)
range(2, 5)
range(0, 10, 2)
```

### `break` and `continue`

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

### Functions

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

### `return`

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

### Lists

Lists store multiple values in a single variable.

Create a list using square brackets:

```orbit
numbers = [10, 20, 30]

show numbers
```

#### List Indexing

Individual elements can be accessed using their index:

```orbit
show numbers[0]
show numbers[1]
show numbers[2]
```

List indexing starts at `0`.

#### List Assignment

List elements can be updated using indexed assignment:

```orbit
numbers = [10, 20, 30]

numbers[1] = 50

show numbers
```

Output:

```text
[10, 50, 30]
```

### Dictionaries

Dictionaries store data as key-value pairs.

Create a dictionary using curly braces:

```orbit
person = {
    "name": "Alex",
    "age": 25,
    "city": "London"
}

show person
```

#### Dictionary Access

Access a value using its key:

```orbit
show person["name"]
show person["age"]
```

#### Dictionary Assignment

Dictionary values can be updated, and new keys can be added:

```orbit
person["age"] = 26
person["active"] = true

show person
```

#### Empty Dictionaries

```orbit
data = {}

show data
```

#### Dictionary Operations

OrbitLang provides several built-in functions for working with dictionaries.

**`keys()`**

Returns a list containing the dictionary's keys:

```orbit
show keys(person)
```

**`values()`**

Returns a list containing the dictionary's values:

```orbit
show values(person)
```

**`remove()`**

Removes a key from a dictionary and returns its associated value:

```orbit
removed = remove(person, "age")

show removed
show person
```

**`clear()`**

Removes all entries from a dictionary:

```orbit
clear(person)

show person
```

**`merge()`**

Combines two dictionaries and returns a new dictionary.

If both dictionaries contain the same key, the value from the second dictionary takes priority. The original dictionaries remain unchanged.

```orbit
first = {
    "name": "Alex",
    "age": 25
}

second = {
    "age": 26,
    "city": "London"
}

combined = merge(first, second)

show combined
```

### Membership Operator

OrbitLang supports the `in` operator for checking whether a value exists in a collection.

It works with lists, dictionaries, and strings.

**Lists**

```orbit
numbers = [10, 20, 30]

show 20 in numbers
show 50 in numbers
```

**Dictionaries**

For dictionaries, `in` checks whether a key exists:

```orbit
person = {
    "name": "Alex",
    "age": 25
}

show "name" in person
show "city" in person
```

**Strings**

For strings, `in` checks whether a substring exists:

```orbit
message = "Hello, OrbitLang!"

show "OrbitLang" in message
show "Python" in message
```

---

## 🧰 Built-in Functions

| Function | Description |
|---|---|
| `input()` | Reads user input |
| `type()` | Returns the type of a value |
| `range()` | Creates a range of numbers |
| `int()` | Converts a value to an integer |
| `len()` | Returns the length of a supported value |
| `keys()` | Returns dictionary keys |
| `values()` | Returns dictionary values |
| `remove()` | Removes a dictionary entry and returns its value |
| `clear()` | Removes all entries from a dictionary |
| `merge()` | Merges two dictionaries into a new dictionary |

### `type()`

Returns the type of a value:

```orbit
show type(10)
show type("Hello")
show type(true)
show type([1, 2, 3])
show type({"name": "Alex"})
```

### `len()`

Returns the length of a supported value:

```orbit
show len("OrbitLang")
show len([10, 20, 30])
show len({"name": "Alex", "age": 25})
```

---

## 💬 Comments

Comments start with `#`:

```orbit
# This is a comment

x = 10  # This is also a comment
```

---

## 🧠 How OrbitLang Works

OrbitLang follows a traditional interpreter pipeline:

```text
OrbitLang source code
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

The lexer reads source code and converts it into tokens.

It handles:

- Keywords
- Identifiers
- Numbers
- Strings
- Operators
- Indentation
- New lines
- Comments

### Parser

The parser takes the tokens produced by the lexer and builds an Abstract Syntax Tree.

It is responsible for understanding OrbitLang's grammar and structure.

### AST

The AST represents the structure of a program using Python objects such as:

- `Number`
- `String`
- `Boolean`
- `Variable`
- `BinaryOp`
- `UnaryOp`
- `Assign`
- `Show`
- `If`
- `While`
- `For`
- `FunctionDef`
- `Return`
- `Call`
- `ListLiteral`
- `Index`
- `IndexAssign`
- `Dictionary`

### Interpreter

The interpreter walks the AST and executes the program directly.

OrbitLang currently uses a tree-walk interpreter rather than compiling programs to machine code or another intermediate language.

---

## 📁 Project Structure

```text
orbitlang/
├── .github/
│   └── workflows/
│       └── build.yml
├── examples/
│   └── program.orbit
├── installer/
│   ├── installer.py
│   └── windows.iss
├── orbit/
│   ├── __init__.py
│   ├── ast.py
│   ├── cli.py
│   ├── interpreter.py
│   ├── lexer.py
│   └── parser.py
├── tests/
│   ├── test_basic.orbit
│   ├── test_bool.orbit
│   ├── test_break.orbit
│   ├── test_continue.orbit
│   ├── test_data_type.orbit
│   ├── test_dictionary.orbit
│   ├── test_elif.orbit
│   ├── test_for.orbit
│   ├── test_function.orbit
│   ├── test_index_assignment.orbit
│   ├── test_input.orbit
│   ├── test_list.orbit
│   ├── test_repeat.orbit
│   ├── test_return.orbit
│   └── test_while.orbit
├── .gitignore
├── LICENSE
├── orbit.spec
├── pyproject.toml
└── README.md
```

---

## 🧪 Testing

OrbitLang includes test programs written in OrbitLang itself.

The tests are stored in the `tests/` directory and cover different language features and interpreter behavior.

### Run an Individual Test

```bash
orbit run tests/test_basic.orbit
```

For example:

```bash
orbit run tests/test_dictionary.orbit
```

### Run All Tests

On Linux and other Unix-like systems:

```bash
for f in tests/*.orbit; do
    echo "=== $f ==="
    orbit run "$f" || exit 1
done
```

The command stops if a test exits with an error.

The test programs exercise the same lexer, parser, interpreter, and CLI used by normal programs.

---

## 🛣️ Roadmap

Planned features and improvements include:

- Imports and modules
- Expanded standard library
- More comprehensive testing
- Multiline REPL support
- Better error diagnostics
- Improved tooling
- More language features
- Continued interpreter improvements

The roadmap may change as OrbitLang evolves.

---

## 🎯 Philosophy

OrbitLang is intentionally small.

The goal is not to create another Python replacement or a huge production language. The goal is to build a programming language from scratch and understand how its individual components work.

OrbitLang aims to be:

- Simple
- Understandable
- Consistent
- Small enough to study
- Powerful enough to build interesting programs

---

## 🤝 Contributing

Contributions, ideas, bug reports, and improvements are welcome.

If you find a bug or have an idea for OrbitLang, feel free to open an issue or submit a pull request.

---

## 📄 Project Information

| Property | Value |
|---|---|
| Name | OrbitLang |
| Version | 0.1.0 |
| Description | A simple programming language made in Python |
| Implementation | Python |
| License | MIT |

The command-line entry point is configured as:

```toml
[project.scripts]
orbit = "orbit.cli:main"
```

This makes the `orbit` command available after installing the package.

---

## 📜 License

OrbitLang is released under the MIT License.

See [`LICENSE`](LICENSE) for the full license text.
