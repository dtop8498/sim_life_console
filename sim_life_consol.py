import time

perf_list = {1:"Магазин",
             2:"Работать",
             3:"Статистика",
             4:"Выход"
             }
job_list = {1:["Собирать бутылки", 30, 10],
            2:["Пахать на заводе", 200, 40],
            3:["Чистить атомный реактор", 750, 50]
            }

shop_list = {1:["Машина", 500],
             2:["Крутой телефон", 350],
             3:["Обед в kfc", 20]
             }

class Player:
    def __init__(self, name):
        self.name = name
        self.__balance = 100
        self.__inventory = []

    def get_stats(self):
        return f"Имя: {self.name}, Баланс: {self.__balance}, Инвентарь: {self.__inventory}"

    def get_balance(self, value):
        self.__balance += value

    def withdraw_balance(self, value):
        self.__balance -= value


    def add_inventory(self, item, cost):
        self.withdraw_balance(cost)
        self.__inventory.append(item)



def choice_actions(obj):
    for i in perf_list:
        print(f"{i} : {perf_list[i]}")
    player_choice = int(input("Сделайте выбор: "))
    for i in perf_list:
        if player_choice == i:
            print(f"Вы выбрали: {perf_list[i]}")
    if player_choice == 3:
        print(obj.get_stats())
        input("Нажмите любую клавишу чтобы продолжить...")
    elif player_choice == 2:
        for i in job_list:
            print(f"{i} : {job_list[i][0]}, Зарплата: {job_list[i][1]}, Время: {job_list[i][2]}")
        job_choice = int(input("Выберите тип работы: "))
        job_actions(obj, job_choice)
    elif player_choice == 1:
        for i in shop_list:
            print(f"{i} : {shop_list[i][0]}, Цена: {shop_list[i][1]}")
        item_choice = int(input("Выберите предмет: "))
        shop_action(obj, item_choice)
    elif player_choice == 4:
        print("Спасибо за игру")
        return "stop"


def job_actions(obj, player_choice):
    if player_choice == 1:
        timers(10)
        obj.get_balance(30)
    elif player_choice == 2:
        timers(40)
        obj.get_balance(200)
    elif player_choice == 1:
        timers(50)
        obj.get_balance(750)


def shop_action(obj, player_choice):
    cost = shop_list[player_choice][1]
    item_name = shop_list[player_choice][0]
    obj.add_inventory(item_name, cost)


def timers(value):
    counter = 0
    last_time = time.time()

    print("Работа началась:\n")

    while True:
        if counter >= value:
            print("Работа закончилась!")
            break
        # Проверяем, не прошла ли секунда
        current = time.time()
        if current - last_time >= 1:
            counter += 1
            last_time = current
            print(f"🕐 Время! Счётчик: {counter}")

def main():
    player1 = Player("Bob")
    while True:
        result = choice_actions(player1)
        if result == "stop":
            break
if __name__ == "__main__":
    main()