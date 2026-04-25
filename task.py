import datetime


class MyCustomException(Exception):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        if self.message:
            return


class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100,
                             'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20,
                           'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):  # геттер __name_items
        return self.__name_items

    @property
    def number_items(self):  # геттер __number_items
        return self.__number_items

    @property
    def item_price(self):  # геттер __item_price
        return self.__item_price

    @property
    def tax_rate(self):
        return self.__tax_rate

    @name_items.setter
    def name_items(self, name_items):  # сеттер __name_items
        self.__name_items = name_items

    @number_items.setter
    def number_items(self, number_items):  # сеттер __number_items
        self.__number_items = number_items

    def add_item_to_cheque(self, name):  # добавление товара в чек
        if len(name) == 0 or len(name) > 40:  # проверка что длина имени != 0 и не более 40
            raise ValueError(
                'Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.item_price:  # исключение если товара нет в __item_price
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            # добавление имени в список __name_items
            self.name_items.append(name)
            self.number_items += 1
            return self.name_items, self.number_items

    def delete_item_from_check(self, name):  # удаление товара из чека
        if name not in self.name_items:  # исключение если товара нет в __name_items
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.number_items -= 1
            self.name_items.remove(name)
            return self.name_items, self.number_items

    def check_amount(self):  # подсчет суммы чека
        total = []
        for item in self.name_items:
            total.append(self.item_price[item])  # добавление цен в total
        if self.number_items > 10:  # если товаров больше 10, то скидка 10%
            return sum(total)*0.9
        else:
            return sum(total)

    def twenty_percent_tax_calculation(self):  # расчет НДС
        twenty_percent_tax = []  # список товаров с 20% НДС
        total = []  # список цен товаров с 20% НДС
        for item in self.name_items:
            if self.tax_rate[item] == 20:
                twenty_percent_tax.append(item)
                total.append(self.item_price[item])
        if self.number_items > 10:  # если товаров больше 10, то скидка 10%
            return sum(total)*0.9*0.2  # уменьшаем сумму если товаров больше 10
        else:
            return sum(total)*0.2

    def ten_percent_tax_calculation(self):  # расчет НДС
        ten_percent_tax = []  # список товаров с 10% НДС
        total = []  # список цен товаров с 10% НДС
        for item in self.name_items:
            if self.tax_rate[item] == 10:
                ten_percent_tax.append(item)
                total.append(self.item_price[item])
        if self.number_items > 10:  # если товаров больше 10, то скидка 10%
            return sum(total)*0.9*0.1  # уменьшаем сумму если товаров больше 10
        else:
            return sum(total)*0.1

    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

    @staticmethod
    # возврат номера телефона с проверкой
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        elif telephone_number > 9999999999:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return f'+7{telephone_number}'

    @staticmethod
    def get_date_and_time():  # получение даты в формате '<название_интервала>: <значение>'
        date_and_time = []
        now = datetime.datetime.now()
        date = [
            ['часы', lambda x: x.hour],
            ['минуты', lambda x: x.minute],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year]
        ]
        for element in date:
            date_and_time.append(f'{element[0]}: {element[1](now)}')
        return date_and_time
