#PARENT CLASS

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

#CHILD CLASS

class Admin(Users):
  def __init__(self,first_name,last_name,id_number,login_attempts):
    super().__init__(first_name,last_name,id_number,login_attempts)
    self.privileges = []

  def show_privileges(self):
    print(f"Here is a list of admin priviledges you have access too:")
    for privileges in self.privileges:
        print(f"-{privileges.title()}")

  
currentuser = Admin('bugs','bunny','321','3')
currentuser.privileges = ['change password','change privacy settings','change date format']

print(currentuser.describe_user())
currentuser.show_privileges()

