import random

the_correct_nr = random.randint(1, 101)

while True:
    response = input('Guess a nr between 1 & 100 > ')

    try:
        res = int(response)
    except:
        print(f'No you nitwit "{response}" is not a number.')
        continue

    if res < the_correct_nr:
        print('Too low!')
    elif res > the_correct_nr:
        print('Too high!')
    else:
        print('Yes, you would appear to be right. The nr is: ' + response)
        break
