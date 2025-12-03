def can_get_discount(age):
    if age >= 65 or age <= 13:
        return True
    else:
        return False

def calculate_discounted_price(price, discount_rate):
    return price * discount_rate

def get_popcorn_price(want_popcorn):
    if want_popcorn == True:
        return 6000
    else:
        return 0
    
def calculate_total(age, want_popcorn):
    age = can_get_discount(age)
    movie = 10000
    if age == True:
        discount = calculate_discounted_price(movie, 0.5)
    else:
        discount = 0

    popcorn = get_popcorn_price(want_popcorn)
    return movie + popcorn - discount

result = calculate_total(10, True)
print(result) 
result = calculate_total(30, False)
print(result)
result = calculate_total(70, True)
print(result)