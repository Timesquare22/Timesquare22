fruits = ["apple", "bush","HOOD"]
boss = ["kill","stop"]
fruits.append("stop")
print(fruits)
t = 10 
while t > 0:
  #print("more needs")
  if t == 3:
    print(" 7 more to go")
  if t == 6:
    print ("4 more to go")
  if t == 9:
    print("done")
  t -= 1
  print(t,end=',')
  
 
Mouse = ['apple', 'lemon', 'orange', 'grape', 'blueberry', 'tomato']
print(Mouse[3])
#Mouse.replace( "l", "k")
Mouse.count("r")
print(Mouse)
r='rule'
r.replace('r','m')
print(r)

bloom = "{0} is a lot of {1}".format("Python", "fun!")
#'Python is a lot of fun!'
print(bloom)

num = 20
if num == 20:
    print('the number is 20')
else:
    print ('the number is not 20')
    
a, b = 0, 1
while a <= 1000:
    print(a, end=',')
    a, b = b, a+b
print(a,b)

x = int(input("Please enter an integer: "))
#if x < 0:
#x = 0
#print('Negative changed to zero')
#elif x == 0:
#print('Zero')
#elif x == 1:
#print('Single')
#else:
#print('More')


