class FlatIterator:

    def __init__(self, some_list):
        self.main_list = sum(some_list, [])

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        if self.cursor == len(self.main_list) - 1:
            raise StopIteration
        self.cursor += 1
        return self.main_list[self.cursor]
