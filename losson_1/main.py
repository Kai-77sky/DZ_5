
# class User:
#     first_name = None
#     last_name = None
#     age = None
#
#
# jack = User()
# jack.first_name = 'Jack'
# jack.last_name = 'barbaro'
# jack.age = '23'


# Jack = User('Jack', 'Barbaro', 23) # Instance User
# John = User('John', 'Barbaro', 34) # Instance User
# print(Jack.first_name, Jack.last_name, Jack.age)


# def __init__(self, first_name, last_name, age):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.age = age


class Car:

    def __init__(self,
                 title,
                 madel,
                 engine,
                 max_speed,
                 speed):
        self.title = title
        self.madel = madel
        self.engine = engine
        self.max_speed = max_speed
        self.speed = speed


    def get_info(self):
        print(f"""
Title: {self.title} {self.madel}
Engine: {self.engine}
Max_speed: {self.max_speed}
        """)


bmw = Car('BMW', 'e38', 'v10', 360, 20)
bmw.get_info()