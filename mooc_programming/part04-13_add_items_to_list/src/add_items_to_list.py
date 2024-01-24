# Write your solution here
numbers = []
num_of_items = int(input("How many items: "))
for i in range(num_of_items):
    item = int(input(f"Item {i+1}: "))
    numbers.append(item)
print(numbers)
    