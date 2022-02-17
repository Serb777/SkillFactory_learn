from Cat import Cat

class Dog(Cat):

    def get_pet(self):
        return self.name, self.age

dog_1 = Dog('Felix', 'male', 2)
dog_2 = Dog('Muchtar', 'male', 0)

print(dog_1.get_pet())
print(dog_2.get_pet())

