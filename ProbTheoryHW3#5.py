import random



#X = marked
#O = unmarked

fish = []



for i in range(50):
    fish.append('X')

print("How many fish total do you want to have?\n")
addFish = int(input())

if addFish < 85:
    print("No, you can't do that")
    exit()

for i in range(addFish - 50):
    fish.append('O')


rightNum = False
count = 0
print("\n")

while rightNum != True:
        random.shuffle(fish)
        testFish = []

        for i in range(50):
            testFish.append(fish[i])
        if testFish.count('X') == 15:
            rightNum = True
        else:
            count = count + 1
        if count % 100 == 0:
            print('')
        else:
            print(".", end='')
print(count)
