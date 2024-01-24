# Write your solution here
def remove_smallest(numbers: list):
    smallest = numbers[0]
    for item in numbers:
        if smallest > item:
            smallest = item
    print(smallest)
    numbers.remove(smallest)

