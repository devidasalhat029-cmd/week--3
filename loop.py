student=["yogita ","Shital","Sanika","Laxmi","Srushti"]  #list
print(student)    #print list
print(student[0])#First student
print(student[1])#second student
print(student[2])#third student
print(student[3])#Forth student
print(student[4])#fifth  Student

#loop 
for student in student:
    print(f"Hello {student}! Welcome to class")

mark_list=(85,89,98,65,45,77)#second list
for mark in mark_list:
    if mark>=90:
        print(f"Excellent you scored {mark}.")
    elif mark>=80:
        print(f"Good job! you scored {mark}")    
    else :
            print(f"passs! you scored {mark}")       