# Write your solution here
numbers = [1, 2, 3, 4, 5]
new_value = 0
index = 0
while True:
        
        index = int(input("Index: "))
        
        
    
        if index == -1:
               
                break
        else:
                new_value = int(input("New Value: "))
                numbers[index] = new_value
                print(f"{numbers}")
        
        