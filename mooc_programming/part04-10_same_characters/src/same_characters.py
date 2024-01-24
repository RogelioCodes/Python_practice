# Write your solution here
def same_chars(word, x, y):
    try:
        if word[x] == word[y]:
            return True
        else:
            return False
    except:
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))