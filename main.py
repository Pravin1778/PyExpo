import random
print("welcome to number guessing game!!")
number_guess=random.randrange(100)
chances=6
guess_counter=0
while guess_counter<chances:
    guess_counter+=1
    my_guess=int(input("enter your guess number:"))
    if my_guess==number_guess:
        print(f'the number is {number_guess} and you found it right!! in the {guess_counter} attempts')
        break
    elif guess_counter >= chances and my_guess != number_guess:
        print(f'Oops sorry, The number is {number_guess} better luck next time')
    elif my_guess > number_guess:
        print('Your guess is higher')
    elif my_guess < number_guess:
        print('Your guess is lesser')
