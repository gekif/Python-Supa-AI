from contextlib import contextmanager


@contextmanager
def open_file(name):
    f = open(name, 'r')
    yield f
    f.close()


with open_file('file.txt') as f:
    data = f.read()
