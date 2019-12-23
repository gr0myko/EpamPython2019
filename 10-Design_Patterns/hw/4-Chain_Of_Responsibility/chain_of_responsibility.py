"""
С помощью паттерна "Цепочка обязанностей" составьте список покупок для выпечки блинов.
Необходимо осмотреть холодильник и поочередно проверить, есть ли у нас необходимые ингридиенты:
    2 яйца
    300 грамм муки
    0.5 л молока
    100 грамм сахара
    10 мл подсолнечного масла
    120 грамм сливочного масла
В итоге мы должны получить список недостающих ингридиентов.
"""
from abc import ABC, abstractmethod


class Handler(ABC):
    """
    Интерфейс Обработчика объявляет метод построения цепочки обработчиков. Он
    также объявляет метод для выполнения запроса.
    """

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractHandler(Handler):
    """
    Поведение цепочки по умолчанию может быть реализовано внутри базового класса
    обработчика.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler):
        self._next_handler = handler
        # Возврат обработчика отсюда позволит связать обработчики простым
        # способом, вот так:
        # handler1.set_next(handler2).set_next(handler3)
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


pancakes_receipt = {'eggs': 2, 'flour': 300, 'milk': 0.5, 'oil': 10, 'butter': 120}


class Fridge:
    products_list = []

    def __init__(self, eggs=2, flour=300, milk=0.5, oil=10, butter=120):
        self.eggs = eggs
        self.flour = flour
        self.milk = milk
        self.oil = oil
        self.butter = butter

    def add_to_list(self, ingredient):
        self.products_list.append(ingredient)


class CheckEggs(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge.eggs < pancakes_receipt['eggs']:
            fridge.add_to_list('eggs')
        if self._next_handler:
            return self._next_handler.handle(fridge)


class CheckFlour(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge.flour < pancakes_receipt['flour']:
            fridge.add_to_list('flour')
        if self._next_handler:
            return self._next_handler.handle(fridge)


class CheckMilk(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge.milk < pancakes_receipt['milk']:
            fridge.add_to_list('milk')
        if self._next_handler:
            return self._next_handler.handle(fridge)


class CheckOil(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge.oil < pancakes_receipt['oil']:
            fridge.add_to_list('oil')
        if self._next_handler:
            return self._next_handler.handle(fridge)


class CheckButter(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge.butter < pancakes_receipt['butter']:
            fridge.add_to_list('butter')
        if self._next_handler:
            return self._next_handler.handle(fridge)


def check_ingredients(fridge):
    check_eggs = CheckEggs()
    check_flour = CheckFlour()
    check_milk = CheckMilk()
    check_oil = CheckOil()
    check_butter = CheckButter()

    check_eggs.set_next(check_flour).set_next(check_milk).set_next(check_oil).set_next(check_butter)

    check_eggs.handle(fridge)
    return print(fridge.products_list)


fridge_to_check = Fridge(eggs=1, flour=250, milk=1, oil=100, butter=10)
check_ingredients(fridge_to_check)
