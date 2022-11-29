def isAmountOfTwoNumbersBiggerThanThirdNumber(a=float(input('введите число а ')),b=float(input('введите число b ')),c=float(input('введите число c '))):
    if a+b>c and a+c>b and b+c>a:
        res='все нормально'
    else:
        res='не подходит'
    return res
print(isAmountOfTwoNumbersBiggerThanThirdNumber())