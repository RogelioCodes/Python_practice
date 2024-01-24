# Write your solution here
def histogram(str: str):
    list = dict()
    for letter in str:
        
        if letter not in list:
            list[letter] = []
        list[letter].append("*")
    stars = "*"
    for key, value in list.items():
        print(f"{key} { stars * len(value)}")
   
if __name__ == "__main__":   
    histogram("abba")
    histogram("statistically")