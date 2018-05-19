guess = 10
















































our_num = 42
result = False

for i in range(1,11):
    your_num = int(input('Enter the number: '))

    if your_num == our_num:
        print('You are correct')
        result = True
        break

    elif your_num > our_num:
        print('You are higher. Go Lower')
        print('You have ' , guess - i , ' left')
        print()

    elif your_num < our_num:
        print('You are lower. Go high')
        print('You have ' , guess - i , ' left')
        print()

if result == False:
    print('You lose. All your guesses are done')
        
