"""
Представьте, что вы пишите программу по формированию и выдачи комплексных обедов для сети столовых, которая стала
расширяться и теперь предлагает комплексные обеды для вегетарианцев, детей и любителей китайской кухни.
С помощью паттерна "Абстрактная фабрика" вам необходимо реализовать выдачу комплексного обеда, состоящего из трёх
позиций (первое, второе и напиток).
В файле menu.yml находится меню на каждый день, в котором указаны позиции и их принадлежность к
определенному типу блюд.
"""

from abc import ABC, abstractmethod
from ruamel import yaml

with open("menu.yml", 'r', encoding='utf-8') as file:
    menu = yaml.safe_load(file)


class AbstractFirstCourse(ABC):
    def serve_meal(self):
        pass


class VeganFirstCourse(AbstractFirstCourse):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        return menu[self.weekday]['first_courses']['vegan']


class ChildFirstCourse(AbstractFirstCourse):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        return menu[self.weekday]['first_courses']['child']


class ChinaFirstCourse(AbstractFirstCourse):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        return menu[self.weekday]['first_courses']['china']


class AbstractSecondCourse(ABC):
    def serve_meal(self):
        pass


class VeganSecondCourse(AbstractSecondCourse):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        return menu[self.weekday]['second_courses']['vegan']


class ChildSecondCourse(AbstractSecondCourse):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        return menu[self.weekday]['second_courses']['child']


class ChinaSecondCourse(AbstractSecondCourse):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        return menu[self.weekday]['second_courses']['china']


class AbstractDrink(ABC):
    def serve_meal(self):
        pass


class VeganDrink(AbstractDrink):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        return menu[self.weekday]['drinks']['vegan']


class ChildDrink(AbstractDrink):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        return menu[self.weekday]['drinks']['child']


class ChinaDrink(AbstractDrink):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        return menu[self.weekday]['drinks']['china']


class AbstractMenu(ABC):
    @abstractmethod
    def create_fc(self, weekday) -> AbstractFirstCourse:
        pass

    @abstractmethod
    def create_sc(self, weekday) -> AbstractSecondCourse:
        pass

    @abstractmethod
    def create_drink(self, weekday) -> AbstractDrink:
        pass


class VeganMenu(AbstractMenu):
    def create_fc(self, weekday: str) -> VeganFirstCourse:
        return VeganFirstCourse(weekday)

    def create_sc(self, weekday) -> VeganSecondCourse:
        return VeganSecondCourse(weekday)

    def create_drink(self, weekday) -> VeganDrink:
        return VeganDrink(weekday)


class ChildMenu(AbstractMenu):
    def create_fc(self, weekday) -> ChildFirstCourse:
        return ChildFirstCourse(weekday)

    def create_sc(self, weekday) -> ChildSecondCourse:
        return ChildSecondCourse(weekday)

    def create_drink(self, weekday) -> ChildDrink:
        return ChildDrink(weekday)


class ChinaMenu(AbstractMenu):
    def create_fc(self, weekday) -> ChinaFirstCourse:
        return ChinaFirstCourse(weekday)

    def create_sc(self, weekday) -> ChinaSecondCourse:
        return ChinaSecondCourse(weekday)

    def create_drink(self, weekday) -> ChinaDrink:
        return ChinaDrink(weekday)


def client_code(menu_type: AbstractMenu, weekday: str):
    first_course = menu_type.create_fc(weekday)
    second_course = menu_type.create_sc(weekday)
    drink = menu_type.create_drink(weekday)

    print(first_course.serve_meal())
    print(second_course.serve_meal())
    print(drink.serve_meal())


if __name__ == "__main__":
    """
    Клиентский код может работать с любым конкретным классом фабрики.
    """
    client_code(ChildMenu(), 'Sunday')
