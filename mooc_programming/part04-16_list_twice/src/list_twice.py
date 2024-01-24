# Write your solution here
original = []
while True:
    item = int(input("New item: "))
    if item == 0:
        print("Bye!")
        break
    original.append(item)
    in_order = sorted(original)
    print(f"The list now: {original}")
    print(f"The list in order: {in_order}")

    

