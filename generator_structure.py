import random

# cara umum
def nilai_kubik(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

print(nilai_kubik(10))

# cara 2 menggunakan decorator
def nilai_kubik2(n):

    for x in range(n):
        yield x ** 3

print(list(nilai_kubik2(10)))

def gen_fib(n):
    a = 1
    b = 1
    for x in range(n):
        yield a,
        a, b = b, a+b

for x in gen_fib(10):
    print(x)

# generator random number antara high dan low number
ran = random.randint(1, 10)
print(ran)
def rand_numb(low, high, n):
    for i in range(n):
        yield random.randint(low, high)

print(list(rand_numb(1, 10, 12)))
