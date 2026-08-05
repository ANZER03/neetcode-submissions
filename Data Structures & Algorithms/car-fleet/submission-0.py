class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
            stack = []
            
            for po, sp in sorted(zip(position, speed))[::-1] :
                time = ( target - po ) / sp

                if len(stack) == 0 :
                    stack.append(time)
                elif time > stack[-1] :
                    stack.append(time)
            return len(stack)
            
            