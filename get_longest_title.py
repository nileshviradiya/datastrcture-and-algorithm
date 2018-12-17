import copy

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

Input = ['OF MICE AND MEN', 'BLACK MASS', 'MEN IN BLACK']
assert(get_longest_title(Input) == 'OF MICE AND MEN IN BLACK MASS')

Input = []
assert(get_longest_title(Input) == '')

Input = ['a']
assert(get_longest_title(Input) == 'a')

Input = ['a', 'b']
assert(get_longest_title(Input) == 'a' or get_longest_title(Input) == 'b')

Input = ['a', 'a b']
assert(get_longest_title(Input) == 'a b')

Input = ['a b', 'b c', 'c d', 'c e', 'e f']
assert(get_longest_title(Input) == 'a b c e f')

Input = ['e f', 'c e', 'c d','b c', 'a b']
assert(get_longest_title(Input) == 'a b c e f')

Input = ['c d','b c', 'a b', 'e f', 'c e']
assert(get_longest_title(Input) == 'a b c e f')

Input = ['a b', 'b c', 'c a']
result = get_longest_title(Input)
assert(result == 'a b c' \
       or result  == 'b c a' \
       or result  == 'c a b')

Input = ['c a', 'b c', 'a b']
result = get_longest_title(Input)
assert(result == 'a b c' \
       or result  == 'b c a' \
       or result  == 'c a b')

Input = ['b c', 'a b', 'c a']
result = get_longest_title(Input)
assert(result == 'a b c' \
       or result  == 'b c a' \
       or result  == 'c a b')