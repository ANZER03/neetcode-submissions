class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        mem = [(i, temperatures[i]) for i in range(len(temperatures))]
        res = [0]*len(temperatures)

        for temp in mem:
            if not st :
                st.append(temp)
                continue
            
            while (st and temp[1] > st[-1][1]):
                res[st[-1][0]] = (temp[0] - st[-1][0])
                st.pop()
            
            st.append(temp)
        
        return res
