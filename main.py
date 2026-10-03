# Project Question
# Create a Number Guessing Game in Python.
# The computer should generate a random number within a specified range, and the user has to guess the
# number.
# The program should give hints after every incorrect guess and continue until the user guesses the correct
# number.
# Part 1- Basic Version
# The computer should generate a random number between 1 and 100
# Ask the user to enter a guess.
# For every guess:
# • If the guess is greater than the secret number, print:
# Too high!
# • If the guess is smaller than the secret number, print:
# Too low!
# • If the guess is equal to the secret number, print:
# Congratulations! You guessed the number
# The program should continue asking for guesses unti' the user gets the correct answer

# import random
# ran_num_guess = random.randint(1, 10)
# while True:
#         a = int(input("Guess the num between "))
#         # ran_num_guess = random.randrange(1, 10)
#         # ran_num_guess = random.randint(1, 10)
#         # print(ran_num_guess)
#         print(ran_num_guess)

#         if(a==ran_num_guess):
#             print("Congratulations! You guessed the number")
#         elif(a>ran_num_guess):
#             print("Too high!")
#         elif(a<ran_num_guess):
#             print("Too low")

# 2.Part 2- Count Attempts
# Modify the program so that it counts how many attempts the user needed.
# Example:
# Congratulations! You guessed the number
# The number was: 73
# Attempts: 6
# Requirement
# Create a variable such as:
# attempts
# and increase it after every guess.


# import random
# ran_num_guess = random.randint(1, 10)
# attempts = 0
# while True:
#         a = int(input("Guess the num between "))
#         # print(ran_num_guess)

#         if(a==ran_num_guess):
#             print("Congratulations! You guessed the number")
#             print("The number is: ",ran_num_guess)
#             print("Attempts= ",attempts)
#             break
#         elif(a>ran_num_guess):
#             print("Too high!")
#         elif(a<ran_num_guess):
#             print("Too low")
#         attempts = attempts+1
#         print("Attempts= ",attempts)

# 3.Part 3- Create Functions
# Now restructure your program using functions
# You should have at least:
# generate_number ()
# get_guess ()
# check_guess()
# play_game()
# Your main program should eventually look conceptually like:
# play_game()
# instead of putting everything directly in the main code.

# def generate_num(n):
#     while True:
#         get_guess = 
            

# Part 4 - Difficulty Levels
# Add a difficulty selection.
# When the game starts:
# NUMBER GUESSING GAME
# = ==
# H==s
# Select Difficulty:
# 1. Easy
# 2. Medium
# 3. Hard
# Enter your choice:

# print("====NUMBER GUESSING GAME===")
# print("Select Difficulty: 1\nEasy \n2.Medium \n3.Hard")

# difficulty = int(input("Enter the Difficulty"))

# import random
# # ran_num_guess = random.randint(1, 10)
# attempts = 0


# match difficulty:
#     case 1:
#         ran_num_guess = random.randint(1, 10)
#         while True:
#             a = int(input("Guess the num between "))
#             print(ran_num_guess)

#             if(a==ran_num_guess):
#                 print("Congratulations! You guessed the number")
#                 print("The number is: ",ran_num_guess)
#                 print("Attempts= ",attempts)
#                 break
#             elif(a>ran_num_guess):
#                 print("Too high!")
#             elif(a<ran_num_guess):
#                 print("Too low")
#             attempts = attempts+1
#             print("Attempts= ",attempts)
#             # print("Print Easy.")

#     case 2:
#         ran_num_guess = random.randint(1, 50)
#         # print(ran_num_guess)
#         while True:
#                     attempts = 0
#                     for attempts in range(0,10):
#                         a = int(input("Guess the num between "))
#                         print(ran_num_guess)
            
#                         if(a==ran_num_guess):
#                             print("Congratulations! You guessed the number")
#                             print("The number is: ",ran_num_guess)
#                             print("Attempts= ",attempts)
#                             break
#                         elif(a>ran_num_guess):
#                             print("Too high!")
#                         elif(a<ran_num_guess):
#                             print("Too low")
#                         attempts = attempts+1
#                         attempts == 11
#                         print("Attempts= ",attempts)
#                     break
#         print("Your 10 attempts finished")
#                     # break
                    
                    
#         # print("Print Medium.")

#     case 3:
#         ran_num_guess = random.randint(1, 500)
#         print(ran_num_guess)
#         while True:
#                     attempts = 0
#                     for attempts in range(0,7):
#                     #   ran_num_guess = random.randint(1, 100)
#                         a = int(input("Guess the num between "))
#                         # print(ran_num_guess)
            
#                         if(a==ran_num_guess):
#                             print("Congratulations! You guessed the number")
#                             print("The number is: ",ran_num_guess)
#                             print("Attempts= ",attempts)
#                             break
#                         elif(a>ran_num_guess):
#                             print("Too high!")
#                         elif(a<ran_num_guess):
#                             print("Too low")
#                         attempts = attempts+1
#                         print("Attempts= ",attempts)
#                         print("Remaining attempts:", 7 - attempts)
#                     break
#         print("Game Over!")
#         print("You used all your atempts")
#         print("The correct num was", ran_num_guess)



# Part 6- Input Validation
# Now make your program handle invalid input.
# For example:
# Guess a number: abc
# Invalid input!
# Please enter a number.
# Also handle numbers outside the allowed range:
# Guess a number between 1 and 100: 150
# Invalid guess!
# Please enter a number between 1 and 100
# Challenge
# Don't let invalid input consume an attempt.

# import random

# guess_num = random.randint(1,100)
# print(guess_num)
# while True:
#     try:
#         a = int(input("Please Enter a number:" ))
#         if(a == guess_num):
#             print("Congrates")
#         elif a > 100:
#             print("Invalid Guess")
#             print("Please enter a number between 1 and 100")
#         else:
#             print("Better luck next time")

#     except:
#         print("Invalid input")


