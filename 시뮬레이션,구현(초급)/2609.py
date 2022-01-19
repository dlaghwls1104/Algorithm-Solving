#유클리어드 호제법
n,m=map(int,input().split())
def gcd(x,y):
    while y:
        x,y=y,x%y
    return x

def lcm(x,y):
    return x*y // gcd(x,y)


print(gcd(n,m))
print(lcm(n,m))