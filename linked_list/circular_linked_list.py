class Node:
    def __init__(self,item):
        self.info=item
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.start=None

    def insert_at_beg(self,item):
        nd=Node(item)

        if self.start is None:
            nd.next=nd
            self.start=nd
            return
        
        temp=self.start
        while temp.next!=self.start:
            temp=temp.next
        nd.next=self.start
        temp.next=nd
        self.start=nd
        

    def insert_at_end(self,item):
        nd=Node(item)

        if self.start is None:
            self.start=nd
            nd.next=self.start
            return
        
        temp=self.start
        while temp.next!=self.start:
            temp=temp.next
        temp.next=nd
        nd.next=self.start

    def insert_at_specific_pos(self,item,pos):
        if pos<=0:
            print("Invalid position")
            return
        if pos==1:
            self.insert_at_beg(item)
            return
        if self.start is None:
            print("Empty list")
            return
        nd=Node(item)
        i=1
        temp=self.start
        while i<pos-1 and temp.next!=self.start:
            temp=temp.next
            i+=1
        if i!=pos-1:
            print("Position out of range inserting at end")
        nd.next=temp.next
        temp.next=nd


    def insert_after_specific_item(self,item,spec_it):
        if self.start is None:
            print("Empty linked list")
            return
        
        nd = Node(item)
        temp=self.start
        while temp.info!=spec_it and temp.next!=self.start:
            temp=temp.next

        if temp.info!=spec_it:
            print("Specific item doesn't exist so adding element to end")
        
        nd.next=temp.next
        temp.next=nd

    def delete_from_beg(self):
        if self.start is None:
            print("Empty Linked List")
            return
        
        if self.start.next == self.start:
            temp=self.start
            self.start=None
            del temp
            return
        
        var=self.start
        temp=self.start
        while temp.next!=self.start:
            temp=temp.next
        temp.next=var.next
        self.start=var.next
        del var

    def delete_last_node(self):
        if self.start is None:
            print("Empty list cannot delete")
            return
        
        if self.start.next == self.start:
            temp=self.start
            self.start=None
            del temp
            return

        temp=self.start
        prev=None
        while temp.next!=self.start:
            prev=temp
            temp=temp.next
        prev.next=self.start
        del temp

    def delete_specific_pos(self,pos):
        if self.start is None:
            print("Empty linked list cannot delete")
            return
        
        if pos<=0:
            print("Invalid position")
            return

        if pos==1:
            #self.delete_from_beg()
            if self.start.next==self.start:
                temp=self.start
                self.start=None
                del temp
                return
            temp=self.start
            var=self.start
            while temp.next!=self.start:
                temp=temp.next
            temp.next=var.next
            self.start=var.next
            del var
            return
        
        temp=self.start
        prev=None
        i=1
        while i<pos and temp.next!=self.start:
            prev=temp
            temp=temp.next
            i+=1
        if i<pos:
            print("Position not found cannot delete node")
            return
        prev.next=temp.next
        del temp
        
    
    def delete_specific_item(self,spec_it):
        if self.start is None:
            print("Empty list cannot delete")
            return
        
        if self.start.info==spec_it:
            self.delete_from_beg()
            return
        
        temp=self.start
        prev=None
        
        while temp.info!=spec_it and temp.next!=self.start:
            prev=temp
            temp=temp.next
        
        if temp.info!=spec_it:
            print("Item doesn't exist cannot delete")
            return
        
        prev.next=temp.next
        del temp
        

    
    def dispLinkedList(self):
        if self.start is None:
            print("Linked list is empty")
        else:
            temp=self.start
            while temp.next!=self.start:
                print(temp.info, end = " -> ")
                temp=temp.next
            print(temp.info)
        

l1=CircularLinkedList()
l1.insert_at_beg(10)
l1.insert_at_beg(5)
l1.insert_at_end(15)
l1.insert_at_end(18)
l1.insert_at_end(22)
# l1.insert_at_specific_pos(20,7)
# l1.insert_after_specific_item(20,0)
l1.delete_specific_item(18)

l1.dispLinkedList()

        
