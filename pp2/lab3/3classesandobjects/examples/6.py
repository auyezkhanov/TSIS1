class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40
print(p1.age)


#del p1.age
print(p1.age)

#del p1
print(p1)

class People:
  pass
# having an empty class definition like this, would raise an error without the pass statement