import csv
from typing import Dict, List
from collections import Counter


def read_csv(path_to_file: str):  # -> List[Dict]:
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


def analyze_log(path_to_file: str):
    data = read_csv(path_to_file)

    most_requested_by_maria = most_requested_dish("maria", data)
