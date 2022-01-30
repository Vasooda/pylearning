#PARENT CLASS
class Restaurant:
  def __init__ (self,name, cuisine):
    self.name = name
    self.cuisine = cuisine
    self.number_served = 0
  
  def describe_restaurant(self):
    print(f"At {self.name} you can find {self.cuisine} cuisine")

  def open_restaurant(self):
    print(f"{self.name} is open 24/7")

  def count_customers_served(self):
    print(f"This restaurant has served {self.number_served} customers.")

  def update_customers_served(self, customers):
    self.number_served = customers

  def increment_customers_served(self, patrons):
    self.number_served += patrons


#sub-sub class
class Flavors:
  def __init__(self):
    self.icecream_flavors = []

  def list_icecream_flavors(self):
    print(f"We carry the following icecream flavors:")
    for icecream_flavors in self.icecream_flavors:
      print(f"-{icecream_flavors.title()}") 

#CHILD CLASS
class IceCreamStand(Restaurant):
  def __init__(self,name,cuisine):
    super().__init__(name,cuisine)
    self.flavors = Flavors()


firstuser = IceCreamStand('Buddhas Kitchen','Thai')
firstuser.flavors.icecream_flavors = ['mango sticky rice', 'friend banana icecream']

print(firstuser.describe_restaurant())
print(firstuser.flavors.list_icecream_flavors())
