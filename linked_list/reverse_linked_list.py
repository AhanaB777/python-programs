class Node:
    def __init__(self,item):
        self.info=item
        self.next=None

class ReverseLinkedList:
    def __init__(self):
        self.start=None
    
    def insert_at_beginning(self,item):
        nd=Node(item)
        nd.next=self.start
        self.start=nd

    def reverse(self):
        if self.start is None:
            print("Empty linked list cannot reverse")
            return
        temp=self.start
        prev=None
        while temp is not None:
            var=temp.next
            temp.next=prev
            prev=temp
            temp=var
        self.start=prev


    def display(self):
        if self.start is None:
            print("Linked list is empty")
        else:
            print("Start",end=" -> ")
            temp=self.start
            while temp is not None:
                print(temp.info, end = " -> ")
                temp=temp.next
            print("None")

r1=ReverseLinkedList()
r1.insert_at_beginning(50)
r1.insert_at_beginning(40)
r1.insert_at_beginning(30)
r1.insert_at_beginning(20)
r1.insert_at_beginning(10)
r1.display()
r1.reverse()
r1.display()
