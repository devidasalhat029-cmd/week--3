student=[  

    {
        "name":"vainshanvi" ,"marks" : 88,
        " name":"Sakshi" ,"marks" : 65,
        "name":"Yogita" ,"marks" : 95,
    }
]


#part b

def get_status(marks):
    if marks >= 75:
        return 'destination'
    elif marks >=60:
        return 'A'
    else :
        return 'fail'
    
    #part c
    print(f"Name :{name}  marks :{marks}")