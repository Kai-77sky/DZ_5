# from .models import Person
#
#
# def create_person(
#         first_name,
#         last_name,
#         age
# ):
#     person = Person(
#         first_name=first_name,
#         last_name=last_name,
#         age=age
#     )
#     return person


class Fraction:

    def __init__(self, numerator, denumreator):
        self.numerator = numerator
        self.denumerator = denumreator

    def __add__(self, other):
        self.numerator += other.numerator
        return Fraction(self.numerator, self.denumerator)


fraction1 = Fraction(1, 2)
fraction2 = Fraction(1, 2)

fraction3 = fraction1 + fraction2
print(f'{fraction3.numerator}/{fraction3.denumerator}')
