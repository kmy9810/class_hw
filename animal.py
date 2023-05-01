class Animal:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        print(f'안녕! 나는 {self.name}!! {self.age}살이야!')


class Dog(Animal):
    def speak(self):
        return '나는 강아지! 멍멍!'

class Cat(Animal):
    def speak(self):
        return '나는 고양이! 야옹!'


cat = Dog(name='cat', age=2)
print(cat.speak())


dog = Dog(name='dog', age=4)
print(dog.speak())