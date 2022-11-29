def raiseToADegree(a, b):
    return a ** b


def writeNumbersWhichDividedIntoA(a):
    numbers = []
    for i in range(1, 1001):
        if i % a == 0:
            numbers.append(i)
    return numbers


def findCountOfNumbersWhoseSquareLessThanA(a):
    k = 0
    for i in range(1, a):
        if i**2 < a:
            k += 1
    return k


def findGreatestDividerOfA(a):
    max = 0
    i = 1
    while i != a:
        if a > i:
            if a % i == 0:
                if i > max:
                    max = i
            i += 1
        elif i > a:
            a = a * (-1)
            while i != a:
                if a % i == 0:
                    if i > max:
                        max = i
                i += 1
    return max


def getAmountOfNumbersFromAToBWhichAreDivisibleBy7Entirely(a, b):
    sum = 0
    if a > b:
        for i in range(a, b - 1, -1):
            if i % 7 == 0:
                sum = sum + i
        return sum
    elif a < b:
        for i in range(a, b + 1):
            if i % 7 == 0:
                sum = sum + i
        return sum
    else:
        return sum


def getNumberOfFibonachi(n):
    a = 1
    b = 1
    case = 0
    if n <= 2:
        return a
    else:
        for i in range(0, n - 2):
            case = a
            a = b
            b = b + case
        return b


def doAlgorithmOfEvklid(a, b):
    while a != b:
        if a > b:
            a = a - b
        elif b > a:
            b = b - a
    return a, b


def doMethodOfHalfDivision(a):
    l = 0
    r = a
    if (((r - l) // 2) ** 3) == a:
        return r // 2
    while not (((r - l) // 2) ** 3) == a:
        if (((r - l) // 2) ** 3) > a:
            r = r // 2
        elif (((r - l) // 2) ** 3) < a:
            l = r / 2
    return (r - l) // 2


def findquantityOfOddDiggit(a):
    k = 0
    if a > 0:
        while a != 0:
            i = a % 10
            if i % 2 != 0:
                k += 1
            a = a // 10
    elif a < 0:
        while a != 0:
            i = a % 10
            if i % 2 != 0:
                k += 1
            a = (a // 10) + 1
    return k


def reverseNumber(a):
    b = 0
    if a > 0:
        while a != 0:
            i = a % 10
            b = b * 10
            b = b + i
            a = (a // 10)
        return b
    elif a < 0:
        a = a * (-1)
        while a != 0:
            i = a % 10
            b = b * 10
            b = b + i
            a = (a // 10)
        return b


def getNumberFromAToBWhichEvenDigitsGreatestThanOddDiggits(a, b):
    l1 = []
    sum1 = 0
    sum2 = 0
    if a < b:
        for i in range(a, b + 1):
            r = i
            while r != 0:
                h = r % 10
                j = h % 2
                if j == 0:
                    sum1 += h
                else:
                    sum2 += h
                r = r // 10
            if sum1 > sum2:
                l1.append(i)
                sum1 = 0
                sum2 = 0
            else:
                sum1 = 0
                sum2 = 0
    elif a > b:
        for i in range(a, b - 1, -1):
            r = i
            while r != 0:
                h = r % 10
                j = h % 2
                if j == 0:
                    sum1 += h
                else:
                    sum2 += h
                r = r // 10
            if sum1 > sum2:
                l1.append(i)
                sum1 = 0
                sum2 = 0
            else:
                sum1 = 0
                sum2 = 0
    return l1


def findNumbersWithSameDigits(a, b):
    c = b
    d = False
    if a > 0 and b > 0:
        while a > 0:
            p = a % 10
            while c > 0:
                t = c % 10
                if t == p:
                    d = True
                c = c // 10
            c = b
            a = a // 10
        if d == False:
            return 'НЕТ'
        else:
            return "ДА"
    if a < 0 and b < 0:
        a = a * (-1)
        c = b * (-1)
        while a > 0:
            p = a % 10
            while c > 0:
                t = c % 10
                if t == p:
                    d = True
                c = c // 10
            c = b
            a = a // 10
        if d == False:
            return 'НЕТ'
        else:
            return "ДА"
    if a > 0 and b < 0:
        c = b * (-1)
        while a > 0:
            p = a % 10
            while c > 0:
                t = c % 10
                if t == p:
                    d = True
                c = c // 10
            c = b
            a = a // 10
        if d == False:
            return 'НЕТ'
        else:
            return "ДА"
    if a < 0 and b > 0:
        a = a * (-1)
        while a > 0:
            p = a % 10
            while c > 0:
                t = c % 10
                if t == p:
                    d = True
                c = c // 10
            c = b
            a = a // 10
        if d == False:
            return 'НЕТ'
        else:
            return "ДА"
    else:
        return 'ДА'
