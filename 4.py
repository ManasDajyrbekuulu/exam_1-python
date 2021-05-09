# Абстракция(класс)
 
from abc import ABC, abstractmethod
 
class Polygon(ABC):
 
    @abstractmethod
    def noofsides(self):
        pass
 
class Triangle(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("У меня есть 3 стороны")
 
class Pentagon(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("у меня 5 стороны")
 
class Hexagon(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("у меня 6 сторон")
 
class Quadrilateral(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("У меня 4 стороны")
 
# Driver code
R = Triangle()
R.noofsides()
 
K = Quadrilateral()
K.noofsides()
 
R = Pentagon()
R.noofsides()
 
K = Hexagon()
K.noofsides()