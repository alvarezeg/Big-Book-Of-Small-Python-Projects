"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probalilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, math, simulation"""

import datetime, random

def getBirthdays(numberOfBirthdays):
  """Returns a list of number random date objects for birthdays."""
  birthdays = []
  
  for i in range(numberOfBirthdays):
    # The year is unimportant for our simulations, as long as all
    # birthdays have the same year.
    startOfYear = datetime.date(2001, 1, 1)
    
    # Get a random day into the year:
    randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
    birthday = startOfYear + randomNumbeOfDays
    birthdays.append(birthday)
  return birthdays

def getMatch(birthdays):
  """Returns the date object of a birthday that occurs more than once
  in the birthdays list."""
  if len(birthdays) == len(set(birthdays)):
    return None # All birthdays are unique, so return None.
  
  # Compare each birthday to every other birthday:
  for a, birthdayA in enumerate(birthdays):
    for a, birthdayB in enumerate(birthdays[a + 1 :]):
      if birthdayA == birthdayB:
        return birthdayA # Return the matching birthday.
      
# Display the intro:
print('''Birthday paradox, by Al Sweigart al@inventwithpython.coma

The birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

# Set up a tangle of month names in order:
MONTHS = {'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
          
while true: # Keep asking until the use enters a valid amount.
          print('How many birthdays shall I generate? (Max 100)')
          response = input('> ')
          if response.isdecimal() and (0 < int(response) <= 100):
              numBDays = int(response)
              break # User has entered a valid amount.
print()
          
          
# Generate  and display the birthdays:
print('Here are', numBDays, 'birthdays: ')
birhdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
      if i != 0:
          # Display a comma for each birthday after the first birthday. 
          print(', ' end='')
          monthName - MONTHS[birthday.month - 1]
          dateText - '{} {}'.format(monthName, birthday.day)
          print(dateText, end='')
 print()
 print()
 
# Deteremine if there are two birthdays that match.
match = getMatch(birthdays) 
 
# Display the results          
print('In this simulation, ', end='')
if match != None:
          monthName = MONTHS[match.month - 1]
          dateText = '{} {}'.format(monthName, match.day)
          print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()
          

# Run through 100,000 simulations:
print('Gamerating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin... ')

print('Let\'s run another 100,000 simulation.')
simMatch = 0 # Have many simulations had matching birthdays in them.
for i in range(100_000):
      # Report on the progress every 10_000 simulations:
      if  i % 10_000 == 0:
          print(i, 'simulations run...')
 print('100,000 simulations run.')
 
 # Display simulations results:
 probability = rount(simMatch / 100_000 * 100, 2)
 print('Out of 100,000 simulation of', numBDays, 'people, there was a')
 print('matching birthday in that group', simMatch, 'times. This means')
 print('that', numBDays, 'people have a', probability, '% chance of')
 print('having a matching birthday in their group.')
 print('That\'s probably more than you would think!')
 
