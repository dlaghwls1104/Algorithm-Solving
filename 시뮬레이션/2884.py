h,m=map(int,input().split())


if m>44:
    print(h,m-15)
elif m<45 and h>0:
    print(h-1,m+15)
else:
    print(23,m+15)

