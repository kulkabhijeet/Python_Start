string = input('Enter a string :  ')

output = {}
for each in string :
    if each in output:
        output[each] = output[each] + 1
    else:
        output[each] = 1
print(output)
