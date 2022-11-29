print("ax^2 + bx + с = 0")
def findRootsOfFunctions(a=float(input("введите коэффициент а ")),b=float(input("введите коэффициент b ")),c=float(input("введите коэффициент с "))):
    diss=(b**2)+(-4*a*c)
    if diss>0:
        print("дискриминант =",diss)
        x1=(-b+(diss**0.5 ))/(2*a)
        x2=(-b-(diss**0.5 ))/(2*a)
        res1=('первый корень =',x1)
        res2=('второй корень =',x2)
        return res1,res2
    elif diss == 0:
        res1=('всего есть 1 корень; корень равен =',-b/(2*a))
        return res1
    elif diss<0:
        res1="корней нет"
        return res1
print(findRootsOfFunctions())

