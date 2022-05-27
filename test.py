import random

print("Welcome to the Estimator!")

a =  input("How many times do you want to guess? ")
b = input("How long is your max random number? (default 10) ")
random_number = random.randint(1, int(b))
false_amount = int(a)
debug_mode = False
#If you are a player and you found this option, you can see the number. Only use it for debugging and remastering.
if debug_mode == True:
    print("Debug mode is on, don't abuse it a lot.")
    print("Random number is:", random_number)
else:
    print("Debug mode is off.")
while True:
    guess = int(input("Guess the number: "))
    if guess == random_number:
        print("You win!")
        break
    else:
        false_amount += 1
        if guess > random_number:
            print("Too high.")
        else:
            print("Too low.")
        
        if false_amount == 3:
            print("You lose! The number was", random_number)
            break

#Credits:
#Github CoPilot
#RobloxianCoder

#Copyright © 2020, Esteban A. Pardo
#All rights reserved.
#This code is under GNU General Public License v3.0.
#You can find the license here: https://www.gnu.org/licenses/gpl-3.0.en.html
#You can find the source code here:
#URL: https://www.github.com
#Github:
#Github CoPilot: https://www.github.com/copilot
#Github RobloxianCoder: https://www.github.com/RobloxianCoder