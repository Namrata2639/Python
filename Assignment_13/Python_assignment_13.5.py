# Write a program which accepts marks and display grades
# Condition Exampl
#  >= 75 -> Distinction
#  >= 60 -> First Class
#  >= 50 -> Second Class 
#  <50   -> Fail

def Grades(Marks):

    if Marks >= 75 :
        return "Distinction"
    
    elif Marks >= 60:
        return "First_Class"
    
    elif Marks >= 50:
        return "Second_Class"
    
    elif Marks <50 :
        return "Fail"
       
def main():
    Marks = 0.0

    print("Enter the Marks:  ")
    Marks = float(input())

    Ret = Grades(Marks)
    print("For",Marks,"Grades are: ",Ret)
    
        
if __name__ == "__main__":
    main()
