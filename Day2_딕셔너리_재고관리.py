shop = {
    '사과':{'재고':50}
}
def check_stock(shop_dict, product_name):
    return shop_dict[product_name]['재고']

def sell_product(shop_dict, product_name, quantuty):
    current = check_stock(shop_dict, product_name)

    if current < quantuty:
        print('재고부족')
    else:
        shop_dict[product_name]["재고"] -= quantuty
        print('판매완료')

sell_product(shop, "사과", 10)  # 판매 완료
print(check_stock(shop, "사과"))  # 40