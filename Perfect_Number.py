def perfect_number(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s==n
x=int(input())
print(perfect_number(x))

