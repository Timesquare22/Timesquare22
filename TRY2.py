import random
Done = []
box = ["F","L","O","W","E","R"]
Words = ["FLOWER","LOWER","ROLE","WORE","FLOW"]
i = 5
while i > 1:
    random.shuffle(box)
    print(box)
    ST_1 = str(input("Write word: "))
    Done.append(ST_1)
    print("new list:",Done)
    if Done == Words:
        print("DONE")
        break
i = i + 1