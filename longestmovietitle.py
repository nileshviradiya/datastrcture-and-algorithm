import copy

def longestMovieTitle(input):
    dic= {}
    for i in range(len(input)):
        s=input[i].split()
        dic[input[i]]=list()
        for j in range(0,len(input)):
            value=input[j].split()
            if i!=j and s[len(s)-1]==value[0]:
                 dic[input[i]]=input[j]
    return dic
    # for key in dic:
    #     if len(dic[key]) > 0 :
    #         longstr=key +" "+ dic[key]
    #     else:
    #         longstr= key 
    #     print(longstr)
def get_longest_title(titles):
    adj_list = create_adj_list(titles)
    longest_title = list()
    memo = dict()
    for title in adj_list.keys():
        if title not in memo:
            local_visit = set()
            local_result = visit_title(title,
                                        adj_list, 
                                        local_visit,
                                        memo)
            if len(local_result) > len(longest_title):
                longest_title = copy.deepcopy(local_result)
    return concat_title(adj_list, longest_title)

def visit_title(title, adj_list, local_visit, memo):
    if title in memo:
        return memo[title]
    result = list()
    if title not in local_visit:
        result.append(title)
        local_visit.add(title)
        neighbors = adj_list[title]
        for next_title in neighbors:
            local_result = visit_title(next_title,
                                        adj_list, 
                                        local_visit,
                                        memo)
            new_result = [title] + local_result
            if len(new_result) > len(result):
                result = new_result
        local_visit.remove(title)
    memo[title] = copy.deepcopy(result)
    return result

def concat_title(adj_list, titles):
    if len(titles) == 0:
        return ''
    result = list()
    result.append(titles[0])
    for index in range(1, len(titles)):
        title = titles[index]
        words_in_title = title.split()
        sub_title = words_in_title[1:]
        result += sub_title
    if is_cyclic(adj_list, titles):
        result = result[:-1]
    return ' '.join(result)
        
def is_cyclic(adj_list, titles):
    if len(titles) <= 1:
        return False
    last_title = titles[-1]
    first_title = titles[0]
    if first_title in adj_list[last_title]:
        return True
    return False  

def create_adj_list(titles):
    firstWord_to_titles_hash = dict()
    result = dict()
    for title in titles:
        words = title.split()
        if len(words) != 0:
            first_word = words[0]
            if first_word not in firstWord_to_titles_hash:
                firstWord_to_titles_hash[first_word] = list()
            firstWord_to_titles_hash[first_word].append(title)
    for title in titles:
        words = title.split()
        if len(words) != 0:
            last_word = words[-1]
            if last_word in firstWord_to_titles_hash:
                titles = firstWord_to_titles_hash[last_word]
                result[title] = titles
            else:
                result[title] = list()
    return result







input=['OF MICE AND MEN', 'BLACK MASS', 'MEN IN BLACK']
input1=['a b', 'b c', 'c d', 'd e']
print(get_longest_title(input))
print(get_longest_title(input1))

#print(create_adj_list(input))
#print(create_adj_list(input1))
