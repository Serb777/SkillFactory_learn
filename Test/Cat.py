
class Cat:
    def __init__(self, name: str, sex: str, age: int) -> None:
        self.name = name
        self.sex = sex
        self.age = age

    def get_name(self):
        return self.name
    
    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age
    
    def get_all(self):
        return self.name, self.sex, self.age

    def print_all(self):
        print('Имя: {},\nПол: {},\nВозраст: {}'.format(*cat.get_all()))


# cat = Cat('Vasya', 'male', 2)
# cat.print_all()

