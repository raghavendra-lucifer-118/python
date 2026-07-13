#Input for name and Roll Number
name = input("Enter Name: ")
rollNumber = int(input("Enter Roll Number: "))

marks = 0
for _ in range(3):
    mark = int(input(f"Enter Subject {_+1} marks: "))
    marks += mark
    

# Output Grades
print("Name: ", name)    
print("Roll Number: ", rollNumber)
print("Total Marks : ", marks)
print("Average: ", round(marks/3 ,3),"%")
print("pass" if (marks/3) > 40 else "Fail")
    