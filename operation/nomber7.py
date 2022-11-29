def findNumberInInteval(a=float(input('число а '))):
    if a>=0 and a<= 10:
        res='подходит'
    elif a>=20 and a<=30:
        res='подходит'
    elif a>=40 and a<=50:
        res='подходит'
    else:
        res='не подходит'
    return res
print(findNumberInInteval())
