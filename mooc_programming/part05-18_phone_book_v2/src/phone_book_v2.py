# Write your solution here
# Write your solution here
list = {}
while True:
    command = input("command (1 search, 2 add, 3 quit): ")
   # print(list)
    if command == '3':
        print("quitting...")
        break

    if command == '1':
        name = input("name: ")
        if name in list:
            for number in list[name]:
                print(number)     
            #print(list[name])
        else:
            print("no number")
           
    if command == "2":
        name = input("name: ")
        number = input("number: ")
        
        print("ok!")
        
        if name not in list:
            list[name] = []
            list[name].append(number)
        else:
            list[name].append(number)