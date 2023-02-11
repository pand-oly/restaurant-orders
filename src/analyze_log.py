import csv
from typing import Dict, List, Set
from collections import Counter


def read_csv(path_to_file: str) -> List[Dict]:
    """Responsible for reading the csv file"""
    if path_to_file.endswith(".csv"):
        try:
            with open(path_to_file, "r") as file:
                data = csv.DictReader(
                    file,
                    delimiter=",",
                    fieldnames=["cliente", "pedido", "dia"],
                )
                return [product for product in data]
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")


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


def write_return(requirements: Dict) -> None:
    string = ""
    for value in requirements.values():
        string += f"{value}\n"

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(string)


def analyze_log(path_to_file: str) -> None:
    data = read_csv(path_to_file)

    most_requested_by_maria = most_requested_dish("maria", data)
    arnaldo_order_hamburguer = how_many_times__order_this_dish(
        "hamburguer", "arnaldo", data
    )
    dishes_joao_never_order = dishes_were_not_ordered("joao", data)
    days_that_joao_never_went = search_day_not_attend("joao", data)

    write_return(
        {
            1: most_requested_by_maria,
            2: arnaldo_order_hamburguer,
            3: dishes_joao_never_order,
            4: days_that_joao_never_went,
        }
    )
