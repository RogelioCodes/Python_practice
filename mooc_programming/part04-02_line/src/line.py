# Write your solution here
def line(number, letter):
    if letter == "":
        print("*" * number)
    else:
        print(letter[0] * number)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(7, "%")