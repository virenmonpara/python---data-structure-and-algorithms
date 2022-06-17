class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30  # private variable because double underscore

    def public_method(self):
        print(self.__c)  # like this we can use private instance variable
        print("public method")
        self.__private_method()  # like this we can use private method

    def __private_method(self):
        print("private method")


hello = Hello('name')
print(hello.a)
print(hello._b)
print(hello.__c)  # it wil give error because it is private variable

hello.public_method()
hello.__private_method()  # it will give error because it is private method
