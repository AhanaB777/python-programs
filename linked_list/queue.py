class Node:
    def __init__(self, item):
        self.info = item
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size=0

    def enqueue(self, item):
        nd = Node(item) 
        if self.front is None:
            self.front = self.rear = nd
            self.size += 1
            return
        self.rear.next = nd
        self.rear = nd
        self.size += 1

    def dequeue(self):
        if self.front is None:
            print("Empty Queue")
            return
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print("Removed item:", temp.info)
        del temp
        self.size -= 1
    
    def getSize(self):
        return self.size

    def getFront(self):
        if self.front is None:
            return None
        return self.front.info
    
    def getRear(self):
        if self.rear is None:
            return None
        return self.rear.info
    
    def isEmpty(self):
        return self.front is None #Returns true/false

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return
        print("Start",end=" -> ")
        temp = self.front
        while temp is not None:
            print(temp.info, end=" -> ")
            temp = temp.next
        print("None")

q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.display()
print("Size of queue : ", q1.getSize())
print("Front: ", q1.getFront())
print("Rear : ", q1.getRear())
# q1.dequeue()
# q1.display()