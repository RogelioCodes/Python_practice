# Write your solution here
list = []

item = 0
while True:
    print(f"The list is now {list}")
    operation = input("a(d)d, (r)emove or e(x)it: ")
    if operation == "x":
        print("Bye!")
        break
    if operation == "d":
        item += 1
        list.append(item)
    if operation == 'r':
        item -= 1 
        list.pop()
    