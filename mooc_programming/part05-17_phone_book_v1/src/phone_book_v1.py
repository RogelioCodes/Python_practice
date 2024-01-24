# Write your solution here
list = {}
while True:
    command = input("command (1 search, 2 add, 3 quit): ")
  
    if command == '3':
        print("quitting...")
        break

    if command == '1':
        name = input("name: ")
        if name in list:     
            print(list[name])
        else:
            print("no number")
           
    if command == "2":
        name = input("name: ")
        number = input("number: ")
        
        print("ok!")
       
        
        list[name] = number
      

   
"""
8 != 6 : Instead of 8 rows, your program prints out 6 rows:
ok!
ok!
09-334455
040-234567
no number
quitting...
with the input:
2
mike
040-234567
2
mary
09-334455
1
mary
1
mike
1
becky
2
mike
045-554433
1
mike
3
expected print out is
ok!
ok!
09-334455
040-234567
no number
ok!
045-554433
quitting...
"""
      