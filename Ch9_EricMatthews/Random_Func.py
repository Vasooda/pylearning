
def roll_die(min, max):
    print("Rolling dice...")
    number = random.randint(min, max)
    print(f"Your dice rolled:{number}")
roll_die(1,6)

  

value = random.random()
print(value)

print("--------------------")

#random floating point value
value = random.uniform(1,10)
print(value)

print("--------------------")

#random integer value
value = random.randint(1,6)
print(value)

print("--------------------")

#random choice from list
greetings =  ['hello', 'hi','bye','yo','howdy','aloha','namaste']

value = random.choice(greetings)
print(value + ',Vasooda!' )


#random choice selected from list with equal probabilty that each will be selected, use k value (how many times we want to pick the value)
colors = ['red', 'black','green']

results = random.choices(colors,k=10)
print(results)

print("--------------------")

#roulette you can weight the choices based on probability
colors = ['red', 'black','green']

results = random.choices(colors,weights=[18,18,2], k=10)
print(results)

print("--------------------")

#shuffle choices -- i.e shuffle a deck of cards

deck = list(range(1,53)) #53 non inclusive
random.shuffle(deck)
print(deck)

print("--------------------")
#use sample method to sample a specified set from the range i.e. a hand from a deck of cards
deck = list(range(1,53)) #53 non inclusive
hand = random.sample(deck, k=5)
print(hand)

print("--------------------")
