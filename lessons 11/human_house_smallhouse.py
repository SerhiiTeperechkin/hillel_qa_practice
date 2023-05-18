class Human:
    default_name = "User"
    default_age = 45

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Money: {self.__money}")
        print(f"House: {self.__house}")

    @staticmethod
    def default_info():
        print(f"Default name: {Human.default_name}")
        print(f"Default age: {Human.default_age}")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        self.__money += amount

    def buy_house(self, house, discount=0):
        final_price = house.final_price(discount)
        if self.__money >= final_price:
            self.__make_deal(house, final_price)
            print("House purchased successfully!")
        else:
            print("Insufficient funds to buy the house.")


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount)


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area=40, price=price)


if __name__ == '__main__':
    # Викличте довідковий метод default_info() для класу Human()
    Human.default_info()

    # Створіть об'єкт класу Human
    # Виведіть довідкову інформацію про створений об'єкт (викличте метод info())
    human = Human('Serega', 23)
    human.info()

    # Створіть об'єкт класу SmallHouse
    house = SmallHouse(600)

    # Спробуйте купити створений будинок, переконайтеся в отриманні попередження
    human.buy_house(house)

    # Виправте фінансове становище об'єкта - викличте метод earn_money()
    human.earn_money(900)

    # Знову спробуйте купити будинок
    human.buy_house(house, discount=0.2)

    # Подивіться, як змінилося стан об'єкта класу Human
    human.info()
