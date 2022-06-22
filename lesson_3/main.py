
"""

What is Dunder Methods - ?

"""


class Num:

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        print('method __add__ called')
        return Num(self.num + other)

    def __sub__(self, other):
        print('method __add__ called')
        self.num -= other
        return Num(self.num)


num1 = Num(20)

num2 = num1 + 20
print(num2.num)
