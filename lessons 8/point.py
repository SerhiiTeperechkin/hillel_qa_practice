# Написать класс для сущности Точка(содержит в себе координаты Х и Y). Написать классы для сущностей
# Треугольник, Квадрат, которые аггрегируют объекты класса Точка.

# Написать методы, которые считают площадь фигур, если координаты введены правильно. Если нет,
# то показать сообщение об ошибке.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        a = ((self.p2.x - self.p1.x) * (self.p3.y - self.p1.y) -
             (self.p3.x - self.p1.x) * (self.p2.y - self.p1.y)) / 2
        if a < 0:
            print("Ошибка: заданы неправильные координаты.")
            return None
        else:
            return a


class Square:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def area(self):
        s1 = (self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2
        s2 = (self.p3.x - self.p2.x) ** 2 + (self.p3.y - self.p2.y) ** 2
        s3 = (self.p4.x - self.p3.x) ** 2 + (self.p4.y - self.p3.y) ** 2
        s4 = (self.p1.x - self.p4.x) ** 2 + (self.p1.y - self.p4.y) ** 2
        if s1 == s2 == s3 == s4 and (self.p2.x - self.p1.x) * (self.p3.y - self.p2.y) == (self.p3.x - self.p2.x) * (
                self.p2.y - self.p1.y):
            return s1
        else:
            print("Ошибка: заданы неправильные координаты.")
            return None


if __name__ == '__main__':
    # [FIXED] Данные примеры работы класса необходимо писать в мейне, иначе при импорте этот код будет выполнен.

    p1 = Point(6, 0)
    p2 = Point(10, 1)
    p3 = Point(1, 0)

    t = Triangle(p1, p2, p3)
    print("Площадь треугольника:", t.area())
