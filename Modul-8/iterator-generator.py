# Iterator manual

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value


# Menggunakan iterator
my_iter = MyIterator([10, 20, 30])

for item in my_iter:
    print(item)


# Fungsi generator yield

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen)) # Output: 1
print(next(gen)) # Output: 2
print(next(gen)) # Output: 3

# next(gen) berikutnya akan melempar StopIteration


# Generator untuk menghasilkan deret angka

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

for number in count_up_to(5):
    print(number)  # Output: 1, 2, 3, 4, 5


# Generator Expression

gen_exp = (x * x for x in range(5))

print(next(gen_exp)) # 0
print(next(gen_exp)) # 1
print(next(gen_exp)) # [4, 9, 16]