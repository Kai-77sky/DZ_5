

class Animals:

    def __init__(self, name, voice_text):
        self.name = name
        self.voice_text = voice_text

    def voice(self):
        print(f'{self.name} {self.voice_text}')


class Dog(Animals):
    pass


class Cat(Animals):
    pass

    def voice(self):
        pass

    def go_toilet(self):
        print("I'am going.....")


sharick = Dog('Sharick', 'GAF! GAF!')
murka = Cat('Murka', 'Mew Mew')


class Human:

    def happy(self):
        print("OOO I'm heppy")


class Animals2:

    def Happy(self):
        print("I'm Happy animal!")