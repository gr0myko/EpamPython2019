"""
Реализовать класс Quaternion, позволяющий работать с кватернионами
https://ru.wikipedia.org/wiki/%D0%9A%D0%B2%D0%B0%D1%82%D0%B5%D1%80%D0%BD%D0%B8%D0%BE%D0%BD
Функциональность (магическими методами):
- сложение
- умножение
- деление
- сравнение
- нахождение модуля
- строковое представление и repr
По желанию:
- взаимодействие с числами других типов
"""
import math


class Quaternion:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.result = ''

    def __repr__(self):
        return f"Quaternion({self.a}, {self.b}, {self.c}, {self.d})"

    def __str__(self):
        self.result += f'Q = {self.a}'
        self.result += f' - {-1 * self.b}i' if self.b < 0 else f' + {self.b}i'
        self.result += f' - {-1 * self.c}j' if self.c < 0 else f' + {self.c}j'
        self.result += f' - {-1 * self.d}k' if self.d < 0 else f' + {self.d}k'
        return self.result

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        c = self.c + other.c
        d = self.d + other.d
        return Quaternion(a, b, c, d)

    def __mul__(self, other):
        if isinstance(other, Quaternion):
            a = self.a * other.a - self.b * other.b \
                - self.c * other.c - self.d * other.d
            b = self.a * other.b + self.b * other.a \
                + self.c * other.d - self.d * other.c
            c = self.a * other.c + self.c * other.a \
                + self.d * other.b - self.b * other.d
            d = self.a * other.d + self.d * other.a \
                + self.b * other.c - self.c * other.b
            return Quaternion(a, b, c, d)
        else:
            raise TypeError("Operation undefined.")

    def __truediv__(self, other):
        # division of quaternions: https://www.mathworks.com/help/aeroblks/quaterniondivision.html
        # calculator http://tamivox.org/redbear/qtrn_calc/index.html
        if isinstance(other, Quaternion):
            a = (other.a * self.a + other.b * self.b + other.c * self.c + other.d * self.d) \
                / (other.a ** 2 + other.b ** 2 + other.c ** 2 + other.d ** 2)
            b = (other.a * self.b - other.b * self.a - other.c * self.d + other.d * self.c) \
                / (other.a ** 2 + other.b ** 2 + other.c ** 2 + other.d ** 2)
            c = (other.a * self.c + other.b * self.d - other.c * self.a - other.d * self.b) \
                / (other.a ** 2 + other.b ** 2 + other.c ** 2 + other.d ** 2)
            d = (other.a * self.d - other.b * self.c + other.c * self.b - other.d * self.a) \
                / (other.a ** 2 + other.b ** 2 + other.c ** 2 + other.d ** 2)
            return Quaternion(a, b, c, d)
        else:
            raise TypeError("Operation undefined.")

    def __eq__(self, other):
        r = list(map(lambda i, j: abs(i) == abs(j),
                     self.__dict__.values(), other.__dict__.values()))
        return sum(r) == len(r)

    def __abs__(self):
        # https://www.mathworks.com/help/aeroblks/quaternionmodulus.html
        abs_q = math.sqrt(self.a**2 + self.b + self.c + self.d)
        return abs_q


q1 = Quaternion(4, 7, 3, 5)
q2 = Quaternion(2, 9, 6, 1)
print(q2/q1)
