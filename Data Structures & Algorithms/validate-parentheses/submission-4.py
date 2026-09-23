class Solution:
    def isValid(self, s: str) -> bool:
        t = []
        for i in s:
            if i in ['(', '[', '{']:
                t.append(i)
            elif len(t) > 0:
                last_pop = t.pop()
                if i == ']' and last_pop != '[':
                    return False
                elif i == ')' and last_pop != '(':
                    return False
                elif i == '}' and last_pop != '{':
                    return False
            else:
                return False
        if len(t) == 0:
            return True
        else:
            return False
            
