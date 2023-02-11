class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self.__orders = list()

    def __use_ingredients(self, order):
        ingredients = self.INGREDIENTS[order]

        for ingredient in ingredients:
            self.MINIMUM_INVENTORY[ingredient] -= 1

    def __search_contains_ingredient(self, order):
        ingredients = self.INGREDIENTS[order]
        for ingredient in ingredients:
            if self.MINIMUM_INVENTORY[ingredient] < 1:
                return False
        return True

    def add_new_order(self, customer, order, day):
        if self.__search_contains_ingredient(order):
            self.__orders.append(
                {"customer": customer, "order": order, "day": day}
            )
            self.__use_ingredients(order)

    def get_quantities_to_buy(self):
        shopping_list = dict()
        for key in self.MINIMUM_INVENTORY:
            if key == "queijo":
                shopping_list[key] = 100 - self.MINIMUM_INVENTORY[key]
            else:
                shopping_list[key] = 50 - self.MINIMUM_INVENTORY[key]

        return shopping_list
