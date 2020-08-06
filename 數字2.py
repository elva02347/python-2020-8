  
import random
a = 1
b = 100
number = random.randint(a,b)

while True:
    print('now=%d-%d'%(a,b))
    guess = int(input('fill in you number from 1~100:'))
    if guess < a or guess > b:
        print ('fill in your number again!')
    elif guess > number :
        b = guess
    elif guess < number:
        a = guess
    elif guess == number:
        print(number)
        print('you are right!!')
        break