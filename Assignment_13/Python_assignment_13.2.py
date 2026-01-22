# write a program which accepts radius of circle and prints area of circle 
# Input: 4
# Output : 50.24

def Area(radius,Pi=3.14):
    return Pi*radius*radius

def main():
    radius = 0
    Ret = 0

    print("Enter the radius of circle:  ")
    radius= int(input())

    Ret = Area(radius)
    print("Area of circle is: ",Ret)
        
if __name__ == "__main__":
    main()