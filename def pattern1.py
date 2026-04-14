n=10
for i in range(4,0,-1):
  for j in range(i):
    print(n,end=" ")
    n-=1
  print(" ")

print()

class Person:
  name="Rinku"
  # def __init__(self,mark):
  #     self.mark=mark
  

  # def changeName(self,name):
  #   self.name=name    #create new name attribute for object/instance
  #   Person.name=name #change whole class attribute     
  #   self.__class__.name="hetal"
  @classmethod
  def changeName(cls,name):
    cls.name=name 

# p1=Person(56)
p1=Person()
p1.changeName("Hetal Jambukiya")
# print(p1.mark)
print(p1.name)
print(Person.name)

# print()


class Student:
  def __init__(self,math,phy,chem):
    self.math=math
    self.phy=phy
    self.chem=chem
  # self.percentage=str((self.math+self.phy+self.chem)/3)+"%"

  # def calcPercent(self):
  # self.percentage=str((self.math+self.phy+self.chem)/3)
  @property
  def percentage(self):
    return str((self.math+self.phy+self.chem)/3)

st1=Student(98,97,99) 
print(st1.percentage)

st1.phy=86
print(st1.phy)
# st1.calcPercent()
print(st1.percentage)


