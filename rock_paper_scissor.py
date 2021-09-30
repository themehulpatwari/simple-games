import random

def convert(a):
    if a == 1:
        a = 'rock'
    elif a == 2:
        a = 'paper'
    else:
        a = 'scissor'
    return a

user_count = 0
machine_count = 0
tie_count = 0
list1 = ['rock','paper','scissor']


print('1.Rock\n2.Paper\n3.Scissor')
print('To stop playing press 0')

user = int(input('\nWhat do you choose\nRock or Paper or Scissor: '))

while user != 0:
    user = convert(user)
    machine = random.choice(list1)
    if user == machine:
        print('Tie, you both chose {}'.format(user))
        tie_count += 1
    else:
        if user == 'rock':
            if machine == 'scissor':
                print('You win!! you = {}, machine = {}'.format(user,machine))
                user_count += 1
            else:
                print('You lose you = {}, machine = {}'.format(user,machine))
                machine_count += 1
        if user == 'paper':
            if machine == 'rock':
                print('You win!! you = {}, machine = {}'.format(user,machine))
                user_count += 1
            else:
                print('You lose you = {}, machine = {}'.format(user,machine))
                machine_count += 1
        if user == 'scissor':
            if machine == 'paper':
                print('You win!! you = {}, machine = {}'.format(user,machine))
                user_count += 1
            else:
                print('You lose you = {}, machine = {}'.format(user,machine))
                machine_count += 1
    user = int(input('\nWhat do you choose\nRock or Paper or Scissor: '))


print()
print('No of times you won =',user_count)
print('No of times machine won =',machine_count)
print('No of times you both tied =',tie_count)



