def calculate_grade(name , rollNumber, marks):
     # Output Grades
        print("Name: ", name)    
        print("Roll Number: ", rollNumber)
        print("Total Marks : ", marks)
        print("Average: ", round(marks/3 ,3),"%")
        print("pass" if (marks/3) > 40 else "Fail")


def main():
    #Input for name and Roll Number
    name = input("Enter Name: ")
    rollNumber = int(input("Enter Roll Number: "))

    marks = 0

    try:
        # Taking input of marks for the subjects
        for _ in range(3):
            mark = int(input(f"Enter Subject {_+1} marks: "))
            marks += mark
        
        calculate_grade(name,rollNumber , marks)    
        
       
    except Exception as err:
        print(f"Error is: {err}")
        print("Cannot genrate for this data")     
    
    finally:
        print("Thank You!!!")
    
if __name__ == "main":
    main()
    