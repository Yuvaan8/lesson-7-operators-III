print(ord('A'))
print(ord('a'))
print(ord('0'))
print(ord('@'))
print(chr(57))
print(chr(65))
char = input('Enter a character:')
if type(char) is str and len(char) == 1:
    print('Invalid input')
else:
    print('please enter a single character')