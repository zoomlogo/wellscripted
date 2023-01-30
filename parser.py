from enum import Enum, auto
from lexer import *

class ASTType(Enum):
    PROGRAM = auto()
    EXPRESSION = auto()
    EXPR = auto()
    UNARY = auto()
    BINARY = auto()
    IDENTIFIER = auto()

class ASTNode:
    def __init__(self, value, typ, children):
        self.value = value
        self.type = typ
        self.children = children

    def add(self, child):
        # append child
        self.children.append(child)

    def extend(self, children):
        # extend with children
        self.children.extend(children)

    def __repr__(self, level=0):
        s = f"ASTNode(\"{self.value}\",{self.type})\n"
        for child in self.children:
            s += " " * level + "- " + child.__repr__(level + 1)
        return s

def match_brackets(x, i=0, parens="()"):
    k = 0
    while i < len(x):
        if x[i] == parens[0]: k += 1
        if x[i] == parens[1]: k -= 1
        if k == 0: return i
        i += 1
    return -1  # error

def parse(tokens):
    root = ASTNode("", ASTType.PROGRAM, [])

    i = 0
    while i < len(tokens):
        l.append(tokens[i])

if __name__ == "__main__":
    test_string = """val collatz = (n) -> {
    var ar = [];
    while (n > 1) ar = ar.tack(n =
        n % 2 ?
        1 + 3 * n :
        n / 2
    ); return ar;
}
    """
    print(test_string)
    tokens = lex(test_string)
