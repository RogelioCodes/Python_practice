# write your solution here
def read_fruits():
    fruit_dict = {} #dict of fruits and prices, ie: {banana: 6.5}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            
            name = parts[0]
            price = parts[1] 
            
            fruit_dict[name] = float(price)
    return fruit_dict
