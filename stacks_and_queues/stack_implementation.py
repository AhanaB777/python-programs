class Stack:
    def __init__(self,size):
        self.size=size
        self.s=[0]*size
        self.top=-1

    def push(self,e):
        if self.top==self.size-1:
            print("Stack overflow")
            return
        else:
            self.top=self.top+1
            self.s[self.top]=e
            print(f"{e} pushed")

    def pop(self):
        if self.top==-1:
            print("Stack already empty")
            return
        else:
            e=self.s[self.top]
            self.top=self.top-1
            print(f"{e} deleted")

    def peek(self):
        item=self.s[self.top]
        return item
    
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    
    def isFull(self):
        if self.top==self.size-1:
            return True
        else:
            return False

    def disp(self):
        if self.top==-1:
            print("Stack is empty")
        else:
            print(self.s[:self.top+1])

s1=Stack(10)
s1.pop()    
s1.push(10)
s1.push(20)
s1.push(30)
s1.disp()
s1.pop()
s1.disp()