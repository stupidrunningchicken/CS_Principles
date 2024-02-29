# global variable

x=10

# creating a function
def redunDun():
   # its a trap
   # global x 
   x = 10 
   return("hello" , x)

redunDun()

print(x)

while x != 20: 
   print("FOREVER")
   x+=1
   print(x)

print(7%6)