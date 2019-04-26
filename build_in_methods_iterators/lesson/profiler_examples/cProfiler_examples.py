import cProfile
import argparse

from build_in_methods_iterators.lesson.profiler_examples.utils import list_comprehension, \
    iterate_throw_list_comprehension, loop_example, iterate_throw_list_loop, generator_comprehension, \
    iterate_throw_gen_comprehension, generator_loop, iterate_trow_loop_gen

if __name__ == '__main__':
    # Initiate ArgumentParser
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", dest='el_number',
                        help="Number of elements that will be added to containers",
                        type=int,
                        default=1000 * 1000 * 1000
                        )
    args = parser.parse_args()
    # Enable profiler
    pr = cProfile.Profile()
    pr.enable()
    # Create and iterate
    data = list_comprehension(args.el_number)
    iterate_throw_list_comprehension(data)
    # Create and iterate throw loop list
    data = loop_example(args.el_number)
    iterate_throw_list_loop(data)
    # Create and iterate throw generator comprehension
    data = generator_comprehension(args.el_number)
    iterate_throw_gen_comprehension(data)
    # Create and iterate throw loop list
    data = generator_loop(args.el_number)
    iterate_trow_loop_gen(data)

    pr.disable()
    pr.print_stats()
