# This file was created by: Theodore Do

#in object constructor - like a mold you can make things with like blueprint
class Group:
  # _init_ is a built in function/method
  def __init__(self, name, size,):
    self.name = name 
    self.size = size
    self.tablenumber = 0

g1 = Group("TheBoys", "6" , 1)
g0 = Group("TheDudes", "6", 0)
g2 = Group("TheGuys", "6", 1)
g3 = Group("TheFellas", "7", 1)

print(g0.name)
print(g0.size)
print(g0.tablenumber)

print(g1.name)
print(g1.size)
print(g1.tablenumber)

print(g2.name)
print(g2.size)
print(g2.tablenumber)




# class Person:

#   def __init__(self, name, year):
#     self.name = name
#     self.year = year

# # create an instance of the person class...
# p1 = Person("John", 36)

# print(p1.name)
# print(p1.year)

