# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:35:39 2022

@author: turgu
"""

def difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard:'").lower()
    
    if difficulty == "hard":
      return 10
    else:
      return 5


def compare(guess, random_number, attempt):


  if (guess > random_number) and ((guess - random_number) > 50):
    print("too_high")
    return attempt - 1
  elif (guess > random_number) and ((guess - random_number) < 50):
    print("high")
    return attempt - 1
  elif (guess < random_number) and (abs((guess - random_number)) > 50):
    print("too_low")
    return attempt - 1
  elif (guess < random_number) and (abs((guess - random_number)) < 50):
    print("low")
    return attempt - 1