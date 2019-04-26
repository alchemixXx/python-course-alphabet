import string
import dis


list_1 = [x for x in string.ascii_lowercase]
list_2 = [1 for x in string.ascii_lowercase]
list_3 = [x for x in range(0, 100) if x % 2 == 0]
list_4 = [x if x % 2 == 0 else -1 for x in range(0, 100)]


def list_with_while():
    list_5 = []
    i = 0
    while i < 100:
        list_5.append(i)
        i += 1
    return list_5


def list_with_comprehension():
    return [x for x in range(0, 100)]


if __name__ == "__main__":
    print(dis.dis(list_with_comprehension))
    print("||" * 50)
    print(dis.dis(list_with_while))

# print(list_5)
# print(list_1)
# print(list_2)
# print(list_3)
# print(list_4)
