# GUESS THE NUMBER WITH THE LESS THAN 5 NUMBER OF TRIES :

guess = 0
tries = 0
while guess != 6 and tries < 5:
    guess = int(input("guess the number: "))
    tries = tries+1

if guess != 6:
    print('you ran out of the tries')
else:
    print('you got it!')
    
    
    
# STONE,PAPER,SCISSOR GAME:

import random
options = ('rock', 'paper', 'scissor')
player = None
computer = random.choice(options)
while player not in options:
    player = input('Enter a choice(rock,paper,scissor): ')

print(f'player: {player}')
print(f'computer: {computer}')

if player == computer:
    print('Its a tie!')
elif player == 'rock' and computer == 'scissor':
    print('You win')
elif player == 'paper' and computer == 'rock':
    print('You win')
elif player == 'scissor' and computer == 'paper':
    print('You win')
else:
    print('You lose')


# PYTHON NUMBER GUESSING NAME

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True


print('python number guessing game')
print(f'select a number between {lowest_num} and {highest_num}')

while is_running:
    guess = input('Enter your guess: ')

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print('That number is out of range')
            print(
                f'please select a number between {lowest_num} and {highest_num}')
        elif guess < answer:
            print('Too low!Try again')
        elif guess > answer:
            print('Too high!Try again')
        else:
            print(f'CORRECT! The answer was {answer}')
            print(f'Number of guesses: {guesses}')
            is_running = False
    else:
        print('Invalid guess')
        print(f'please select a number between {lowest_num} and {highest_num}')