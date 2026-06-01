def get_grade(score):
    if score >= 80:
        return 'A'
    elif score >=70:
        return 'B'
    elif score >=50:
        return 'C'
    else:
        return 'Fail'
student =["Yogita","Devidas","Shital","Sanika"]
mark=[85,98,78,56,99,98]

for i in range(len (student)):
    grade = get_grade(mark[i])
    print(f"{student[i] scored{mark}}")