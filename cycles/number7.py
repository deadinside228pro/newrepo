a = int(input(''))
b = int(input(''))
while a != b:
    if a>b:
        a=a-b
        print(a,'',b)
    elif b>a:
        b=b-a
        print(a,"",b)