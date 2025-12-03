products = {
    "사과" : 1000,
    "바나나" : 1500,
    "오렌지" : 2000
}

def get_price(products_dict, product_name):
    return products_dict[product_name]

def add_product(product_dict, product_name, price):
    product_dict[product_name] = price
    pass

def increase_price(products_dict, product_name, price):
    products_dict[product_name] = products_dict[product_name]+price
    pass

print(get_price(products, "사과"))  # 1000
add_product(products, "포도", 3000)
print(products)  # {"사과": 1000, "바나나": 1500, "오렌지": 2000, "포도": 3000}
increase_price(products, "사과", 200)
print(get_price(products, "사과"))  # 1200