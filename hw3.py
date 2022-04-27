from datetime import date
import types


class ClassMethod:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, cls=None):
        if cls is None:
            return type(obj)
        if hasattr(type(self.f), '__get__'):
            return self.f.__get__(cls, cls)
        return types.MethodType(self.f, cls)


class StaticMethod:
    def __init__(self, f):
        self.f = f

    def __get__(self, instance, owner):
        return self.f

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def get_year_from_year(cls, name: str, birth_year: int):
        return cls(name, date.today().year - birth_year)

    @ClassMethod
    def get_2_year_from_year(cls, name: str, birth_year: int):
        return cls(name, date.today().year - birth_year)

    @staticmethod
    def recreate_date_format(date: str):
        return date.replace("/", "-")

    @StaticMethod
    def recreate_2_date_format(date: str):
        return date.replace("/", "-")

    def display(self):
        return f'{self.name} {self.age}'


class Realization:
    person = Person('David', 2007)
    person_with_my_method = Person.get_year_from_year('Vlad', 2002)
    person_with_builtin_method = Person.get_year_from_year('Alex', 1990)

    my_date_method = Person.recreate_2_date_format('2020/19/20')
    builtin_method = Person.recreate_date_format('2020/19/20')

    def print_examples(self):
        print(f'My ClassMethod realization result {self.person_with_my_method.display()}')
        print(f'Implemented @classmethod realization result {self.person_with_builtin_method.display()}\n')

        print(f'My StaticMethod realization result {self.my_date_method}')
        print(f'Implemented @staticmethod realization result {self.builtin_method}')


if __name__ == '__main__':
    Realization().print_examples()
