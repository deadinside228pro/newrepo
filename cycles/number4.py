a=int(input('vvedite a '))
max=0
i=1
while i != a:
    if a>i:
        if a%i==0:
            if i>max:
                max=i
        i+=1
    elif i>a:
        a=a*(-1)
        while i != a:
            if a % i == 0:
                if i > max:
                    max = i
            i+=1
print(max)