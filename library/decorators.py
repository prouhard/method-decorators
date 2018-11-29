from functools import partial

import abc


class MethodDecorator(metaclass=abc.ABCMeta):
    def __get__(self, obj, objtype=None):
        self._is_staticmethod = obj == None
        if self._is_staticmethod:
            return self.wrapper
        return partial(self.wrapper, obj)

    @abc.abstractmethod
    def wrapper(self, *args, **kwargs):
        ...


class CallableMethodDecorator(MethodDecorator):
    def __init__(self, *args, **kwargs):
        self.__instanciated = False
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        if not self.__instanciated:
            self.method = args[0]
            self.__instanciated = True
            return self
        return self.wrapper(*args, **kwargs)


class NonCallableMethodDecorator(MethodDecorator):
    def __init__(self, method):
        self.method = method
