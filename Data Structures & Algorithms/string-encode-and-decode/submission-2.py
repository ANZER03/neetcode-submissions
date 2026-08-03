class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        temp = []
        if len(strs) == 0 :
            return temp
        for x in strs:
            temp.append(str(len(x)).zfill(4))
            temp.append(x)
        return res.join(temp)


    def decode(self, s: str) -> List[str]:
        res = []

        if len(s) == 0 :
            return res.append("")

        i = 0
        while (i < len(s)) :
            # prefix_start = i + 
            prefix = int(s[i:i+4])
            indx = i + 4
            res.append(s[indx : indx+prefix])
            i += prefix + 4
        
        return res