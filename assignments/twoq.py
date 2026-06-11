from collections import deque
class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
    def pop(self):
        if not self.q1:
            return None
        return self.q1.popleft()
    def peek(self):
        if not self.q1:
            return None
        return self.q1[0]
stack = StackUsingQueues()
stack.push(10)
stack.push(20)
print(stack.peek())  
print(stack.pop())   
print(stack.peek())  