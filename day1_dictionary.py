TICKET_PRICES = {
    'Adult':12000,
    'Student':9000,
    'Child':6000
}

def get_price_by_type(ticket_type):
    return TICKET_PRICES[ticket_type]

# --- 테스트 코드 (수정하지 마세요) ---
adult_price = get_price_by_type('Adult')
student_price = get_price_by_type('Student')

print(f"Adult Price: {adult_price}")
print(f"Student Price: {student_price}") 