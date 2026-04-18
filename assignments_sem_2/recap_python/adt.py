"""Create an ADT of array using OOPs concept.
Define a class with the name array1 and with the following members
Data member List l
Data member Size of the array max
Define a member function(constructor) __init__ () which define an empty list l
and define size of the list.
Define member function CreateArray(), take input for the list l with size max
Define member function ShowArray() display all the values of the array
Define member function LinearSearch(), search one item in the array, return
index of the item
Define member function Sorting(), arrange all the elements in sorted order
Define member function BinarySearch(), return index of the item in the
sorted array
Write a main function, create an object of the class array1, call all the
member functions of the class array1 and implements data structure
operations on array."""

class array1:
    def __init__(self, l, size):
        self.l = l
        self.size = size

    def CreateArray(self):
        for i in range(self.size):
            x=int(input("Enter element: "))
            self.l.append(x)

    def ShowArray(self):
        print(self.l)

    def LinearSearch(self, key):
        for i in range(self.size):
            if self.l[i]==key:
                return i
        return -1

    def Sorting(self):
        return self.l.sort()

    def BinarySearch(self, key):
        low=0
        high=self.size - 1
        while low<=high:
            mid=(low + high)//2
            if self.l[mid]==key:
                return mid
            elif self.l[mid]<key:
                low=mid+1
            else:
                high=mid-1
        return -1


l = []
size=5
obj=array1(l,size)
obj.CreateArray()
obj.ShowArray()
k=int(input("Enter key to search(linear): "))
print(obj.LinearSearch(k))
obj.Sorting()
obj.ShowArray()
k=int(input("Enter key to search(binary): "))
print(obj.BinarySearch(k))

    