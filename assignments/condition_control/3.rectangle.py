"""
    Given the length and breadth of a rectangle, write a program to find whether the area of the
    rectangle is greater than its perimeter. For example, the area of the rectangle with length = 5 and
    breadth = 4 is greater than its perimeter.
"""
length=float(input("Enter length of rectangle: "))
breadth=float(input("Enter breadth of rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

if area>perimeter :
    print(f"Yes the area of rectangle {area} sq unit is greater than its perimeter {perimeter} units")
elif area<perimeter :
    print(f"No the area of rectangle {area} sq unit is not greater than its perimeter {perimeter} units")
else:
    print(f"Area and Perimeter are equal")
