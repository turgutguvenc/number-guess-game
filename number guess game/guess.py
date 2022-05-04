# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:21:11 2022

@author: turgu
"""

from art import logo
from functions import difficulty, compare
import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thiking of a number between 1 and 100.") 




random_number = random.randint(1,100)

attempt = difficulty()
print(f"outer attempt {attempt}")
while attempt > 0:
  guess = int(input("Make a guess"))

  if guess == random_number:
      print(f"You win the correct answer is {random_number}")
      break
  attempt = compare(guess, random_number, attempt)
  
  print(f"inner attempt {attempt}")
  
  if attempt == 0:
    print("you have no right to try ")
    print(f'the correct answer is {random_number}')
    