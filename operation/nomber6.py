def findDifferenceBiggerNumberWithSmallerNomber(a=float(input('число а ')),b=float(input('число b '))):
    if a>b:
        res=a-b
    elif a<b:
        res=b-a
    else:
        res='они одинаковые'
    return res
print(findDifferenceBiggerNumberWithSmallerNomber())