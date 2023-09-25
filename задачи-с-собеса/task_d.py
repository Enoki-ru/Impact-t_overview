from fractions import Fraction
n=int(input())
a=1
b=1
if n<=100:

    for i in range(1,n+1):
        if n==1:
            a*=i*(i+4)*(i+5)
            b*=(i+1)*(i+2)*(i+6)
        else:
            if (i==1):
                a*=i*(i+4)*(i+5)
                b*=(i+2)
            elif i==n:
                a*=(i+4)
                b*=(i+1)*(i+2)*(i+6)
            else:
                a*=(i+4)
                b*=(i+2)
else:
    a=(n+4)*(n+3)*(n+2) 
    b=2*(n+1)*(n+2)*(n+6)
a=b-a
# print(a,b)
q=Fraction(a,b)
print(q.numerator,q.denominator)

# a*=i*(i+4)*(i+5)
# b*=(i+1)*(i+2)*(i+6)