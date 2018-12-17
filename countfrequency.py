def countfrequency(input):
    dic={}
    for i in input:
        if i in dic:
            dic[i] +=1
        else:
            dic[i]=1
    return dic
        




input= [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
print(countfrequency(input))

