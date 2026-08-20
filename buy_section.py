from database import get_default_database, get_finance, get_add_database
from history_section import add_action
from decorators import log_decarator

default_database = get_default_database()
finance = get_finance()
add_database = get_add_database()



"""
database = {
    "electronics": {
        "telefon": {
                "quantity": 100,
                "buy_price": 1000000,
                "sell_price": 1200000,
                "unit": "piece"
    }
"""

@log_decarator
def add_product(product_family, product_name, quantity, buy_price, sell_price, unit):
    if product_family not in default_database.keys():
        default_database[product_family] = {
            product_name: {
                "quantity": quantity,
                "buy_price": buy_price,
                "sell_price": sell_price,
                "unit": unit
            }
        }
        add_database[product_family] = {
            product_name: {
                "quantity": quantity,
                "buy_price": buy_price,
                "sell_price": sell_price,
                "unit": unit
            }
        }
        print("########################################")
        print(add_database)


        finance["expense"] += quantity * buy_price
        add_action("buy", product_name, quantity, buy_price)


    elif product_name not in default_database[product_family].keys():
        default_database[product_family][product_name] = {
            "quantity": quantity,
            "buy_price": buy_price,
            "sell_price": sell_price,
            "unit": unit
        }
        add_database[product_family][product_name] = {
            "quantity": quantity,
            "buy_price": buy_price,
            "sell_price": sell_price,
            "unit": unit
        }

        finance["expense"] += quantity * buy_price
        add_action("buy", product_name, quantity, buy_price)

    else:
        default_database[product_family][product_name]["quantity"] += quantity
        new_quantity = add_database[product_family][product_name]["quantity"] + quantity

        add_database[product_family] = {
            product_name: {
                "quantity": new_quantity,
                "buy_price": buy_price,
                "sell_price": sell_price,
                "unit": unit
            }
        }

        finance["expense"] += quantity * buy_price
        add_action("buy", product_name, quantity, buy_price)


