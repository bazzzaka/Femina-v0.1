import random


class Process:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def result(self):
        print(f'args is \n {self.args}\nkwargs is \n {self.kwargs}')
        num1 = random.random()
        num2 = random.random()
        res = num1 + num2
        return res
