class Node:
    def __init__(self,item):
        self.info=item
        self.next=None

class LinkedList:
    def __init__(self):
        self.start=None

    def insert_at_beginning(self,item):
        nd=Node(item)
        nd.next=self.start
        self.start=nd

    def insert_at_position(self,item,pos):
        nd=Node(item)
        if pos==1:
            nd.next=self.start
            self.start=nd
            return
        if self.start is None:
            print("Empty linked list cannot find position")
            return
        temp=self.start
        i=1
        while i<pos-1 and temp.next is not None:
            temp=temp.next
            i+=1
        if temp.next is None:
            print("Couldnt find position")
            return
        nd.next=temp.next
        temp.next=nd

    def insert_after_it(self,item,spec_it):
        nd=Node(item)
        if self.start is None:
            print("empty linked list couldn't find item")
            return
        temp=self.start
        while temp.info!=spec_it and temp.next is not None:
            temp=temp.next
        if temp.next is None:
            print("Couldnt find item")
            return
        nd.next=temp.next
        temp.next=nd

    def delete_pos(self,pos):
        if self.start is None:
            print("Empty")
            return
        temp=self.start
        i=1
        prev=None
        while i<pos and temp is not None:
            prev=temp
            temp=temp.next
            i+=1

        if temp is None:
            print("Pos doesnt exist")
            return
        prev.next=temp.next
        del temp

    def spec_it(self,spec_it):
        temp=self.start
        while temp.info!=spec_it and temp is not None:
            prev=temp
            temp=temp.next
        if temp is None:
            print("no")
            return
        
        prev.next=temp.next
        del temp




    def display(self):
        if self.start is None:
            print("Linked list is empty")
        else:
            temp=self.start
            while temp is not None:
                print(temp.info, end = " -> ")
                temp=temp.next
            print("None")

a1=LinkedList()
a1.insert_at_beginning(50)
a1.insert_at_beginning(40)
a1.insert_at_beginning(30)
a1.insert_at_beginning(20)
a1.insert_at_beginning(10)
a1.insert_at_position(25,3)
a1.insert_after_it(45,40)
a1.delete_pos(1)
a1.display()