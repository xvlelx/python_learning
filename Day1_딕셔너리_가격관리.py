TICKET_PRICES = {
    'Adult':12000,
    'Student':9000,
    'Child':6000,
    'Senior':7000
}

removed_child_price = 0

del TICKET_PRICES['Student']

Child.pop() = removed_child_price


print(f"Removed Child Price: {removed_child_price}")
print(f"Current Keys in Dictionary: {TICKET_PRICES.keys()}")