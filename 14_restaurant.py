MENU = {
    'sandwich': 10,
    'tea': 3,
    'chips': 2,
}

def get_order():
    order = input("order: ").strip()
    total = MENU.get(order, 0)
    if order == "":
        return -1
    if total == 0:
        print(f"Sorry, we are fresh out of {order} today")
    else:
        print(f"{order} costs {total}")
    return total

def restaurant():
    total = 0
    while True:
        order_val = get_order()
        if order_val == -1:
            break
        total += order_val
        print(f"New total: {total}")
    print(f"Your total is {total}")

restaurant()
