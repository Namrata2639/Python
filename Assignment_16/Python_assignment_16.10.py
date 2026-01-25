# Q.10. Write a program which accepts a name from user and displays the length of its name.
# Example:
# Input : Marvellous  
# Output : 10

def len_str(str):
    count = 0 
    for i in str:
        count += 1

    return count

def main():

    Str= input("Enetr the string: ")
    ouput = len_str(Str)

    print("length of String: ",Str,"is: ",ouput)

if __name__ == "__main__":
    main()
