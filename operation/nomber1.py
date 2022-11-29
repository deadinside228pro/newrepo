def baseOperationsWithNombers(a,b):
    if a>b:
        res=a+b
    elif a==b:
        res=a*b
    else:
        res=a-b
    return res
print(baseOperationsWithNombers())