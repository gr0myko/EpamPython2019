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
        if self.weekday == 'Monday':
            return menu['Monday']['first_courses']['vegan']
        elif self.weekday == 'Tuesday':
            return menu['Tuesday']['first_courses']['vegan']
        elif self.weekday == 'Wednesday':
            return menu['Wednesday']['first_courses']['vegan']
        elif self.weekday == 'Thursday':
            return menu['Thursday']['first_courses']['vegan']
        elif self.weekday == 'Friday':
            return menu['Friday']['first_courses']['vegan']
        elif self.weekday == 'Saturday':
            return menu['Saturday']['first_courses']['vegan']
        elif self.weekday == 'Sunday':
            return menu['Sunday']['first_courses']['vegan']


class ChildFirstCourse(AbstractFirstCourse):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        if self.weekday == 'Monday':
            return menu['Monday']['first_courses']['child']
        elif self.weekday == 'Tuesday':
            return menu['Tuesday']['first_courses']['child']
        elif self.weekday == 'Wednesday':
            return menu['Wednesday']['first_courses']['child']
        elif self.weekday == 'Thursday':
            return menu['Thursday']['first_courses']['child']
        elif self.weekday == 'Friday':
            return menu['Friday']['first_courses']['child']
        elif self.weekday == 'Saturday':
            return menu['Saturday']['first_courses']['child']
        elif self.weekday == 'Sunday':
            return menu['Sunday']['first_courses']['child']


class ChinaFirstCourse(AbstractFirstCourse):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        if self.weekday == 'Monday':
            return menu['Monday']['first_courses']['china']
        elif self.weekday == 'Tuesday':
            return menu['Tuesday']['first_courses']['china']
        elif self.weekday == 'Wednesday':
            return menu['Wednesday']['first_courses']['china']
        elif self.weekday == 'Thursday':
            return menu['Thursday']['first_courses']['china']
        elif self.weekday == 'Friday':
            return menu['Friday']['first_courses']['china']
        elif self.weekday == 'Saturday':
            return menu['Saturday']['first_courses']['china']
        elif self.weekday == 'Sunday':
            return menu['Sunday']['first_courses']['china']


class AbstractSecondCourse(ABC):
    def serve_meal(self):
        pass


class VeganSecondCourse(AbstractSecondCourse):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        if self.weekday == 'Monday':
            return menu['Monday']['second_courses']['vegan']
        elif self.weekday == 'Tuesday':
            return menu['Tuesday']['second_courses']['vegan']
        elif self.weekday == 'Wednesday':
            return menu['Wednesday']['second_courses']['vegan']
        elif self.weekday == 'Thursday':
            return menu['Thursday']['second_courses']['vegan']
        elif self.weekday == 'Friday':
            return menu['Friday']['second_courses']['vegan']
        elif self.weekday == 'Saturday':
            return menu['Saturday']['second_courses']['vegan']
        elif self.weekday == 'Sunday':
            return menu['Sunday']['second_courses']['vegan']


class ChildSecondCourse(AbstractSecondCourse):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        if self.weekday == 'Monday':
            return menu['Monday']['second_courses']['child']
        elif self.weekday == 'Tuesday':
            return menu['Tuesday']['second_courses']['child']
        elif self.weekday == 'Wednesday':
            return menu['Wednesday']['second_courses']['child']
        elif self.weekday == 'Thursday':
            return menu['Thursday']['second_courses']['child']
        elif self.weekday == 'Friday':
            return menu['Friday']['second_courses']['child']
        elif self.weekday == 'Saturday':
            return menu['Saturday']['second_courses']['child']
        elif self.weekday == 'Sunday':
            return menu['Sunday']['second_courses']['child']


class ChinaSecondCourse(AbstractSecondCourse):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        if self.weekday == 'Monday':
            return menu['Monday']['second_courses']['china']
        elif self.weekday == 'Tuesday':
            return menu['Tuesday']['second_courses']['china']
        elif self.weekday == 'Wednesday':
            return menu['Wednesday']['second_courses']['china']
        elif self.weekday == 'Thursday':
            return menu['Thursday']['second_courses']['china']
        elif self.weekday == 'Friday':
            return menu['Friday']['second_courses']['china']
        elif self.weekday == 'Saturday':
            return menu['Saturday']['second_courses']['china']
        elif self.weekday == 'Sunday':
            return menu['Sunday']['second_courses']['china']


class AbstractDrink(ABC):
    def serve_meal(self):
        pass


class VeganDrink(AbstractDrink):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        if self.weekday == 'Monday':
            return menu['Monday']['drinks']['vegan']
        elif self.weekday == 'Tuesday':
            return menu['Tuesday']['drinks']['vegan']
        elif self.weekday == 'Wednesday':
            return menu['Wednesday']['drinks']['vegan']
        elif self.weekday == 'Thursday':
            return menu['Thursday']['drinks']['vegan']
        elif self.weekday == 'Friday':
            return menu['Friday']['drinks']['vegan']
        elif self.weekday == 'Saturday':
            return menu['Saturday']['drinks']['vegan']
        elif self.weekday == 'Sunday':
            return menu['Sunday']['drinks']['vegan']


class ChildDrink(AbstractDrink):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        if self.weekday == 'Monday':
            return menu['Monday']['drinks']['child']
        elif self.weekday == 'Tuesday':
            return menu['Tuesday']['drinks']['child']
        elif self.weekday == 'Wednesday':
            return menu['Wednesday']['drinks']['child']
        elif self.weekday == 'Thursday':
            return menu['Thursday']['drinks']['child']
        elif self.weekday == 'Friday':
            return menu['Friday']['drinks']['child']
        elif self.weekday == 'Saturday':
            return menu['Saturday']['drinks']['child']
        elif self.weekday == 'Sunday':
            return menu['Sunday']['drinks']['child']


class ChinaDrink(AbstractDrink):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        if self.weekday == 'Monday':
            return menu['Monday']['drinks']['china']
        elif self.weekday == 'Tuesday':
            return menu['Tuesday']['drinks']['china']
        elif self.weekday == 'Wednesday':
            return menu['Wednesday']['drinks']['china']
        elif self.weekday == 'Thursday':
            return menu['Thursday']['drinks']['china']
        elif self.weekday == 'Friday':
            return menu['Friday']['drinks']['china']
        elif self.weekday == 'Saturday':
            return menu['Saturday']['drinks']['china']
        elif self.weekday == 'Sunday':
            return menu['Sunday']['drinks']['china']


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
