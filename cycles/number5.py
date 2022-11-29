a = int(input('vvedite a '))
b = int(input('vvedite b '))
sum = 0
if a>b:
    for i in range (a,b, -1):
        if i % 7 == 0:
            sum = sum + i
elif a<b:
    for i in range (a,b+1):
        if i % 7 == 0:
            sum = sum + i
print(sum)
