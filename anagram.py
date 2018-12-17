def anagram(input):
    dic={}
    k =0
    group ={}
    print(dic)
    for i in input:
        k=k+1
        dic[k] ={}
        for j in i:
            dic[k][j]=0
            dic[k][j]= dic[k][j]+1
        #print(dic)
    counter=0
    group[counter]={}
    group[counter]=dic[1]
    #print(group)
    for i in dic:
        for j in group:
            for k in group[j]:
                temp = dic[i+1].get(k)
                if(group[j][k]!=temp):
                    counter=counter +1
                    group[counter] ={}
                    group[counter] = dic[i+1]
    print(group)  
input =["eat", "tea", "tan", "ate", "nat", "bat"]
anagram(input)





