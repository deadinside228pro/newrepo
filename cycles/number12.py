a=int(input('введите а '))
b=int(input('введите b '))
c=b
d=False
if a>0 and b>0:
    while a>0:
        p=a%10
        while c>0:
            t=c%10
            if t==p:
                d=True
            c=c//10
        c=b
        a=a//10
    if d==False:
        print('НЕТ')
    else:
        print("ДА")
if a<0 and b<0:
    a=a*(-1)
    c=b*(-1)
    while a > 0:
        p = a % 10
        while c > 0:
            t = c % 10
            if t == p:
                d = True
            c = c // 10
        c = b
        a = a // 10
    if d == False:
        print('НЕТ')
    else:
        print("ДА")
if a>0 and b<0:
    c=b*(-1)
    while a > 0:
        p = a % 10
        while c > 0:
            t = c % 10
            if t == p:
                d = True
            c = c // 10
        c = b
        a = a // 10
    if d == False:
        print('НЕТ')
    else:
        print("ДА")
if a<0 and b>0:
    a=a*(-1)
    while a > 0:
        p = a % 10
        while c > 0:
            t = c % 10
            if t == p:
                d = True
            c = c // 10
        c = b
        a = a // 10
    if d == False:
        print('НЕТ')
    else:
        print("ДА")
else:
    print('ДА')