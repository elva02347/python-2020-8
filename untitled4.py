import random
number = random.randint(1,10)
while True:
    guess = int(input('fill in your number from one to ten:'))
    if number == guess:
        print('you are right!!')
        print(number)
        break
    else:
        print('you are wrong~~, keep trying.')
