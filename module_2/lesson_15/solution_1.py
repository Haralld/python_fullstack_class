"""Какаято прога добавляющая клиента"""


def add_client(name, history):
    """
    надо что бы pylint не ругался
    """
    # создает клиента
    client_id = len(history) + 1
    history[client_id] = {"name": name, "orders": []}


def make_order(client_id, history, order_details):
    """
    и тут должна быть доп инфа
    """
    # добавляет клиента
    history[client_id]["orders"].append(order_details)


def get_history(client_id, history):
    """
    такая же песня как и в функции выше
    """
    # история
    return history[client_id]["orders"]


client_history = {}

add_client("Roman", client_history)
make_order(1, client_history, {"order_id": 1, "amount": 100})

print(get_history(1, client_history))
