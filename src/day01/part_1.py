initial_dial = 50
count = 0
wrap = 100

with open('puzzle_pieces/sequence.txt','r') as file:
    for line in file:
        for word in line.split():
            lP = 0
            operation = word[lP]
            lP += 1
            number = 0
            while lP < len(word):
                number *= 10
                number += int(word[lP])
                lP += 1
            
            if operation == "L":
                initial_dial -= number
            else:
                initial_dial += number
            
            if abs(initial_dial) > 99:
                initial_dial = initial_dial % wrap

            if initial_dial == 0:
                count += 1

print(count)
