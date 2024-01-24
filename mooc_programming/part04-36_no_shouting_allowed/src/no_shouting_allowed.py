# Write your solution here
def no_shouting(list):
    no_supers_list = []
    for word in list:
        if word.isupper() == False:
            no_supers_list.append(word)
    return no_supers_list
