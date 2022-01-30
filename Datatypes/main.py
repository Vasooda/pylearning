
#can change the item in a list at its index
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print(fruits)


#a string in immutable so you need to slice a string 
sentence = "i like big butts"
#sentence[0] = "u"
print("u" + sentence[1::])


fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]

fruits.update(more_fruits)
print(fruits

#car =	{  "brand": "Ford",
  #"model": "Mustang",
 # "year": 1964}
#print(car.get("model")
)

#adding numbers
def list_of_numbers(nums):
  total = 0
  for item in nums:
    total += item
  return total

nums = [1,2,3,4]
print(list_of_numbers(nums))


#return words that start with a vowel

li = []
def words_with_vowels(words):
  for item in words:
    if item[0] in 'aeiou':
      li.append(item)
  return li

words = ['hello', 'i','am','ollie']

print(words_with_vowels(words))

#find locaiton of even numbers


def location_of_even_numbers(numlist):
  evenslocation = []

  for item in range(len(numlist)):
    if numlist[item] % 2 == 0:
      evenslocation.append(item)
  return evenslocation

numlist = [1,2,3,4]

print(location_of_even_numbers(numlist))

newlist = []
def even_numbers(li):
  for item in range(len(li)):
    if li[item] % 2 == 0:
      
      newlist.append(item)
  return newlist

li = [1,2,3,4]

print(even_numbers(li))

#find the longest word

def longest_word(letters):
  longword = ''

  for item in letters:
    if len(item) > len(longword):
      longword = item
  return longword

letters = ['ollie','is','a', 'friendly', 'pup']

print(longest_word(letters))


#more evens and odds

def evens_or_odds(numbers):
  count_evens = 0
  count_odds = 0

  for item in numbers:
    if item % 2 == 0:
      count_evens += count_evens + 1
    else:
      count_odds += count_odds + 1

    
  if count_evens > count_odds:
    return 'evens'
  elif count_evens < count_odds:
    return 'odds'
  else:
    return 'evens and odds'

numbers = [1,2,3,4,5,6,7,8]

print(evens_or_odds(numbers))


#song selection 

#date = input ('What the date today?')

def song_selection():
  temprature = ''
  workout = ''

  weather = int(input('What the weather like today in your neighbourhood?')) 
  exercise = bool(input('Did you exercise today?True or False?'))

  if weather > 70:
    temprature = 'Sunny!'
  elif weather > 50:
    temprature = 'Moderate'
  else:
    temprature = 'Mild'
    return temprature

  if exercise == "True":
    return 'True'
  else:
    return 'False'

print(song_selection())


    


