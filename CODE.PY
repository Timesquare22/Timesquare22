import random

JIN = random.random() #PRINTS BTW ZERO AND ONE RANDOM NUMBERS
print(JIN)
JINI = random.randint(10,25)# THIS GENERATES A RANDOM VALUE BTW A STATED RANGE WITH TWO PARAMETERS
print(JINI)
JIN = random.randrange(2,20,2)
print(JIN) #the addition of the random and range formula produces a random number with specs. ths three attributes possible
JIN = random.uniform(10,14)#PRODUCEA a float value withen a range
print(JIN)
JILO = random.sample(range(12,30), 4)# PRINTS RANDO NUBERS WITHEN A GIVEN RANGE AND LIST NUMBERS
print(JILO)
# next introducing the shuffle  method on ra]ndom numbers from maybe a list
gub = [5,1,7,8,4,2,5,26,61]
random.shuffle(gub)
print(gub)
print(random.choice(gub))
