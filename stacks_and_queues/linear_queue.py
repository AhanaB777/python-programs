class LinerQueue:
    def __init__(self,size):
        self.size=size
        self.q=[0]*size
        self.front=-1
        self.rear=-1

    def enqueue(self,item):
        if self.rear==self.size-1: 
            print("Queue is full, cannot insert element")
            return
        else:
            if self.front==-1:
                self.front=0
            self.rear+=1
            self.q[self.rear]=item
            print(f"{item} inserted in Queue")

    def dequeue(self):
        if self.front==-1 or self.front>self.rear:
            print("Queue is empty cannot delete any item")
            return
        else:
            item=self.q[self.front]
            self.front+=1
            print(f"{item} deleted from queue")

    def peek(self):
        item=self.q[self.front]
        print(f"Front element is {item}")

    def isFull(self):
        if self.rear==self.size-1:
            return True
        else:
            return False

    def isEmpty(self):
        if self.front==-1 or self.front>self.rear:
            return True
        else:
            return False 

    def disp(self):
        if self.front==-1 or self.front>self.rear:
            print("Cannot print empty queue")
        else:
            print(self.q[self.front:self.rear+1])

    
q1=LinerQueue(5)
print(q1.isFull())
q1.disp()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.disp()
q1.dequeue()
q1.disp()