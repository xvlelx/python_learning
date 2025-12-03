def can_use_coupon(total_price, coupon_min):
    if total_price >= coupon_min:
        return True
    else:
        return False
    
def apply_coupon(price, discount_rate):
    return price * discount_rate

def calculate_shipping(price):
    if price >= 50000:
        return 0
    else:
        return 3000

def calculate_final_price(price, coupon_min, discount_rate):
    coupon = can_use_coupon(price, coupon_min)
    if coupon == True:
        discount = apply_coupon(price, discount_rate)
    else:
        discount = 0
    
    shipping = calculate_shipping(price)
    final = price - discount + shipping
    return final

def print_order(name, price, coupon_min, discount_rate):
    result = calculate_final_price(price, coupon_min, discount_rate)
    print(f'[{name}][{price}][{coupon_min}][{result}]')


print_order("현기", 60000, 50000, 0.1)
print_order("철수", 30000, 50000, 0.1)