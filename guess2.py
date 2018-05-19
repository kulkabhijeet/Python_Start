

















































guess = 10
result = False
lower = 0
higher = 100

from random import randint

for i in range(1, 11):
    comp_num = randint(lower, higher)
    print('Is your number ' , comp_num)
    resp = input('''Say HIGH if my number is HIGH.
Say LOW if my number is LOW.
Say CORRECT if I am correct:  ''')
                    

    if resp.upper() == 'HIGH':
        higher = comp_num  

    if resp.upper() == 'LOW':
        lower = comp_num

    if resp.upper() == 'CORRECT':
        result = True
        print('Yey !! I WIN !!!')
        break
    print('I have ' , 10-i , ' left')


if result == False:
    print('Urghh. I lose')

        

    
           
          

    
