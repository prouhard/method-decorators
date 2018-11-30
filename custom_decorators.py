from library import MethodDecorator


class print_text(MethodDecorator):
    def wrapper(self, *args, **kwargs):
        print(
            'In custom method decorator with args {args} and kwargs {kwargs}'.format(
                args=self.args,
                kwargs=self.kwargs
            )
        )
        print(
            'This is a {method_type} method'.format(
                method_type='static' if self.is_staticmethod else 'normal'
            )
        )
        print(self.kwargs.get('text', 'No text passed as argument'))
        return self.method(*args, **kwargs)

