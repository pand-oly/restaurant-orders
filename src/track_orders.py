from collections import Counter
from .analyze_log import (
    most_requested_dish,
    dishes_were_not_ordered,
    search_day_not_attend,
)


class TrackOrders:
    def __init__(self) -> None:
        self.__orders = list()
        self.__length = 0

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return self.__length

    def add_new_order(self, customer, order, day):
        if customer and order and day:
            self.__orders.append(
                {"customer": customer, "order": order, "day": day}
            )
            self.__length += 1
            return 0

        raise ValueError("no value can be None")

    def get_most_ordered_dish_per_customer(self, customer):
        return most_requested_dish(customer, self.__orders)

    def get_never_ordered_per_customer(self, customer):
        return dishes_were_not_ordered(customer, self.__orders)

    def get_days_never_visited_per_customer(self, customer):
        return search_day_not_attend(customer, self.__orders)

    def get_busiest_day(self):
        orders_days_data = [order["day"] for order in self.__orders]
        return Counter(orders_days_data).most_common(1)[0][0]

    def get_least_busy_day(self):
        orders_days_data = [order["day"] for order in self.__orders]
        return Counter(orders_days_data).most_common()[::-1][0][0]
