import time


# Упражнение 1.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def info(self):
        print(self.x, self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


# Упражнение 2.


class Rectangle:
    def __init__(self, point_1, point_2):
        self.x1, self.y1, self.x2, self.y2 = point_1.get_x(), point_1.get_y(), point_2.get_x(), point_2.get_y()
        self.width = point_2.get_x() - point_1.get_x()
        self.height = point_2.get_y() - point_1.get_y()

    def get_s(self):
        return self.width * self.height

    def get_p(self):
        return (self.width + self.height) * 2

    def contains(self, point):  # Упражнение 3.
        return True if self.x1 <= point.get_x() <= self.x2 and self.y1 <= point.get_y() <= self.y2 else False


p1 = Point(2, 3)
p2 = Point(4, 4)
p3 = Point(2, 5)

rect = Rectangle(p1, p2)


# print(rect.get_p(), rect.get_s())
# print(rect.contains(p3))


# Упражнение 4.


class Counter:
    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter += 1

    def decrement(self):
        if self.counter > 0:
            self.counter -= 1

    def get_counter(self):
        return self.counter


# Упражнение 5.


class Watch:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def add_hour(self):
        self.hour += 1
        if self.hour == 24:
            self.hour = 0

    def add_minute(self):
        self.minute += 1
        if self.minute >= 60:
            self.add_hour()
            self.minute -= 60

    def add_second(self):
        self.second += 1
        if self.second >= 60:
            self.add_minute()
            self.second -= 60

    def __add__(self, other):  # Упражнение 6.
        self.second += other.second
        if self.second > 59:
            self.second -= 60
            self.add_minute()

        self.minute += other.minute
        if self.minute > 59:
            self.minute -= 60
            self.add_hour()

        self.hour += other.hour

    def info(self):
        print(self.hour, self.minute, self.second)


w = Watch(11, 59, 20)
w.info()
w2 = Watch(12, 1, 50)

w + w2
w.info()


# Упражнение 7.


class Grass:
    def __init__(self, nutritional):
        self.nutritional = nutritional


class Animal:
    def __init__(self, name):
        self.stomach = 50
        self.name = name

    def live(self, grass):
        if self.stomach < 50:
            while self.stomach < 200:
                time.sleep(0.2)
                self.eat(grass)
            print(f"Животное {self.name} наелось.")
        else:
            self.wait()

    def wait(self):
        self.stomach -= 20
        print(f"{self.name} гуляет. Наполненность желудка {self.stomach}.")

    def eat(self, grass):
        self.stomach += grass.nutritional
        print(f"{self.name} eст. Наполненность желудка {self.stomach}.")


def task_07():
    field = Grass(25)
    cow = Animal("Корова")
    while True:
        time.sleep(1)
        cow.live(field)


# task_07()


# Упражнение 8.


class Storm:
    def info(self):
        print("Storm")


class Dust:
    def info(self):
        print("Dust")


class Lightning:
    def info(self):
        print("Lightning")


class Lava:
    def info(self):
        print("Lava")


class Mud:
    def info(self):
        print("Mud")


class Steam:
    def info(self):
        print("Steam")


class Earth:
    def info(self):
        print("Earth")

    def __add__(self, other):
        if type(other) is Fire:
            return Lava()
        elif type(other) == Water:
            return Mud()
        elif type(other) is Air:
            return Dust()


class Fire:
    def info(self):
        print("Fire")

    def __add__(self, other):
        if type(other) is Earth:
            return Lava()
        elif type(other) == Water:
            return Steam()
        elif type(other) is Air:
            return Lightning()


class Water:
    def info(self):
        print("Water")

    def __add__(self, other):
        if type(other) is Earth:
            return Mud()
        elif type(other) == Fire:
            return Steam()
        elif type(other) is Air:
            return Storm()


class Air:
    def info(self):
        print("Air")

    def __add__(self, other):
        if type(other) is Earth:
            return Dust()
        elif type(other) == Fire:
            return Lightning()
        elif type(other) is Water:
            return Storm()


class FifthElement:
    def info(self):
        print("Leeloo Dallas! Multi-pass!")

    def __add__(self, other):
        return self


def task_08():
    e = Earth()
    f = Fire()
    w = Water()
    a = Air()
    fe = FifthElement()

    s = f + a
    if s != None:
        s.info()


# task_08()


# Упражнение 9.


class NoMoneyToWithdrawError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PaymentError(Exception):
    def __init__(self, message):
        super().__init__(message)


def print_accounts(accounts):
    """Печать аккаунтов."""
    print("Список клиентов ({}): ".format(len(accounts)))
    for i, (name, value) in enumerate(accounts.items(), start=1):
        print("{}. {} {}".format(i, name, value))


def transfer_money(accounts, account_from, account_to, value):
    """Выполнить перевод 'value' денег со счета 'account_from' на 'account_to'.

   При переводе денежных средств необходимо учитывать:
       - хватает ли денег на счету, с которого осуществляется перевод;
       - перевод состоит из уменьшения баланса первого счета и увеличения
         баланса второго; если хотя бы на одном этапе происходит ошибка,
         аккаунты должны быть приведены в первоначальное состояние
         (механизм транзакции)
         см. https://ru.wikipedia.org/wiki/Транзакция_(информатика).

   Исключения (raise):
       - NoMoneyToWithdrawError: на счету 'account_from'
                                 не хватает денег для перевода;
       - PaymentError: ошибка при переводе.
   """
    debtor = accounts[account_from]
    creditor = accounts[account_to]

    try:
        accounts[account_from] -= value
        accounts[account_to] += value
        if accounts[account_from] < 0:
            raise NoMoneyToWithdrawError(f'на счету {account_from} не хватает денег для перевода')
        print(accounts[account_from], debtor, accounts[account_to], creditor, "creditor")
        if accounts[account_from] != debtor - value or accounts[account_to] != creditor + value:
            raise PaymentError("ошибка при переводе")

    except Exception:
        accounts[account_from] = debtor
        accounts[account_to] = creditor
        print("Перевод был отменен")


#
#
if __name__ == "__main__":
    accounts = {
        "Василий Иванов": 100,
        "Екатерина Белых": 1500,
        "Михаил Лермонтов": 400
    }
    print_accounts(accounts)

    payment_info = {
        "account_from": "Екатерина Белых",
        "account_to": "Василий Иванов"
    }

    print("Перевод от {account_from} для {account_to}...".
          format(**payment_info))

    payment_info["value"] = int(input("Сумма = "))

    transfer_money(accounts, **payment_info)

    print("OK!")

    print_accounts(accounts)


# Упражнение 10.


def task_10():
    summ = 0.
    while True:
        num = input("Введите число.")
        if num.isdigit():
            summ += float(num)
            print(f"сумма: {summ}")
        elif num == "":
            print("Выходим.")
            break
        else:
            print("Это не число.")

# task_10()


# Упражнение 11.


def task_11():
    grades = {"A": 5, "B": 4, "C": 4, "D": 4, "E": 3, "P": 2}
    while True:
        num = input("Введите число: ")
        if num.isdigit() and int(num) in grades.values():
            for k, v in grades.items():
                if v == int(num):
                    print(k)
                    break
        elif num.upper() in grades.keys():
            print(grades[num.upper()])
        elif num == "":
            print("Выходим")
            break
        else:
            print("Введенное значение не является допустимым")

# task_11()
