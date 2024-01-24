# Copy here code of line function from previous exercise
def line(number, letter):
    if letter == "":
        print("*" * number)
    else:
        print(letter[0] * number)
def box_of_hashes(height):
    # You should call function line here with proper parameters
    for i in range(height):

        line(10, "#")
def square_of_hashes(size):
    # You should call function line here with proper parameters

    for i in range(0, size):

        line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
    print()
    square_of_hashes(3)