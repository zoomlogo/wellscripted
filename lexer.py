from enum import Enum, auto
import string

KEYWORDS = ["val", "var", "type", "while", "return"]
COMPOUND_OPERATORS = ["->", "+=", "-=", "*=", "/="]

class LexType(Enum):
    NUMBER = auto()
    STRING = auto()
    OPERATOR = auto()
    KEYWORD = auto()
    IDENTIFIER = auto()

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

        elif head in string.punctuation:  # operators
            if head in map(lambda x: x[0], COMPOUND_OPERATORS):
                op = head
                if i >= len(code):
                    res.append(LexToken(LexType.OPERATOR, op))
                else:
                    i += 1
                    if code[i] in string.punctuation:
                        op += code[i]
                    else:
                        i -= 1
                    for j in COMPOUND_OPERATORS:
                        if j == op:
                            res.append(LexToken(LexType.OPERATOR, op))
                            break
                    else:
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
