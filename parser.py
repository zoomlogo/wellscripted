class ASTNode:
    def __init__(self, value, typ, children):
        self.value = value
        self.type = typ
        self.children = children

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

if __name__ == "__main__":
    n = ASTNode(0,0,[
        ASTNode(1,0,[ASTNode(3,1,[
            ASTNode(5,2,[]),
            ASTNode(6,2,[ASTNode(69,0,[])]),
        ])]),
        ASTNode(2,0,[ASTNode(4,1,[])])
    ])
    print(n)
