def getNumbersInAscendingOrder(a=float(input("число а ")),b=float(input("число b ")),c=float(input("число с "))):
    if a>b>c or a==b and a>c or a>b and b==c:
        res=c,b,a
    elif a>c>b:
        res=b, c, a
    elif b>a>c or a==c and b>a or b==a and b>c:
        res=c, a, b
    elif b>c>a or b==c and b>a:
        res=a,c, b
    elif c>a>b or c>b and a==b or c>b and c==a:
        res=b,a,c
    elif c>b>a:
        res=a,b,c
    else:
        res="они одинаковые ",a,b,c
    return res
print(getNumbersInAscendingOrder())