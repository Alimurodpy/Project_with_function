from survey import chose_number
from buy_section import add_product
from database import get_default_database, get_add_database
from history_section import see_history


print(get_default_database())
print("\n\n\n")
print(get_add_database())
print("\n\n\n")

add_product("Drinks", "Kola", 100, 5000, 7000, "piece")
add_product("Drinks", "Kola", 100, 5000, 7000, "piece")
add_product("Electronics", "Telefon", 50, 1000000, 1200000, "piece")

print("\n\n\n")
print(get_default_database())
print("\n\n\n")
print(get_add_database())

print("\n\n\n")
print(see_history())
