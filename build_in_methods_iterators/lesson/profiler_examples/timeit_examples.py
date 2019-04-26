import argparse
import timeit
from build_in_methods_iterators.lesson.profiler_examples.utils import \
    (
    list_comprehension,
    generator_comprehension,
    generator_loop,
    loop_example
)


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", dest='el_number',
                        help="Number of elements that will be added to containers",
                        type=int,
                        default=1000
                        )

    args = parser.parse_args()
    list_comprehension_wrapped = wrapper(list_comprehension, args.el_number)
    print("List comprehension working time : ", timeit.timeit(list_comprehension_wrapped))

    list_loop_wrapped = wrapper(loop_example, args.el_number)
    print("List loop example working time : ", timeit.timeit(list_loop_wrapped))

    generator_comprehension_wrapped = wrapper(generator_comprehension, args.el_number)
    print("Generator comprehension working time: ", timeit.timeit(generator_comprehension_wrapped))

    generator_loop_wrapped = wrapper(generator_comprehension, args.el_number)
    print("Generator loop working time: ", timeit.timeit(generator_loop_wrapped))







