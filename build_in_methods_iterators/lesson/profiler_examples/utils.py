def list_comprehension(number_of_elements):
    return [x for x in range(number_of_elements)]


def generator_comprehension(number_of_elements):
    return range(number_of_elements)


def generator_loop(number_of_elements):
    i = 0
    while i < number_of_elements:
        yield i
        i += 1


def loop_example(number_of_elements):
    res = []
    i = 0
    while i < number_of_elements:
        res.append(i)
        i += 1
    return res


def iterate_throw_list_comprehension(container):
    for i in container:
        pass


def iterate_throw_gen_comprehension(container):
    for i in container:
        pass


def iterate_throw_list_loop(container):
    for i in container:
        pass


def iterate_trow_loop_gen(container):
    for i in container:
        pass