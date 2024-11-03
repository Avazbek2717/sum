def anagram(s: str, d: str):
    v = sorted(s)
    b = sorted(d)
    if v == b:
        return True
    else:
        return False
    
print(anagram('anan','nana'))