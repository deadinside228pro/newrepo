n = int(input('введите n '))
a = 1
b = 1
case = 0
if n<=2:
    print(a)
else:
    print(a, b, end=' ')
    for i in range(0,n-2):
        case=a
        a=b
        b=b+case
        print(b, end=" ")


