class Users:
  def __init__(self,first_name,last_name,id_number, login_attempts):
    self.first_name = first_name
    self.last_name = last_name
    self.id_number = id_number
    self.login_attempts = 0
  
  def describe_user(self):
    print(f"User name:{self.first_name} {self.last_name}")
    print(f"User id: {self.id_number}")
    print(f"Login attempts: {self.login_attempts}")

  def greet_user(self):
    print(f"Hello {self.first_name}! Welcome to your user profile. Please find your profile details below")

  def increment_login_attempts(self):
      self.login_attempts += 1
  
  def reset_login_attempts(self):
    self.login_attempts = 0
    
#made multiple instances from the class users
firstuser = Users('John', 'Doe', '1234', '0')
seconduser = Users('Jane', 'Doe', '1432','1')
thirduser = Users('Mya', 'Doe', '1324','2')

#calling the methods defined within the class users
thirduser.greet_user()
thirduser.describe_user()

thirduser.increment_login_attempts()
thirduser.increment_login_attempts()
thirduser.increment_login_attempts()

print(f"Login attempts: {thirduser.login_attempts}")

thirduser.reset_login_attempts()

print(f"Updated login attempts: {thirduser.login_attempts}")
