#write a python program to determine how many complete rows can be formed.
#input the total number of students
total_students = int(input("Enter the total number of students: "))
# Initialize the number of complete rows
students_in_row = 0
# Loop to determine the number of complete rows
while total_students >= students_in_row + 1:
    students_in_row += 1
    total_students -= students_in_row
# Output the number of complete rows
print("The number of complete rows that can be formed is:", students_in_row)