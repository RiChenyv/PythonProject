class Animal:
    # 空方法（抽象方法）让animal变成了抽象类（接口）
    def speak(self):
        pass


class Dog(Animal):
    # 复写抽象方法
    def speak(self):
        print("汪汪汪!!!!")


class Cat(Animal):
    # 复写抽象方法
    def speak(self):
        print("喵喵喵~~~~~")


# 实现多态
def make_noise(animal: Animal) -> Animal:
    animal.speak()


dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)
