class MinStack:

    def __init__(self):
        self.head = None

    def push(self, value: int) -> None:
        if (self.head is None):
            self.head = Node(value, value , None)
        else :
            self.head = Node(value, min(value, self.head.min) , self.head)


    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.value

    def getMin(self) -> int:
        return self.head.min

class Node: 
    
    def __init__(self, x: int , minn : int , nextt: Node) :
        self.value = x
        self.next = nextt
        self.min = minn


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()