from enum import Enum, auto
import string

KEYWORDS = ["val", "var", "type", "while", "return"]
COMPOUND_OPERATORS = [
    "->",
    "+=",
    "-=",
    "*=",
    "/=",
    "%=",
    "&=",
    "|=",
    "^=",
    "**",
    "!=",
    "<=",
    ">=",
]
BRACKETS = ["{","}","[","]","(",")"]

class LexType(Enum):
    NUMBER = auto()
    STRING = auto()
    OPERATOR = auto()
    KEYWORD = auto()
    IDENTIFIER = auto()
    BRACKET = auto()

class LexToken:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __repr__(self):
        return f"LexToken(\"{self.value}\",{self.type})"

def lex(code):
    res = []

    i = 0
    while i < len(code):
        head = code[i]

        if head in string.ascii_letters + "_":  # identifiers and keywords
            contents = ""
            while i < len(code) and code[i] in string.ascii_letters + string.digits + "_":
                contents += code[i]
                i += 1
            i -= 1
            if contents in KEYWORDS:
                res.append(LexToken(LexType.KEYWORD, contents))
            else:
                res.append(LexToken(LexType.IDENTIFIER, contents))

        elif head in string.digits:  # numbers
            contents = ""
            while i < len(code) and code[i] in string.digits + ".e_":
                contents += code[i]
                i += 1
            i -= 1
            res.append(LexToken(LexType.NUMBER, contents))

        elif head == '"':  # string
            contents = "\""
            i += 1
            while i < len(code) and code[i] != '"':
                if code[i] == "\\":
                    contents += code[i]
                    i += 1
                contents += code[i]
                i += 1
            contents += code[i]
            contents = contents.replace("\\n", "\n").replace("\\t", "\t")
            res.append(LexToken(LexType.STRING, contents))

        elif head in BRACKETS:  # brackets
            res.append(LexToken(LexType.BRACKET,head))

        elif head in string.punctuation:  # operators
            op = head
            if i >= len(code): pass                
            elif code[i+1] in string.punctuation and code[i+1] not in BRACKETS:
                op += code[i+1]
                if op in COMPOUND_OPERATORS:
                    i += 1
                else:
                    op = op[0]
            res.append(LexToken(LexType.OPERATOR, op))

        i += 1
    return res

if __name__ == "__main__":
    test_string = """val collatz = (n: Integer) -> {
    var ar = [];
    while (n > 1) ar = ar.tack(n =
        n % 2 ?
        1 + 3 * n :
        n / 2
    ); return ar;
}
    """
    print(test_string)
    print(*lex(test_string), sep="\n")
