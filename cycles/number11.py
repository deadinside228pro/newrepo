a=int(input('введите а '))
b=int(input('введите  b '))
sum1=0
sum2=0
if a<b:
    for i in range(a,b+1):
        r=i
        while r != 0:
            h=r%10
            j=h%2
            if j==0:
                sum1+=h
            else:
                sum2+=h
            r=r//10
        if sum1>sum2:
            print(i)
            sum1=0
            sum2=0
        else:
            sum1=0
            sum2=0
elif a>b:
    for i in range(a,b-1, -1):
        r=i
        while r != 0:
            h=r%10
            j=h%2
            if j==0:
                sum1+=h
            else:
                sum2+=h
            r=r//10
        if sum1>sum2:
            print(i)
            sum1=0
            sum2=0
        else:
            sum1=0
            sum2=0
