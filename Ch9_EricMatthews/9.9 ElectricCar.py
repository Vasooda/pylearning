
#PARENT CLASS

class Car:
  def __init__(self,make,model,year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

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
   # print(f"This car has {self.odometer_reading} miles on it")
  

#Battery Class

class Battery:
  def __init__(self,battery_size=75):
    self.battery_size = battery_size
  
  def describe_battery(self):
    print(f"This car has a {self.battery_size} -kWh battery.")

  def get_range(self):
    if self.battery_size == 75:
      range = 260
    elif self.battery_size == 100:
      range = 315
    print (f"This car can go about {range} miles on a full charge.")

  def upgrade_battery(self):
    if self.battery_size == 75:
      self.battery_size = 100
      print(f"Battery needs to be updated to 100 kWh")
    else:
      print(f"Battery size already upgraded!")

#CHILD CLASS

class ElectricCar(Car):
  def __init__(self,make,model,year):
    super().__init__(make,model,year)
    self.battery = Battery()  
  

my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()