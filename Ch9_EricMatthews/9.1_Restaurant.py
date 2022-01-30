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


#making multiple instances from the class
my_restaurant = Restaurant('Rose', 'Indian')
your_restaurant = Restaurant('Lily', 'Thai')
his_restaurant = Restaurant('Boston Pizza', 'Pizza')

#calling method
my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
his_restaurant.describe_restaurant()

my_restaurant.open_restaurant()

# directly change the attributes value
my_restaurant.number_served = 10
my_restaurant.count_customers_served()

# change attributes value through a method
my_restaurant.update_customers_served(15)
my_restaurant.count_customers_served()

# change attributes value through a method
my_restaurant.increment_customers_served(25)
my_restaurant.count_customers_served()


#accessing the attributes
print(f"{my_restaurant.name} serves {my_restaurant.cuisine} food")

