class Node:
    def __init__(self,item):
        self.info=item
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
        self.size=0

    def push(self,item):
        nd=Node(item)
        nd.next=self.top
        self.top=nd
        self.size+=1

    def pop(self):
        if self.top is None:
            print("Empty Stack")
            return
        temp = self.top
        self.top = self.top.next
        print("Popped:",temp.info)
        del temp
        self.size-=1

    def getSize(self):
        return self.size

    def peek(self):
        if self.top is None:
            return None
        return self.top.info
    
    def isEmpty(self):
        return self.top is None

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return
        
        temp = self.top
        while temp is not None:
            print(temp.info, end=" -> ")
            temp = temp.next
        print("None")

s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.display()
print("Top element: ", s1.peek())
print("Size of Stack : ",s1.getSize())


print("Performing Pop operation")
s1.pop()
print("Top element: ", s1.peek())
print("Size of Stack : ",s1.getSize())
s1.display()