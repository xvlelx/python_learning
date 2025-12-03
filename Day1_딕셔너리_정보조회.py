TICKET_PRICES = {
    'Adult' : 15000,
    'Senior' : 7000
}

all_key = TICKET_PRICES.keys()

all_prices = TICKET_PRICES.values()

all_items = TICKET_PRICES.items()

print(f'All key Type: {type(all_key)}')
print(f'All prices type: {type(all_prices)}')
print(f'All items type: {type(all_items)}')