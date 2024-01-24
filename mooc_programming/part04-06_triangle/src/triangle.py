# Copy here code of line function from previous exercise
def line(number, letter):
    if letter == "":
        print("*" * number)
    else:
        print(letter[0] * number)



def triangle(size):
    # You should call function line here with proper parameters
    for i in range(size+1):
        if(i%2 == 0):
            line(i, "#")
        else:
            line(i, "#")
        


# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(6)
