##def fib(n):
##    if n==1 or n==2:
##        return 1
##    return fib(n-2)+fib(n-1)


def fib(n):
    fib1=fib2=1
    i=0
    while i<n-2:
        f=fib1+fib2
        fib1=fib2
        fib2=f
        i+=1
    return fib2



    