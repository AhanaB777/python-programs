class Node:
    def __init__(self,item):
        self.info=item
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
        self.start=None
    
    def push(self,item):
        nd=Node(item)
        if self.top is None:
            self.start=nd
            self.top=nd
            return
        self.top.next=nd
        self.top=nd
    
    def pop(self):
        if self.top is None:
            print("Stack Underfllow")
            return
        if self.start.next is None:
            temp=self.start
            item=self.start.info
            self.top=None
            self.start=None
            print("Popped: ", item)
            del temp
            return
        temp=self.start
        while temp.next is not None:
            prev=temp
            temp=temp.next
        prev.next=None
        self.top=prev
        print("Popped: ", temp.info)
        del temp
        #print(prev.info)
    
    def display(self):
        if self.start is None:
            print("Empty Stack")
            return
        print("Start", end=" -> ")
        temp=self.start
        while temp is not None:
            print(temp.info, end=" -> ")
            temp=temp.next
        print("None")
        print("Top: ",self.top.info)
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.display()
s1.pop()
s1.display()