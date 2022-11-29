a = int(input('введите а '))
k=0
for i in range (1, a):
    i=i**2
    if i<a:
        k+=1
        print(i)
print("kol-vo:",k)
