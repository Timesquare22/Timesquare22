def Passe():    
    return print (("another day" + " " )*3) #the role of brackets in coding changes alot

Passe() #a parametere less function
def finit(money,fruits ):
    return  print (f" adrein loves { money} and {fruits} in the morning\n"  * 3 ) 
#\n is put withen a string so as to make a new line
#indentation in the code, shows the new line belongs to the function above
#def ink():   , the ink function permits inputing of the users data to proceed
    region = 18 
    sound = int(input( "mom has a loud voice  : "))
    sound += region
    return print(sound)
#ink() #here, we are running a return value without storing it in a container
def finits(money,fruits ): #there are functions that perform a task and those who return a value
    x = "mouse " if money > fruits else "more straws"
    return print(x)# the return function only returns only when print function is stated before , 
finit(450, "straws")
finits(50 , 2)
def add():
    word = "loud noises" if 6 >= 8 else "weight"
    plains = "gropies " if 4 <= 45 else "down"
    print(plains)
    return print(word)
add()#returning more than one variable in a parameter free function
noun = "worst" if 85 <= 45 else "good"
print(noun)

#def biz(): #under score is used in functions when u cant insert a value of i because the function will nullify it
    #for _ in range (3):
       # input("kind of currency: ")
       # input( "type of money: ")
       # int(input("type of unit is : ")) 
           #return input 
#print(biz())

#tuples() are immutable unlike lists [] , means we cant add new items to the tuple through index
# or replace its content unlike lists[].

Fruits = ("nice", "cane","sweet ", "mouse","oranges") #tuples, same element containment only, we cant remove nor add items from the
#the tuple, we cant modify which items the tuple is storing
print(Fruits[1])
if "nice" and "oranges"  in Fruits: print("fresh fruits") # "and"if one of the statemennts are false the whole thing is false
#"or" if atleast one of them is true, it validates the process.
else: print("more")
if "one"  or "oranges" in Fruits:
    print ( "true ")
else: print("more")