def create_adj_list(titles):
    firstWord_to_titles_hash = dict()
    result = dict()
    for title in titles:
        words = title.split()
        # print(words)
        if len(words) != 0:
            first_word = words[0]
            #print(first_word)
            #print(firstWord_to_titles_hash)
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
    print(firstWord_to_titles_hash)
    print(result)
    return result
   

Input = ['OF MICE AND MEN', 'BLACK MASS', 'MEN IN BLACK']
create_adj_list(Input)

