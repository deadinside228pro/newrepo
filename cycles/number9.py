a =int(input('vvedite a '))
k=0
if a>0:
    while a !=0 :
        i = a%10
        if i%2!=0:
            k+=1
        a=a//10
        print(a,'',end='')
elif a<0:
    while a != 0:
        i = a%10
        if 1%2 != 0:
            k+=1
        a=(a//10)+1
        print(a,'',end='')
print(sep='')
print('kol-vo: ',k)


