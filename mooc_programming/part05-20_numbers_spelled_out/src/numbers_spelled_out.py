# Write your solution here
def dict_of_numbers():

    dictionary = {}
    numbers = []
    for i in range(100):
        numbers.append(i)

    #print(numbers)

    word0 = ['zero']
    wordints = ['one', 'two', 'three','four', 'five', 'six','seven', 'eight', 'nine']
    wordteens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
    'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    wordtens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    rest = []
    for i in range(len(wordtens)):
        rest.append(wordtens[i])
        for j in range(len(wordints)):
            rest.append(wordtens[i] + "-" + wordints[j])
    wordListFinal = []
    wordListFinal.append(word0[0])


    print(rest)
    for i in range(len(wordints)):
        wordListFinal.append(wordints[i])
    for i in range(len(wordteens)):
        wordListFinal.append(wordteens[i])
    for i in range(len(rest)):
        wordListFinal.append(rest[i])

    for i in range(len(numbers)): #wordListFinal:
        dictionary[i] = wordListFinal[i]
        
       # dictionary[i] = wordListFinal[i]
    #for i in range(len(wordtens)):
    #    wordListFinal.append(wordtens[i])
    return dictionary

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])