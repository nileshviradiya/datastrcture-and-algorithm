def averageofstudent(list,n):
    sum=0
    for key,values in list.items():
        sum=sum+values
    print(sum/n)


input = dict([
    ('Nilesh',19),
    ('Ramesh',29),
    ('Mahesh',39),
    ('Ganesh',49)
    ])

averageofstudent(input,len(input))