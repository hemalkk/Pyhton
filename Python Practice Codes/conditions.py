a=10
b=1
print(a==b)
print(a!=b)

minMark=30
mark=float(input('Enter your mark: '))

if mark>=minMark:
    print('Pass')
elif mark>=25:
    print('Wait')
else:
    print('Fail')