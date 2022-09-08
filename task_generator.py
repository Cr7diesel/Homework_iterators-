def generate_lst(lst):
    for item in lst:
        for value in item:
            yield value
