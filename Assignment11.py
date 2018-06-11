# *** Question 1 ***
class Animal:
    def animal_attribute(selfself):
        print("Animal")

class Tiger(Animal):
    print()
tigerobj = Tiger()
tigerobj.animal_attribute


# *** Question 2 ***
# The ouput will be
#  A B
#  A B

# *** Question 3 ***
class Cop:
    def __init__(self, name, age, work, exp, desig):
        self.name = name
        self.age = age
        self.work = work
        self.exp = exp
        self.desig = desig
    def add(self):
        print()

    def display(self):
        print(self.name)
        print(self.age)
        print(self.work)
        print(self.exp)
        print(self.desig)
    def update(self):
        print()
class Mission(Cop):
    def __init(self):
        super(Mission,self).__init()
    def mission_details(self,Mission):
        print()
    def add_mission_details(self,Mission):
        print()

Missionobj = Mission('Sherlock', 56, 'Cop', '3years', 'Detector')
Missionobj.mission_details('Secret')
Missionobj.add_mission_details('Secret')
Missionobj.add
Missionobj.display()
Missionobj.update()

# *** Question 4 ***
class Shape:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def Area(self, length, breadth):
        area = length * breadth
        return area

class Rectangle(Shape):
    print()
class Square(Shape):
    print()

rect = Rectangle(23,56)
sqr = Square(33,33)
rect.Area(23,56)
sqr.Area(33,33)





