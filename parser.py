def match_brackets(x, i=0, parens="()"):
    k = 0
    while i < len(x):
        if x[i] == parens[0]: k += 1
        if x[i] == parens[1]: k -= 1
        if k == 0: return i
        i += 1
    return -1  # error
