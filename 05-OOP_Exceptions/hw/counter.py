"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    instances_num = 0

    class ModifiedClass(cls):
        def __new__(cls, *args, **kwargs):
            nonlocal instances_num
            instances_num += 1
            instance = super().__new__(cls)
            return instance

        @staticmethod
        def get_created_instances():
            return instances_num

        @staticmethod
        def reset_instances_counter():
            nonlocal instances_num
            instances_before_reset = instances_num
            instances_num = 0
            return instances_before_reset

    return ModifiedClass


@instances_counter
class User:
    pass


if __name__ == '__main__':

    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print(user.get_created_instances())  # 3
    print(user.reset_instances_counter())  # 3
