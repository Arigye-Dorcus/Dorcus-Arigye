class Grandparent:
    def say_hello(self):
        print("Hello from Grandparent")

class Parent(Grandparent):
    def say_hello(self):
        print("Hello from Parent")
        super().say_hello()

class Uncle(Grandparent):
    def say_hello(self):
        print("Hello from Uncle")
        super().say_hello()

class Child(Parent, Uncle):
    def say_hello(self):
        print("Hello from Child")
        super().say_hello()

kid = Child()
kid.say_hello()
print("\nMethod Resolution Order (MRO):")
print(Child.__mro__)