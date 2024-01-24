# Copy here code of line function from previous exercise and use it in your solution
# Copy here code of line function from previous exercise
def line(number, letter):
    if letter == "":
        print("*" * number)
    else:
        print(letter[0] * number)


def triangle(size, letter):
    # You should call function line here with proper parameters
    for i in range(size+1):
        if(i%2 == 0):
            line(i, letter)
        else:
            line(i, letter)
def square_of_hashes(size, letter):
    # You should call function line here with proper parameters

    for i in range(0, size):

        line(size, letter)

def square(height, character, size):
    # You should call function line here with proper parameters
    for i in range(height):
        line(size, character)

def shape(size, letter, height, letter2):
   
        triangle(size, letter)
        square(height, letter2, size)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")