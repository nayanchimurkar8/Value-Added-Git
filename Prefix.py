def longestCommonPrefix(str: list[str]) -> str:
    if not str:
        return""
    base = str[0]
    for i in range(len(base)):
        for s in str[1:]:
            if i>= len(s) or s[i] != base[i]:
                return base[:i]

    return base