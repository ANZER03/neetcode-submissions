from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        mem = {
            "{" : "}",
            "(" : ")",
            "[" : "]",
            "}" : "{",
            ")" : "(" ,
            "]" : "[" ,

        }


        if s[0] in "})]" or s[-1] in "{([":
            return False

        for p in s :

            if stack :
                if stack[-1] == mem[p] and p in "})]":
                    stack.pop()
                    continue

            stack.append(p)
        
        return not stack
            
            

        