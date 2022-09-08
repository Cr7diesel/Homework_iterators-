from task_iterator import FlatIterator
from task_generator import generate_lst


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

nested_list2 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


if __name__ == '__main__':
    test = FlatIterator(nested_list)
    print([item for item in test])
    print([item for item in generate_lst(nested_list2)])
