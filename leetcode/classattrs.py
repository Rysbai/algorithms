
from abc import ABCMeta
import typing


class A(metaclass=ABCMeta):
    foo: typing.ClassVar[str]


class B:
    pass


class Foo:
    bar: typing.ClassVar[str]

    def __init_subclass__(cls, bar: str, **kwargs) -> None:
        cls.bar = bar
        super().__init_subclass__(**kwargs)


class Bar(Foo):
    pass
