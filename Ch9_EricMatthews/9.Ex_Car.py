
class Car:
  def __init__(self,make,model,year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 24

  def get_descriptive_name(self):
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()

  def read_odometer(self):
    print(f"This car has {self.odometer_reading} miles on it.")

#2nd -- modify via a method
  def update_odometer(self,mileage):
  #add conditions
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back an odometer!")


#3rd -- increment via method
  def increment_odometer(self,miles):
    self.odometer_reading += miles
    print(f"This car has {self.odometer_reading} miles on it")
  

my_new_car = Car('VW','Tiguan',2012)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()
#we can modify this attribute's value 3 ways:

#1st -- directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#2nd -- modify via a method
my_new_car.update_odometer(22)
my_new_car.read_odometer()

#3rd -- increment via method
my_new_car.increment_odometer(100)
my_new_car.read_odometer



