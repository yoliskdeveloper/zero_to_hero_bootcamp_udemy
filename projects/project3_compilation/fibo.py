# fibonaci number

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

def fib2(n):
    resutl = []
    a, b = 0, 1
    while a < n:
        resutl.append(a)
        a, b = b, a + b
    return  resutl

if __name__ == '__main__':
    import sys
    fib(int(sys.argv[1]))

