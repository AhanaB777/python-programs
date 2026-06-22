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

    def insert_at_end(self,item):
        nd=Node(item)

        if self.start is None:
            self.start=nd
            return
  
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=nd

    def insert_at_specific_pos(self,item,pos):
        nd=Node(item)
        if pos==1:
            self.insert_at_beginning(item)
        else:
            i=1
            temp=self.start
            while temp.next is not None and i!=pos:
                prev=temp
                temp=temp.next
                i+=1
            if temp.next is None:
                temp.next=nd
            nd.next=temp
            prev.next=nd

    def insert_after_specific_item(self,item,spec_it):
        nd=Node(item)
        temp=self.start
        while temp.next is not None and temp.info!=spec_it:
            temp=temp.next
        nd.next=temp.next
        temp.next=nd

    def delete_start(self):
        if self.start is None:
            print("Empty linked list cannot delete first node")
            return
        
        temp=self.start
        self.start=temp.next
        del temp

    def delete_last_node(self):
        if self.start is None:
            print("Empty linked list cannot delete last node")
            return
        
        if self.start.next is None:
            temp=self.start
            self.start=None
            del temp
            print("Single Node deleted")
            return
        
        temp=self.start
        while temp.next is not None:
            prev=temp
            temp=temp.next
        prev.next=None
        del temp

    def delete_specific_pos(self,pos):
        if pos<=0:
            print("Invalid position")
            return
        
        if self.start is None:
            print("Empty Linked list cannot delete position ",pos)
            return
        
        if pos == 1:
            self.delete_start()
            return

        temp=self.start
        i=1
        while temp is not None and i!=pos:
            prev=temp
            temp=temp.next
            i+=1
        
        if temp is None:
            print("Position doesn't exist")
            return

        prev.next=temp.next
        del temp

    def delete_specific_item(self,spec_it):
        if self.start is None:
            print("Empty Linked List")
            return
        
        if self.start.info==spec_it:
            self.delete_start()
            return
        
        temp=self.start
        while temp is not None and temp.info!=spec_it:
            prev=temp
            temp=temp.next

        if temp is None:
            print("Cannot find specific item")
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

ll=LinkedList()
# ll.display()
ll.insert_at_beginning(40)
ll.insert_at_beginning(30)
ll.insert_at_beginning(20)
ll.insert_at_end(50)
ll.insert_at_specific_pos(25,3)
ll.insert_after_specific_item(35,30)
# ll.delete_start()
# ll.delete_last_node()
# ll.delete_specific_pos(10)
# ll.delete_specific_item(40)
ll.display()
