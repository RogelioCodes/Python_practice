# Write your solution here
def invert(dictionary: dict):
    new_dict = {}
    for i in list(dictionary):
     
        old_value = dictionary[i] #new key # first second
        dictionary[old_value] = i
       
        #dictionary[value] = dictionary[key]
        del dictionary[i]
    
