import csv
from typing import Dict, List, Set
from collections import Counter


def read_csv(path_to_file: str) -> List[Dict]:
    """Responsible for reading the csv file"""
    with open(path_to_file) as file:
        data = csv.DictReader(
            file, delimiter=",", fieldnames=["cliente", "pedido", "dia"]
        )
        return [product for product in data]


def most_requested_dish(name: str, orders: List[Dict]) -> int:
    """receive the parameters
      * name type string - name of the customer you want to search for
      * orders type list of dict - with restaurant order list

    looks and returns up a person's most ordered dish in an order list"""

    const = [order["pedido"] for order in orders if order["cliente"] == name]
    return Counter(const).most_common(1)[0][0]


def how_many_times__order_this_dish(
    dish: str, name: str, orders: List[Dict]
) -> int:
    """takes 3 parameters:
      * dish type string - dish name for search
      * name type string - name of the customer you want to search for
      * orders type list of dict - with restaurant order list

    returns how many times the customer ordered the dish"""

    const = [order["pedido"] for order in orders if order["cliente"] == name]
    return Counter(const)[dish]


def dishes_were_not_ordered(name: str, orders: List[Dict]) -> Set:
    """receive the parameters
      * name type string - name of the customer you want to search for
      * orders type list of dict - with restaurant order list

    returns which dishes were not ordered by the customer"""
    dishes = set()
    orders_customer = list()

    for order in orders:
        dishes.add(order["pedido"])

        if order["cliente"] == name:
            orders_customer.append(order["pedido"])

    return {dish for dish in dishes if dish not in orders_customer}


def search_day_not_attend(name: str, orders: List[Dict]) -> Set:
    """receive the parameters
      * name type string - name of the customer you want to search for
      * orders type list of dict - with restaurant order list

    returns the day that the customer did not go to the restaurant"""
    days = set()
    orders_customer = list()

    for order in orders:
        days.add(order["dia"])

        if order["cliente"] == name:
            orders_customer.append(order["dia"])

    return {day for day in days if day not in orders_customer}


def analyze_log(path_to_file: str):
    data = read_csv(path_to_file)

    most_requested_by_maria = most_requested_dish("maria", data)

    arnaldo_order_hamburguer = how_many_times__order_this_dish(
        "hamburguer", "arnaldo", data
    )

    dishes_joao_never_order = dishes_were_not_ordered("joao", data)
    days_that_joao_never_went = search_day_not_attend("joao", data)
