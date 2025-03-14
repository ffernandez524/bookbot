def word_count(book):
    return len(book.split()) 

def char_count(string):
    char_counts = {}
    for char in string:
        if char.isalpha() == True:
            if char.lower() in char_counts:
                char_counts[char.lower()] += 1
            else:
                char_counts[char.lower()] = 1
    return char_counts

def dict_sort(dict):
    list = []
    for key in dict:
        dict_to_add = { "Character" : key,
                        "Count" : dict[key]}
        list.append(dict_to_add)
    list.sort(reverse=True, key=sort_on)

    return list

def sort_on(dict):
    return dict["Count"]