class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower().replace(" ", "")
        # alph = set([chr(i) for i in range(ord('a') , ord('z') + 1)])

        # for ch in s :
        #     if ch not in alph :
        #         s = s.replace(ch, "")

        s = "".join([c.lower() for c in s if c.isalnum()])
        
        # s = s.lower().replace(" ", "")

        print(s)

        l , r = 0 , len(s) - 1

        while l <= r :
            if s[l] != s[r] : 
                return False
            l += 1
            r -= 1
        
        return True



