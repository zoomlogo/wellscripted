from enum import Enum, auto
from lexer import *

class ASTType(Enum):
    PROGRAM = auto()
    EXPRESSION = auto()
    EXPR = auto()
    UNARY = auto()
    BINARY = auto()
    KEYWORD = auto()
    IDENTIFIER = auto()
    CONSTANT = auto()

class ASTNode:
    def __init__(self, value, typ, children=[]):
        self.value = value
        self.type = typ
        self.children = children

    def add(self, child):
        # append child
        if type(child) != ASTNode:
            raise ValueError(f"Expected ASTNode, found {type(child)}.")
        self.children.append(child)

    def extend(self, children):
        # extend with children
        for child in children:
            self.add(child)

    def pop(self):
        # pop the most recent added child
        return self.children.pop()

    def top(self):
        # refer to the most recent child
        return self.children[-1]

    def __repr__(self, level=0):
        s = f"ASTNode({self.value or 'Nil'}, {self.type})\n"
        for child in self.children:
            s += " " * level + "- " + child.__repr__(level + 1)
        return s

def number(s):
    if "." in s:
        return float(s)
    else:
        return int(s)

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
        token = tokens[i]
        if token.type == LexType.STRING:
            root.add(ASTNode(token.value, ASTType.CONSTANT))
        elif token.type == LexType.NUMBER:
            root.add(ASTNode(number(token.value), ASTType.CONSTANT))
        elif token.type == LexType.KEYWORD:
            root.add(ASTNode(token.value, ASTType.KEYWORD))
        elif token.type == LexType.IDENTIFIER:
            root.add(ASTNode(token.value, ASTType.IDENTIFIER))
        i += 1

    return root

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
    root = parse(tokens)
    print(root)
