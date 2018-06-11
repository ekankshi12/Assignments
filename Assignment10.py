# *** Question 1 ***
class Circle():
  def __init__(self,r):
    r = int(input("enter the radius"))
    self.r = r
  def  getArea(self):
    a =  3.14*self.r**2
    return a
    print(a)
  def getCircumference(self):
    c = self.r*2*3.14
    return c
    print(c)

# *** Question 2 ***
class Student():
  def __init__(self,name,roll):
    self.name = name
    self.roll= roll
  def display(self):
    print(self.name)
    print(self.roll)

# ***Question 3***
class Temprature():
  def  convertFahrenhiet(self,celsius):
    f = (celsius*(9/5))+32
    return f
    print(f)

  def convertCelsius(self,farenhiet):
    c = (farenhiet-32)*(5/9)
    return c
    print(c)

# ***Question 4***
class MovieDetails:
    def __init__(self, movie_name, artist_name, release, ratings):
        self.movie_name = movie_name
        self.artist_name = artist_name
        self.release = release
        self.ratings = ratings
        MovieDetails.update()


    def display(self):
        print(self.movie_name)
        print(self.artist_name)
        print(self.release)
        print(self.ratings)

# ***Question 5***
class Employee:

    def __init__(self, name, expend, savings):
        self.name = name
        self.savings = savings
        self.expend = expend

    def display(self):
        print(self.name)
        print(self.savings)
        print(self.expend)

    def total_salary(self, t_slary):
        self.t_salary = self.savings+self.expend
        return self.t_slary

    def display_salary(self):
        print(self.t_slary)



