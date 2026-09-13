from dataclasses import dataclass


@dataclass
class Number:
    value: int


@dataclass
class String:
    value: str


@dataclass
class Boolean:
    value: bool


@dataclass
class Variable:
    name: str


@dataclass
class BinaryOp:
    left: object
    operator: str
    right: object


@dataclass
class UnaryOp:
    operator: str
    operand: object


@dataclass
class Assign:
    name: str
    value: object


@dataclass
class Show:
    value: object


@dataclass
class If:
    condition: object
    body: list
    elif_branches: list | None = None
    else_body: list | None = None


@dataclass
class While:
    condition: object
    body: list


@dataclass
class Program:
    statements: list

@dataclass
class Repeat:
    count: object
    body: list

@dataclass
class For:
    variable: str
    iterable: object
    body: list
    
@dataclass
class FunctionDef:
    name: str
    parameters: list
    body: list

@dataclass
class Return:
    value: object | None
    
@dataclass
class Break:
    pass

@dataclass
class Continue:
    pass

@dataclass
class Input:
    prompt: object

@dataclass
class TypeOf:
    value: object

@dataclass
class Call:
    name: str
    arguments: list

@dataclass
class TypedAssign:
    type_name: str
    name: str
    value: object

