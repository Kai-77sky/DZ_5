
"""

OOP

"""


class Transport:

    def __init__(self, title, engine, color, model, tachometer):
        self.title = title
        self.engine = engine
        self.color = color
        self.model = model
        self.tachometer = tachometer

    def start_engine(self):
        print(f'On {self.title} {self.model} engine started!')

    def stop_engine(self):
        print(f'On {self.title} {self.model} engine stop!')

    def car_check(self):
        if self.tachometer < 1:
            print('Check ON!')
        else:
            print('Check OFF!')


class Car(Transport):

    def __init__(self,
                 title,
                 engine,
                 color,
                 model,
                 tachometer,
                 max_speed
                 ):
        super().__init__(title, engine, color, model, tachometer)
        self.max_speed = max_speed


class Tesla(Transport):
    pass


tesla = Tesla(
    'Tesla',
    'engine',
    'black',
    'plaid',
    1,
    260
)

print(tesla.max_speed)


