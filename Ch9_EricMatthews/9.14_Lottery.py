import random

class Lottery:
  def __init__(self,ticket):
    self.ticket = ticket

  def ticket_selection(self):
    ticket_values = [1,2,3,4,56,7,8,9,10,'a','b','c','d','e']
    winning_ticket = random.sample(ticket_values,k=4)
    #winning_ticket = random.sample(ticket,k=4)
    print(winning_ticket)


winner = Lottery('test')
winner.ticket_selection()