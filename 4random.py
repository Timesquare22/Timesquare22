k =[]
for i in range(5):
    k.append("x" * 5)
print(k)
for i in range(5):
    print("a",end=" ")
def real(xs):
    lop = "x"
    for x in xs:
     lop = lop *  x
    return (lop)
joe = [2,2,3] 
print(real(joe))

age= int(input("enter your age: "))
while age <= 0:
    print("age aint negative")
    age = int(input("enter age please: "))
print(f"you are {age}yrs old")
import random 
number = random.sample(range(1,10),2)
i = 0
while i < 4:
    peal = int(input("enter new password : "))
    mite = f"ACCESS CODE {peal}"
    if peal != 4569:
        print("wrong password")    
    if peal == 4569:
        print(number)
        print(mite)
        break
    if i < 3:print("new code") 
    if i == 3:print("ACCESS DENIED")
    i = i + 1


class trick():
    def __init__(self,name,age,occupation,style,gender):
        self.name = name 
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.style = style 
    def details(self):
        print(" ")
        print("family details")
        print(" ")
        print("name:",self.name)
        print("age:",self.age) 
        print("gender:",self.gender)
        print("occupation:",self.occupation)
        print("style:",self.style)  
    def user(self):
        fun = input("my data:")
        return fun
fam_1 = trick("dad",70,"business","cringy","male")
fam_2 = trick("mom",60,"agent","sweet","female")
fam_3 = trick("twin",27,"nutritionist", "unique","female")
fam_4 = trick("Biggy",29,"tech","hard", "female")
fam_5 = trick("bro",31,"doc","sound","male")   
       
#print(fam_1.details()) 
#print(fam_2.details()) 
#print(fam_3.details()) 
#print(fam_4.details()) 
#print(fam_5.details()) 
print(fam_3.user())

 