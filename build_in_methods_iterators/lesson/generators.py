import sys


def interger_values():
    i = 0
    while True:
        yield i
        i += 1
        yield str(i)


# our_gen = interger_values()
#
# # print(next(our_gen))
#
# for i in range(100):
#     print(id(our_gen))
#     step_value = next(our_gen)
#     print(step_value)

def generators_examples(step=0):
    i = 0
    while i < 10000:
        yield i + step
        i += 1


numbers = range(100)

g = generators_examples()

d = [x for x in range(10000)]

print("Generator ", sys.getsizeof(g))
print("List ", sys.getsizeof(d))

#
# from pprint import pprint
# pprint(dir(g))
#
# g.send()


members = [
    {'age': 43, 'name': 'Denis'},
    {'age': 49, 'name': 'Roman'},
    {'age': 36, 'name': 'Godzilla'},
    {'age': 47, 'name': 'Spike'},
    {'age': 31, 'name': 'SuperMan'},
    {'age': 49, 'name': 'Batman'},
    {'age': 37, 'name': 'Claus'},
    {'age': 55, 'name': 'Frank'},
    {'age': 83, 'name': 'Homer'}
]

members_gen = (members)
print(next(members_gen))

print(range(100))
