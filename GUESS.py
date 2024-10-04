import random

JIN = random.randrange(2, 20, 2)
poll = int(input("guess the random number: "))
if poll == JIN:
    print("YOU WIN")
else:
    print("you lose")
i = 1
while i < 10:
    JIN = random.randrange(
        2, 20, 2
    )  # if i put like this, those it get to generate a new code everytime?
    poll = int(input("guess the random number: "))
    if i == 10:
        print("gameover")
    if poll == JIN:
        print("you've won")
    else:
        print("try again")
    i = i + 1
