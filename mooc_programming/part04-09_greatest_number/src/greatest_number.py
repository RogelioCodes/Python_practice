# Write your solution here
# You can test your function by calling it within the following block
def greatest_number(x, y , z):
    greatest = x
    if x == y or x == z:
        if y > z:
            return x
        else:
            return z
    if y == x or y == z:
        if x > z:
            return x
        else:
            return z
    if z == y or z == x:
        if y > x:
            return y
        else:
            return x
    if x > y and x > z:
        greatest = x
    if y > x and y > z:
        greatest = y
    if z > x and z > y:
        greatest = z
    return greatest

if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)