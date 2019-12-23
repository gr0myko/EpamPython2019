"""
Представьте, что вы пишите программу по формированию и выдачи комплексных обедов для сети столовых, которая стала
расширяться и теперь предлагает комплексные обеды для вегетарианцев, детей и любителей китайской кухни.
С помощью паттерна "Абстрактная фабрика" вам необходимо реализовать выдачу комплексного обеда, состоящего из трёх
позиций (первое, второе и напиток).
В файле menu.yml находится меню на каждый день, в котором указаны позиции и их принадлежность к
определенному типу блюд.
"""

from abc import ABC, abstractmethod


# for Monday only
class AbstractFirstCourse(ABC):
    def serve_meal(self):
        pass


class VeganFirstCourse(AbstractFirstCourse):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        if self.weekday == 'Monday':
            return 'Салат с рукколой и редисом'
        elif self.weekday == 'Tuesday':
            return 'Морковно-яблочный салат'
        elif self.weekday == 'Wednesday':
            return 'Салат из свежей капусты с чесночной заправкой'
        elif self.weekday == 'Thursday':
            return 'Салат из огурцов и мяты.'
        elif self.weekday == 'Friday':
            return 'Запеканка из брокколи и цветной капусты'
        elif self.weekday == 'Saturday':
            return 'Салат из моркови с чесноком'
        elif self.weekday == 'Sunday':
            return 'Салат из свежей капусты с яблоком'


class ChildFirstCourse(AbstractFirstCourse):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        if self.weekday == 'Monday':
            return 'Салат из белокочанной капусты с яблоком'
        elif self.weekday == 'Tuesday':
            return 'Свекольный салат с черносливом и фетой'
        elif self.weekday == 'Wednesday':
            return 'Салат из моркови и кураги'
        elif self.weekday == 'Thursday':
            return 'Салат "Витаминный"'
        elif self.weekday == 'Friday':
            return 'Панкейки с морковью'
        elif self.weekday == 'Saturday':
            return 'нутовые блины с печенью трески'
        elif self.weekday == 'Sunday':
            return 'цельнозерновая паста со стручковой фасолью'


class ChinaFirstCourse(AbstractFirstCourse):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        if self.weekday == 'Monday':
            return 'Курица Гунбао'
        elif self.weekday == 'Tuesday':
            return 'Жареные огурцы'
        elif self.weekday == 'Wednesday':
            return 'Тушеные грибы и морские ушки'
        elif self.weekday == 'Thursday':
            return 'Салат фунчоза с мясом'
        elif self.weekday == 'Friday':
            return 'Салат Пекинский с отварной курятиной'
        elif self.weekday == 'Saturday':
            return 'Курица с ананасами в кисло-сладком соусе'
        elif self.weekday == 'Sunday':
            return 'Жареный рис с овощами по китайски'


class AbstractSecondCourse(ABC):
    def serve_meal(self):
        pass


class VeganSecondCourse(AbstractSecondCourse):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        if self.weekday == 'Monday':
            return 'Морковный суп-пюре с хрустящим нутом'
        elif self.weekday == 'Tuesday':
            return 'Гороховый суп с томатной пастой'
        elif self.weekday == 'Wednesday':
            return 'Гороховый суп с томатной пастой'
        elif self.weekday == 'Thursday':
            return 'Грибной суп из вешенок'
        elif self.weekday == 'Friday':
            return 'Темный борщ с грибами и черносливом'
        elif self.weekday == 'Saturday':
            return 'Светлый борщ с грибами и курагой'
        elif self.weekday == 'Sunday':
            return 'Запеканка с фасолью и картофельным пюре'


class ChildSecondCourse(AbstractSecondCourse):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        if self.weekday == 'Monday':
            return 'Борщ-пюре'
        elif self.weekday == 'Tuesday':
            return 'Суп рататуй в мультиварке'
        elif self.weekday == 'Wednesday':
            return 'Суп с рыбными фрикадельками'
        elif self.weekday == 'Thursday':
            return 'Суп рататуй в мультиварке'
        elif self.weekday == 'Friday':
            return 'Суп с рыбными фрикадельками'
        elif self.weekday == 'Saturday':
            return 'Гороховый суп'
        elif self.weekday == 'Sunday':
            return 'Овощной суп с нутом'


class ChinaSecondCourse(AbstractSecondCourse):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        if self.weekday == 'Monday':
            return 'Китайский холодный суп из баклажанов'
        elif self.weekday == 'Tuesday':
            return 'Сырный суп с копчеными колбасками '
        elif self.weekday == 'Wednesday':
            return 'Суп с рисовой лапшой и бараниной'
        elif self.weekday == 'Thursday':
            return 'Кисло-сладкий острый суп'
        elif self.weekday == 'Friday':
            return 'Суп с зимней тыквой и свиными рёбрышками'
        elif self.weekday == 'Saturday':
            return 'Яичный суп с помидорами'
        elif self.weekday == 'Sunday':
            return 'Яичный суп с чёрным древесным грибом'


class AbstractDrink(ABC):
    def serve_meal(self):
        pass


class VeganDrink(AbstractDrink):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        return 'Фруктовый коктейль с кефиром и творогом'


class ChildDrink(AbstractDrink):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        if self.weekday == 'Monday':
            return 'Компот из сухофруктов'
        elif self.weekday == 'Tuesday':
            return 'Компот из замороженных ягод'
        elif self.weekday == 'Wednesday':
            return 'Растишка'
        elif self.weekday == 'Thursday':
            return 'Фрутоняня'
        elif self.weekday == 'Friday':
            return 'Агуша'
        elif self.weekday == 'Saturday':
            return 'Яблочный сок из яблок'
        elif self.weekday == 'Sunday':
            return 'Банановый смузи с печеньем и орехами'


class ChinaDrink(AbstractDrink):
    def __init__(self, weekday):
        self.weekday = weekday

    def serve_meal(self):
        if self.weekday == 'Monday':
            return 'Ореховый кисель'
        elif self.weekday == 'Tuesday':
            return 'Кисель из ржаной муки'
        elif self.weekday == 'Wednesday':
            return 'Кисель из ананаса по-пекински'
        elif self.weekday == 'Thursday':
            return 'Чай из древесных грибов'
        elif self.weekday == 'Friday':
            return 'Кисель из ржаной муки'
        elif self.weekday == 'Saturday':
            return 'Ореховый кисель'
        elif self.weekday == 'Sunday':
            return 'Кисель из ананаса по-пекински'


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


def client_code(menu: AbstractMenu, weekday: str):
    first_course = menu.create_fc(weekday)
    second_course = menu.create_sc(weekday)
    drink = menu.create_drink(weekday)

    print(first_course.serve_meal())
    print(second_course.serve_meal())
    print(drink.serve_meal())


if __name__ == "__main__":
    """
    Клиентский код может работать с любым конкретным классом фабрики.
    """
    client_code(ChinaMenu(), 'Friday')
