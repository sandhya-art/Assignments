class Plane:
 
    # init method or constructor
    def __init__(self, wings):
        self.wings = wings
 
    # Sample Method
    def fly(self):
        print('I am able to fly with {} wings'.format(self.wings))
    @staticmethod
    def tri():
        print('parent method')
plane1 = Plane('2')
plane2= Plane('2')
plane1.fly()
class Jet(Plane):
    def __init__(self, color):
        self.color = color
    #@staticmethod
    def fly(self):
        print('I am able to fly',self.color)
jet_1=Jet('purple')
jet_2=Jet('lilac')
jet_1.fly()
class Passenger(Plane):
    def __init__(self, color):
        self.color = color
    def fly(self):
        print('I am able to fly',self.color)
    @staticmethod
    def get():
        print('Just a static method')
passenger_1=Passenger('yellow')
passenger_2=Passenger('Brown')
passenger_1.fly()
passenger_1.get()
passenger_2.tri()
