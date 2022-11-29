a = int(input('введите а '))
b=0
if a>0:
    while a != 0:
        i=a%10
        b=b*10
        b=b+i
        a=(a//10)
        print(a,'',end='')
    print(sep='')
    print(b)
elif a<0:
    a=a*(-1)
    while a != 0:
        i=a%10
        b=b*10
        b=b+i
        a=(a//10)
        print(a,'',end='')
    print(sep='')
    print('-',b)



