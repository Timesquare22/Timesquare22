import random

JIN = random.randrange(1, 45)
if JIN % 2 == 0:
    print("EVEN")
else:
    print("odd")  # random number generated
i = 9  # i runs from from 0 to 9, that makes 10 digits
while i >= 0:
    poll = int(
        input("guess the random number: ")
    )  # user enters a random number between 2 to 20
    if poll > JIN:
        print("you are greater")  # the code tells u when u are above the number
    if poll < JIN:
        print("you are lower")  # the code tells u when you are below the number
    if i == 0:  # the end of the lives at the end of the sequence
        print("gameover")
    if poll == JIN:  # the end code, wins and game over at the end
        print("you've won")
        print("GAME OVER")
        break  # ends the code when player wins
    else:
        print("try again")  # or retry the game
    i = i - 1


box = ["F", "L", "O", "W", "E", "R"]
def gamble(x):
    random.shuffle(x)
    x = box
    return box
print(gamble(box))
