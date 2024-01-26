# Write your solution here
Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

layers = int(input("Layers: "))
length_width = layers * 2 - 1

#To print the square we will print the lines in the first half, then the lines in the center, then the lines in the second half
first_half = "" 
center_string = str()

#Calculates the center line
#We first grab the first half of the center line, we will then reverse that initial half and add it to the end of the center line
#Example: 4 layers
for i in range(1, layers+1):
    center_string += Alphabet[layers - i] #Results in D->DC->DCB -> DCBA
reverse_string = center_string[::-1] #We reverse the center string
center_string = center_string + reverse_string[1:layers] #Add it to the center line, making sure to ignore the initial element, DCBA + BCD


center_coord = int(len(center_string) / 2 )
center_letter = center_string[center_coord]

#This for loop calculates the first half
x = 0 #Counts uneven numbers: 1, 3, 5, 7, 9...
for i in range(length_width, 1, -1):
    if i == length_width: #On our first iteration, the first line will always consist of our initial letter multiplied by the length and width of the square
        first_half += center_string[0] * length_width + "\n"
        x += 1
    if i % 2 != 0 and i != length_width:
        #str1 = ""  # 5c + 2D = 7 #add at beginning and add at end
        inner_letter = center_string[x] #C
        
        outter_letters = center_string[0:x]  #Grabbing the letters for the edges of the line i.e: for 7 layers, you'd have DC at the beginning and CD at the end of the second line
                                             #outter letters are reversed and added to the end of the line
        str1 = outter_letters +  inner_letter * i + outter_letters[::-1] 
        first_half += str1 + "\n" 
        x += 1


second_half = first_half[::-1] #the second half is just the first half in reverse, with the "\n" at the end removed
print(first_half[:-1]) 
print(center_string)
print(second_half[1:])

