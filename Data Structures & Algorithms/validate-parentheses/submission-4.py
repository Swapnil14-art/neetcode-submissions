class Solution:
    def isValid(self, s: str) -> bool:
        stck=[]
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stck.append(s[i])
            elif s[i] == ')':
                if stck and stck[-1] == '(':
                    stck.pop()
                else:
                    return False
            elif s[i] == ']':
                if stck and stck[-1] == '[':
                    stck.pop()
                else:
                    return False
            elif s[i] == '}':
                if stck and stck[-1] == '{':
                    stck.pop()
                else:
                    return False
        return stck == []