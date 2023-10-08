import random
import time

print('Start')
number = random.randint(1,100)
i = 11
while True:
    i = i-1
    print('')
    print('Your chance is equal to: {}'.format(i))
    #print('')
    x = int(input('Enter a number between 1 and 100: '))
    print('')
    if i == 1:
        print('Game over')
        break

    elif x == number:
        print('your win')
        break

    elif x < number:
        print('Try a larger number')


    elif x > number:
        print('Try a smaller number')


    

    
    
    
time.sleep(20)
