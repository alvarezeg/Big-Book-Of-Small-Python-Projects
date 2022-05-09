"""Caesor Cipher Hacker, by Al Sweigart al@inventwithpython.com 
This program hacks messages encrypted with the Caesar Cipher by doing 
a brute force attack against every possible key.
More info at:
https://en.wikipedia.org/wiki/Caesar_Cipher#Breaking_the_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, cryptography, math"""

print('Caesar Cipher Hacker, by Al Sweigart al@iventwithpython.com')

# Let the user specify the message to hack:
print('Enter the encrypted Caesar Cipher message to hack')
message - input('> ')

# Every possible symbol that can be encrypted/decrypted:
# (This must match the SYMBOLS used when encrypting the emssage.)
SYMBOLS = 'ABCDEFHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)): # Loop through every possible key.
  translated = ''
  
  # Decrypted each symbol in the message:
  for symbol in message:
    if symbol in SYMBOLS:
      num = SYMBOLS.find(symbol) # Get the number of the symbol
      num = num - key # Decrypt the number
      
      # Hanlde the wrap-around if num is less than o:
      if num < O:
        num = num + len(SYMBOLS)
        
      # Add decypted number's symbol to translated:
      translated += SYMBOLS[num]
  else:
     # Just add the symbol without decrypting:
      translated += symbol
      
# Display the key being tested, along with its decrypted text:
print('Key #{}: {}'.format(key, translated))
