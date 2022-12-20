from models.animal import Animal


class Cat(Animal):
    def __int__(self, name, age):
        super().__init__(name, age, 4)

    def to_string(self):
        return {"name": self.name,
                "age": self.age,
                "leg_count": self.leg_count}

    @staticmethod
    def communicate():
        return "I am cat, so i can't talk"

    @staticmethod
    def can_fly():
        return False
