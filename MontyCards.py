import random

def genCards():
    cards = []

    for i in range(1,53):
        cards.append(i)
    random.shuffle(cards)
    return cards



print(genCards())
def thantosCards(prize,times):
        compGames = 0
        failedGames = 0
        stickWin = 0
        switchWin = 0
        while compGames != times:
                deck = genCards()
                yourChoice = deck.pop()
                for i in range(len(deck)-1):
                    deck.pop()
                if prize not in deck and yourChoice != prize:
                            #print("Uh, I revealed the prize oops")
                            failedGames = failedGames + 1
                            continue
                print("Your choice: " + str(yourChoice))
                print("Could've switched to: " + str(deck.pop()))

                if yourChoice == prize:
                        stickWin = stickWin + 1
                else :
                        switchWin = switchWin + 1

                compGames = compGames + 1

        print("We played " + str(failedGames + compGames) + " games")
        print("Of those " + str(failedGames) + " I ruined the game")
        print("Switch would've won you " + str(switchWin) + " times")
        print("Sticking would've won you " + str(stickWin) + " times")

def normalMode(prize,times):
        compGames = 0
        switchWin = 0
        stickWin = 0
        while times != compGames:
                deck = genCards()
                yourChoice = deck.pop()
                if yourChoice == prize:
                    stickWin = stickWin + 1
                else:
                    switchWin = switchWin + 1
                compGames = compGames + 1
        print("We played " + str(compGames) + " games")
        print("Switch would've won you " + str(switchWin) + " times")
        print("Sticking would've won you " + str(stickWin) + " times")

print("Hello let's play a card game!")
print("What card # is the prize?")
prize = int(input())
print("How many times should we play?")
times = int(input())
print("Thantos Version?")
answer = input();

if answer == "Y" or answer == "y" or answer == "yes" or answer == "Yes":
        print("OK!")
        print("Starting Thantos version with prize on #" + str(prize))
        thantosCards(prize,times)
else:
    print("OK!")
    print("Starting normal version with prize on #" + str(prize))
    normalMode(prize,times)