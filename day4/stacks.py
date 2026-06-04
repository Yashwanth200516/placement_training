# stack=[]
# stack.append(10)
# stack.append(20)
# stack.append(30) 
# stack.append(40)
# stack.append(50)
# print("Stack:",stack)
# print("top element:",stack[-1])

# popele1=stack.pop()
# popele2=stack.pop()
# print("Stack:",stack)
# print("popped elements are:",popele1,popele2)
# print("top element:",stack[-1])

# print("is empty:",len(stack)==0)


#stack using class
class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)
    
    def is_empty(self):
        return len(self.stack)==0
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "stack is empty"
    
    def size(self):
        return len(self.stack)
    
s1=Stack()
s1.push('A')
s1.push('B')
s1.push('C')
print(s1)
print(s1.peek())
print(s1.pop())
print(s1.peek())
    