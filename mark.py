print('Enter the marks obtained in 5 subjects:')
MarkOne = int(input())
MarkTwo = int(input())
MarkThree = int(input())
MarkFour = int(input())
MarkFive = int(input())
tot = MarkOne + MarkTwo + MarkThree + MarkFour + MarkFive
avg = int(tot / 5)
Validrange = range(0, 101)
if avg not in Validrange:
    print('Invalid input!')
elif avg in range(91, 101):
    print('Grade = A1')
elif avg in range(81, 91):
    print('Grade = A2')
elif avg in range(71, 81):
    print('Grade = B1')
