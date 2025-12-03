def is_heavy(weight):
    if weight >= 5:
        return True
    else:
        return False

def is_far(distance):
    if distance >= 100:
        return True
    else:
        return False
    
def calculate_extra_fee(is_heavy_package, is_far_distance):
    price = 0

    if is_heavy_package and is_far_distance == True:
        return price + 5000
    elif is_heavy_package or is_far_distance == True:
        return price + 3000
    elif is_heavy_package and is_far_distance == False:
        return 0
    else:
        return 0
    
def calculate_shipping_fee(weight, distance):
    value = 3000
    weight = is_heavy(weight)
    distance = is_far(distance)
    free = calculate_extra_fee(weight, distance)
    
    result = value + free
    return result


result = calculate_shipping_fee(7, 150)
print(result)  # 8000 (기본 3000 + 추가 5000)

result = calculate_shipping_fee(3, 150)
print(result)  # 6000 (기본 3000 + 추가 3000)

result = calculate_shipping_fee(3, 50)
print(result)  # 3000 (기본 3000 + 추가 0)