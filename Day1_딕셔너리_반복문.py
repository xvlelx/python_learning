TICKET_PRICES = {
    'Adult': 15000,
    'Senior': 7000
}

# 1. 딕셔너리 자체를 반복하여 키만 출력하는 코드 작성

# 2. .items()를 사용하여 키와 값을 함께 출력하는 코드 작성
# 출력 예시: Adult ticket price is 15000 won.


# --- 테스트 코드 (수정하지 마세요) ---
print("--- 1. Keys Only ---")
for i in TICKET_PRICES:
    print(f'{i}')
print("--- 2. Key and Value ---")
for key, value in TICKET_PRICES.items():
    print(f'{key},{value}')