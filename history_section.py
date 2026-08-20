from database import get_history

history = get_history()

def add_action(type, product, quantity, price):
    history.append({
        "type": type,
        "product": product,
        "quantity": quantity,
        "price": price,
        "total": quantity * price
    })
    
def see_history():
    return history
