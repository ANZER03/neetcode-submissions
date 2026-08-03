class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sett = set(nums)
        mem = set()
        max_res = 0

        for x in nums : 

            if x - 1 in sett :
                continue
            
            if x in mem :
                continue
            
            temp_max = 1
            temp_incremt = x + 1
            while (temp_incremt in sett) :
                temp_max += 1
                temp_incremt += 1
            
            max_res = max (max_res, temp_max)

            mem.add(x)
        
        return max_res
            

