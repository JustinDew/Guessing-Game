import random

# determines how many spaces are needed after the name for the high score
def spaces(name):
    for i in range(14 - int(len(name))):
        name+=" "
    return name

reset = ["AAAA          7\n",
         "BBBB          7\n",
         "CCCC          7\n",
         "DDDD          8\n",
         "EEEE          9"]
numList = []
highScoreList = []

total = 0
tries = 0
number = 0
count = 0
guess = 0
maxTries = 9

name = ""
spot = True
game = True
win = False

highScoreFile = open("HighScores.txt", "r")

# creates a array of 10 random numbers. Then one of those 10 random numbers is 
# randomly chosen
for i in range(10):
    numList.append(random.randint(0, 100))
number = numList[random.randint(0, 9)]

# Loops the game until you have answered 9 times or got the answer. It does
# not allow you to input something other than a number that is 0-100.
while game:
    try:
        guess = int(input("Guess a number between 0-100. You have " + str(maxTries) + " attempts. "))
        if guess >= 0 and guess <= 100:
            if guess == number:
                tries+=1
                game = False
                win = True
            else:
                tries+=1
                print("WRONG")
                if guess - number > 0:
                    print("Its Lower! You have ", maxTries - tries  ," attempts left!")
                else:
                    print("Its Higher! You have " , maxTries - tries , " attempts left!")
            if tries == maxTries:
                game = False;
        else:
            print("Thats not a number between 1-100. Try again.")
    except ValueError:
        print("Thats not a number. Try again")
        
# Determines if you won or not. If you won, you have the chace of putting your
# name on the leaderboards if you got a low enoough score. 
if tries <= maxTries and win:
    print("Correct! You win!\nIt only took you ", tries ," attempt(s)!")
    for i in highScoreFile.readlines():
        highScoreList.append(i) 
    while spot:
        if tries <= int(highScoreList[count][-2]):
            name = input("High Score! What name would you like to input? (less than 12 characters) ")
            name = name.upper()
            if len(name) > 12:
                name = "PEASANT"
            highScoreList.insert(count, spaces(name) + str(tries))
            highScoreList.insert(count + 1, "\n")
            highScoreList.pop()
            spot = False
        count+=1
        if count == 5:
            spot = False
    highScoreFile.close()
    highScoreFile = open("HighScores.txt", "w")
    highScoreFile.writelines(highScoreList)
    highScoreFile.close()

else:
    print("Well... You lost... Try harder next time?\nThe number was ",number)

# Displays the updated high score list
print("\nHigh Scores!\n---------------")
highScoreFile = open("HighScores.txt", "r")
print(highScoreFile.read())
highScoreFile.close()
print("---------------")

# Resets the high scores if you get a high score and name yourself "reset"
if name == "RESET":
    highScoreFile = open("HighScores.txt", "w")
    highScoreFile.writelines(reset)
    print("\nHigh scores have been reset.")
    highScoreFile.close()
    
input("Press enter to exit.")
