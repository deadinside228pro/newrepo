a=int(input())
l=0
r=a
if (((r-l)//2)**3) == a:
    print(r//2)
while not (((r - l) // 2) ** 3) == a:
    if (((r-l)//2)**3) > a:
        r=r//2
    elif (((r-l)//2)**3) < a:
        l=r/2
print((r-l)//2)