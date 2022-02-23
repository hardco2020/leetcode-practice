def backspaceCompare(s: str, t: str) -> bool:
    #build []
    
    #Time O(m+n)
    #Space O(m+n)
    def build(s):
        ans = []
        for c in s:
            if c == "#" and ans:
                ans.pop()
            elif c != "#":
                ans.append(c)
        return "".join(ans)
    #print(build(s))
    #print(build(t))
    return build(s) == build(t)
'''
def backspaceCompare(self, s: str, t: str) -> bool:
    S1 = s
    S2 = t    
    r1 = len(S1) - 1 
    r2 = len (S2) - 1
    
    while r1 >= 0 or r2 >= 0:
        char1 = char2 = ""
        if r1 >= 0:
            char1, r1 = self.getChar(S1, r1)
        if r2 >= 0:
            char2, r2 = self.getChar(S2, r2)
        if char1 != char2:
            return False
    return True
def getChar(self, s , r):
    char, count = '', 0
    # start from end
    while r >= 0 and not char:
        
        #when we have "#" count+=1
        if s[r] == '#':
            count += 1
        #when we don't have # mean f
        elif count == 0:
            char = s[r]
        else:
            count -= 1
        r -= 1
    return char, r

'''
print(backspaceCompare("ab#c","ad#c"))