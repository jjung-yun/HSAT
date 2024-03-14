def fibo(number):
    if number==0:
        return 0
    elif number==1:
        return 1
    else:
        return fibo(number-2)+fibo(number-1)

print(fibo(int(input())))