

class Counter(object):
    def __init__(self, size):
        self.size = size
        self.start = 0

    def __next__(self):
        if self.start < self.size:
            self.start += 1
            return self.start - 1
        else:
            raise StopIteration

    def __iter__(self):
        return self

    def __str__(self):
        return self.start


c = Counter(3)

for num in c:
    print(num)