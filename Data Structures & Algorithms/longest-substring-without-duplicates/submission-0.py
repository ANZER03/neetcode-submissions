class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1 :
            if len(s) == 0 :
                return 0
            return 1
        
        l , r = 0 , 0

        sett = set()
        maxL = 0
        temp_max = 0
        while r < len(s) :

            if s[r] not in sett :
                sett.add(s[r])
                temp_max += 1
                r += 1

            else :

                while s[r] in sett :
                    sett.remove(s[l])
                    l += 1
                    temp_max -= 1

            maxL = max(maxL , temp_max)
        return maxL




            
