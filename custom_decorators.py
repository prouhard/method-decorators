from library import (
    CallableMethodDecorator,
    NonCallableMethodDecorator
)


class print_this_text(CallableMethodDecorator):
    def wrapper(self, instance, *args, **kwargs):
        print(
            'In custom callable decorator with args {args} and kwargs {kwargs}'.format(
                args=self.args,
                kwargs=self.kwargs
            )
        )
        print(
            'This is a {method_type} method'.format(
                method_type=['normal', 'static'][self._is_staticmethod]
            )
        )
        print(self.kwargs.get('text'))
        return self.method(instance, *args, **kwargs)
    
class print_hard_coded_text(NonCallableMethodDecorator):
    def wrapper(self, instance, *args, **kwargs):
        print('In custom non callable decorator without args or kwargs')
        print(
            'This is a {method_type} method'.format(
                method_type=['normal', 'static'][self._is_staticmethod]
            )
        )
        print('hard_coded_text')
        return self.method(instance, *args, **kwargs)
