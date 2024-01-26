# Write your solution here
#This function returns a tuple formed from the paramaters (smallest, greatest, sum)
def create_tuple(x: int, y: int, z: int):
    smallest = min([x, y, z])
    greatest = max([x, y, z])

    sum = x + y + z
    my_tuple = (smallest, greatest, sum  )
    return my_tuple

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))