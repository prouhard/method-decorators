from custom_decorators import print_text


class MyClass:
    @print_text(text='text_1')
    def normal_method_1(self, arg):
        return arg

    @print_text(text='text_2')
    def static_method_1(arg):
        return arg

    @print_text
    def normal_method_2(self, arg):
        return arg

    @print_text
    def static_method_2(arg):
        return arg


if __name__ == '__main__':
    my_object = MyClass()
    print(my_object.normal_method_1(1))
    print(MyClass.static_method_1(1))
    print(my_object.normal_method_2(1))
    print(MyClass.static_method_2(1))
