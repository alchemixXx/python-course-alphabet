import calc


def test_add():
    if calc.add(1, 2) == 3:
        print("True")
    else:
        print("False")


def test_sub():
    if calc.sub(4, 2) == 2:
        print("True")
    else:
        print("False")


def test_mult():
    if calc.mult(5, 2) == 10:
        print("True")
    else:
        print("False")


def test_div():
    if calc.div(8, 4) == 2:
        print("True")
    else:
        print("False")

test_add()
test_sub()
test_mult()
test_div()