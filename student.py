student_name="yogita"
Student_marks=85
Student_Rollno=1
student_sub="java"
student_grade="A"
student_city="Pune"

#using list
student=["yogita ","Shital","Sanika","Laxmi","Srushti"]  
mark_list=(85,89,98,65,45,77)
rollno_list=(1,2,3,4,5)
subject_list=["java","python","c++","html","css"]
grade_list=["A","B","C","D","E"]
city_list=["Pune","Mumbai","Nashik","Aurangabad","Nagpur"]

#get rollno of SANIKA
print("Roll No of Sanika is:",rollno_list[student.index("Sanika")])

#DICTIONARY
STUDENT={
    "name":"yogita",
    "marks":85,
    "rollno":1,
    "subject":"java",
    "grade":"A",
    "city":"Pune"
}


#ACCESS VALUE FOROM DICTIONARY
print("Name:",STUDENT["name"])
print("Marks:",STUDENT["marks"])
print("Roll No:",STUDENT["rollno"])
print("Subject:",STUDENT["subject"])
print("Grade:",STUDENT["grade"])
print("City:",STUDENT["city"])

#NEW DATA ADD IN DICTIONARY
STUDENT["age"]=20
print("Age:",STUDENT["age"])

#CHEKING KEY IN DICTIONARY
print("Is 'name' key present in STUDENT dictionary?", "name" in STUDENT)
print(f"Is 'address' key present in STUDENT dictionary?", "address" in STUDENT)

#key of dictionry
print("Keys in STUDENT dictionary:", STUDENT.keys())
print("Values in STUDENT dictionary:", STUDENT.values())

