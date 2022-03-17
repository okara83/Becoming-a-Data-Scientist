"""
https://edabit.com/challenge/PYEuCAdGJsRS9AABA        EXPERT


Coffee Shop
Write a class called CoffeeShop, which has three instance variables:

name : a string (basically, of the shop)
menu : a list of items (of dict type), with each item containing the item (name of the item), type (whether a food or a drink) and price.
orders : an empty list
and seven methods:

add_order: adds the name of the item to the end of the orders list if it exists on the menu, otherwise, return "This item is currently unavailable!"
fulfill_order: if the orders list is not empty, return "The {item} is ready!". If the orders list is empty, return "All orders have been fulfilled!"
list_orders: returns the item names of the orders taken, otherwise, an empty list.
due_amount: returns the total amount due for the orders taken.
cheapest_item: returns the name of the cheapest item on the menu.
drinks_only: returns only the item names of type drink from the menu.
food_only: returns only the item names of type food from the menu.
IMPORTANT: Orders are fulfilled in a FIFO (first-in, first-out) order.

Examples
tcs.add_order("hot cocoa") ➞ "This item is currently unavailable!"
# Tesha's coffee shop does not sell hot cocoa
tcs.add_order("iced tea") ➞ "This item is currently unavailable!"
# specifying the variant of "iced tea" will help the process

tcs.add_order("cinnamon roll") ➞  "Order added!"
tcs.add_order("iced coffee") ➞ "Order added!"
tcs.list_orders ➞ ["cinnamon roll", "iced coffee"]
# all items of the current order

tcs.due_amount() ➞ 2.17

tcs.fulfill_order() ➞ "The cinnamon roll is ready!"
tcs.fulfill_order() ➞ "The iced coffee is ready!"
tcs.fulfill_order() ➞ "All orders have been fulfilled!"
# all orders have been presumably served

tcs.list_orders() ➞ []
# an empty list is returned if all orders have been exhausted

tcs.due_amount() ➞ 0.0
# no new orders taken, expect a zero payable

tcs.cheapest_item() ➞ "lemonade"
tcs.drinks_only() ➞ ["orange juice", "lemonade", "cranberry juice", "pineapple juice", "lemon iced tea", "vanilla chai latte", "hot chocolate", "iced coffee"]
tcs.food_only() ➞ ["tuna sandwich", "ham and cheese sandwich", "bacon and egg", "steak", "hamburger", "cinnamon roll"]
Notes
Round off due amount up to two decimal places.
"""


class CoffeeShop:

    def __init__(self, name, menu, orders):
        self.name = name
        self.menu = menu
        self.orders = orders

    def add_order(self, order):
        if any(item["item"] == order for item in self.menu):
            self.orders.append(order)
            return "Order added!"
        else: return "This item is currently unavailable!"

    def list_orders(self): return self.orders

    def due_amount(self):
        return round(sum(present["price"] for item in self.orders
                         for present in self.menu
                         if present["item"] == item), 2)

    def fulfill_order(self):
        if self.orders:
            ready_item = self.orders[0]
            self.orders = self.orders[1:]
            return "The {} is ready!".format(ready_item)
        else:  return "All orders have been fulfilled!"

    def cheapest_item(self): return min(self.menu, key=lambda d: d["price"])["item"]

    def drinks_only(self): return [item["item"] for item in self.menu if item["type"] == "drink"]

    def food_only(self): return [item["item"] for item in self.menu if item["type"] == "food"]