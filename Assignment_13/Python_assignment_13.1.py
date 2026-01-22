# write a program which accepts length and width of rectangle and prints area
# Input: length = 4 width = 5
# Output : 20

def Area(width,length):
    return width * length

def main():
    width = 0
    length = 0
    Ret = 0

    print("Enter the length of rectangle: ")
    length = int(input())

    print("Enter the width of rectangle: ")
    width = int(input())

    Ret = Area(length,width)
    print("Area of rectangle is: ",Ret)
        
if __name__ == "__main__":
    main()