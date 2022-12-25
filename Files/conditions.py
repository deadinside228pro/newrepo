def baseOperationsWithNombers(a, b):
    if a > b:
        res = a + b
    elif a == b:
        res = a * b
    else:
        res = a - b
    return res


def findQuarter(x, y):
    if x > 0 and y > 0:
        res = 1
    elif x > 0 and y < 0:
        res = 4
    elif x < 0 and y > 0:
        res = 2
    elif x < 0 and y < 0:
        res = 3
    elif x == 0 and y != 0:
        res = "на оси y"
    elif x != 0 and y == 0:
        res = "на оси х"
    else:
        res = "точка в начале координат"
    return res


def getNumbersInAscendingOrder(a, b, c):
    if a > b > c or a == b and a > c or a > b and b == c:
        res = c, b, a
    elif a > c > b:
        res = b, c, a
    elif b > a > c or a == c and b > a or b == a and b > c:
        res = c, a, b
    elif b > c > a or b == c and b > a:
        res = a, c, b
    elif c > a > b or c > b and a == b or c > b and c == a:
        res = b, a, c
    elif c > b > a:
        res = a, b, c
    else:
        res = "они одинаковые ", a, b, c
    return res


def getRoots(a, b, c):
    diss = (b ** 2) + (-4 * a * c)
    l1=[]
    if a == 0:
        return "это не квадратное уравнение"
    elif diss > 0:
        x1 = (-b + (diss ** 0.5)) / (2 * a)
        x2 = (-b - (diss ** 0.5)) / (2 * a)
        l1.append(x1)
        l1.append(x2)
        return l1
    elif diss == 0:
        res1 = -b / (2 * a)
        return res1
    elif diss < 0:
        res1 = "корней нет"
        return res1


def writeNumberInWord(a):
    l1 = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'восемьедесят', 'семьдесят',
          'девяносто']
    l2 = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    l3 = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
          'восемнадцать', 'девятнадцать', ]
    if a > 10 and a < 20:
        return l3[a - 10]
    else:
        decade = l1[a // 10]
        unit = l2[a % 10]
        return decade, unit


def findDifferenceBiggestNumberWithSmallestNomber(a, b):
    if a > b:
        res = a - b
    elif a < b:
        res = b - a
    else:
        res = 'они одинаковые'
    return res


def findNumberInInterval(a):
    if a >= 0 and a <= 10:
        res = 'подходит'
    elif a >= 20 and a <= 30:
        res = 'подходит'
    elif a >= 40 and a <= 50:
        res = 'подходит'
    else:
        res = 'не подходит'
    return res


def isAmountOfTwoNumbersBiggerThanThirdNumber(a, b, c):
    return a + b > c and a + c > b and b + c > a



