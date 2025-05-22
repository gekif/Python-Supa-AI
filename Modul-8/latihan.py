# Coba buat generator yang menghasilkan bilangan Fibonacci hingga nilai maksimum tertentu:
def fibonacci(max_value):
    a, b = 0, 1
    while a <= max_value:
        yield a
        a, b = b, a + b

for num in fibonacci(20):
    print(num)