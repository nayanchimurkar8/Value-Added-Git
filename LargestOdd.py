def largestOddNumber(s: str) -> str:
    for i in range(len(s)-1,-1,-1):
        if s[i] in {'1','3','5','7','9'}:
            return int(s[:i +1].lstrip('0'))

    return ""
