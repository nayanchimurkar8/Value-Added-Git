def isIsomorphic(s: str, t: str) -> bool:
    if len(s)!= len(t):
        return False
    return len(set(zip(s,t))) ==len(set(s))==len(set(t))
 