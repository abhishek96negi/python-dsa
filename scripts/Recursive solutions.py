def printN(n):
    if n > 0:
        printN(n - 1)
        print(n, end=' ')


def printNreverse(n):
    if n > 0:
        print(n, end=' ')
        printNreverse(n - 1)


def printNOdd(n):
    if n > 0:
        printNOdd(n - 1)
        print(2 * n - 1, end=' ')


def printNEven(n):
    if n > 0:
        printNEven(n - 1)
        print(2 * n, end=' ')


def printNOddreverse(n):
    if n > 0:
        print(2 * n - 1, end=' ')
        printNOddreverse(n - 1)


def printNEvenreverse(n):
    if n > 0:
        print(2 * n, end=' ')
        printNEvenreverse(n - 1)

def sumN(n):
    if n==1:
        return 1
    return n + sumN(n-1)

def sumNOdd(n):
    if n==1:
        return 1
    return 2*n-1 + sumNOdd(n-1)

def sumNEven(n):
    if n==1:
        return 2
    return 2*n + sumNEven(n-1)

def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

def sumNSquare(n):
    if n==1:
        return 1
    return n*n + sumNSquare(n-1)

print("Sum is",sumNSquare(5))
printNOddreverse(10)
