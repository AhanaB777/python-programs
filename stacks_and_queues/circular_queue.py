class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.q=[0]*size
        self.front=-1
        self.rear=-1
    
    def enqueue(self,item):
        self.rear=(self.rear+1)%self.size
        if self.front==self.rear:
            print("Queue is full")
            return
        else:
            if self.front==-1:
                self.front=0
                self.rear=0
            self.q[self.rear]=item
    
    def dequeue(self):
        if self.front==-1:
            print("Queue is empty cannot delete")
            return
        else:
            item=self.q[self.front]
            if self.rear==self.front:
                self.front=-1
                self.rear=-1
            else:
                self.front=(self.front+1)%self.size
            print(f"{item} is deleted")
    
    def disp(self):
        if self.front==-1:
            print("Queue is empty")
        else:
            i=self.front
            while True:
                print(self.q[i],end=" ")
                if i==self.rear:
                    break
                i=(i+1)%self.size   
            print()

q1=CircularQueue(5)
q1.dequeue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
q1.disp()
q1.dequeue()
q1.disp()


