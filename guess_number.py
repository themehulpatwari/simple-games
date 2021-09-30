import random
import math

lower = int(input('Lower Range: '))
upper = int(input('Upper Range: '))

number = random.randint(lower,upper)
tries = round(math.log(upper-lower + 1, 2))
print('You have {} chance to guess the number'.format(tries))
count = 0

while count<tries:
    user_input = int(input("What's your guess: "))
    count += 1
    if user_input == number:
        print('Congrats you found the number in {} try'.format(count))
        break
    elif number>user_input:
        print('Your guess is LOW, try higher')
    elif number<user_input:
        print('Your guess is HIGH, try lower')
else:
    if count>=tries:
        print()
        print('The number is',number)
        print('Better luck next time')



