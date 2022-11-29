def findQuarterWhereDot(x=float(input("координата х ")),y=float(input("координата y "))):
    if x>0 and y>0:
        res="в 1-ой четверти"
    elif x>0 and y<0:
        res="в 4-ой четверти"
    elif x<0 and y>0:
        res=("во 2-ой четверти")
    elif x<0 and y<0:
        res=("в 3-ей четверти")
    elif x==0 and y!=0:
        res=("на оси y")
    elif x!=0 and y==0:
        res=("на оси х")
    else:
        res=("точка в начале координат")
    return res
