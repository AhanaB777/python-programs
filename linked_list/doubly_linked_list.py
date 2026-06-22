class Node:
    def __init__(self,item):
        self.prev=None
        self.info=item
        self.next=None
        

class DoublyLinkedList:
    def __init__(self):
        self.start=None
    
    def insert_at_beg(self,item):
        nd=Node(item)
        if self.start is None:
            self.start=nd
            return
        nd.next=self.start
        self.start.prev=nd
        self.start=nd
    
    def insert_at_end(self,item):
        nd=Node(item)
        if self.start is None:
            self.start=nd
            return
        temp=self.start
        while temp.next is not None:
            temp=temp.next
        temp.next=nd
        nd.prev=temp

    def insert_after_specific_pos(self,item,pos):
        if pos<=0:
            print("invalid pos")
            return
        if self.start is None:
            print("list is empty")
            return
        if pos==1:
            self.insert_at_beg(item)
            return
        nd=Node(item)
        temp=self.start
        i=1
        while i<pos-1 and temp.next is not None:
            temp=temp.next
            i+=1
        if i!=pos-1:
            print("Position out of range")
            return
        nd.next=temp.next
        nd.prev=temp
        if temp.next is not None:
            temp.next.prev=nd
        temp.next=nd

    def insert_after_specific_item(self,item, spec_it):
        if self.start is None:
            print("Empty linked list")
            return
        temp = self.start
        while temp is not None and temp.info != spec_it:
            temp = temp.next
        if temp is None:
            print("Specific item not found")
            return
        nd = Node(item)
        nd.next = temp.next
        nd.prev = temp
        if temp.next is not None:
            temp.next.prev = nd
        temp.next = nd

    def delete_from_beg(self):
        if self.start is None:
            print("Empty list cannot delete")
            return
        temp = self.start
        if self.start.next is None:
            self.start = None
            del temp
            return
        self.start = self.start.next
        self.start.prev = None
        del temp

    def delete_from_end(self):
        if self.start is None:
            print("Empty list cannot delete")
            return
        temp = self.start
        if temp.next is None:
            self.start = None
            del temp
            return
        while temp.next is not None:
            temp = temp.next
        temp.prev.next = None
        del temp

    def delete_at_position(self, pos):
        if self.start is None:
            print("Empty list cannot delete")
            return
        if pos <= 0:
            print("Invalid position")
            return
        if pos == 1:
            self.delete_from_beg()
            return
        temp = self.start
        i = 1
        while temp is not None and i < pos:
            temp = temp.next
            i += 1
        if temp is None:
            print("Position out of range")
            return
        if temp.next is None:
            temp.prev.next = None
            del temp
            return
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        del temp

    def delete_specific_item(self, item):
        if self.start is None:
            print("Empty list cannot delete")
            return
        temp = self.start
        if temp.info == item:
            self.delete_from_beg()
            return
        while temp is not None and temp.info != item:
            temp = temp.next
        if temp is None:
            print("Item not found")
            return
        if temp.next is None:
            temp.prev.next = None
            del temp
            return
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        del temp

    def disp(self):
        if self.start is None:
            print("Empty linked list")
            return
        temp=self.start
        while temp is not None:
            print(temp.info, end=" <-> ")
            temp=temp.next
        print("None")

l1=DoublyLinkedList()
# l1.insert_at_beg(20)
# l1.insert_at_beg(10)
# l1.insert_at_beg(5)
# l1.insert_at_end(30)
# l1.insert_at_end(45)
# l1.insert_after_specific_pos(15,3)
# l1.insert_after_specific_item(23,20)
l1.disp()
l1.delete_from_end()
l1.disp()