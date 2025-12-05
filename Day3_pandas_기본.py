import pandas as pd
'''
#문제: 데이터프레임 만들기
data = {
    "이름": ["현기", "철수", "영희"],
    "나이": [28, 25, 30],
    "점수": [85, 90, 88]
}

df = pd.DataFrame(data)

print(df['나이'])

print(df.loc[2])

# 개념: 조건 필터링
data = {
    "이름": ["현기", "철수", "영희", "민수"],
    "나이": [28, 25, 30, 22],
    "점수": [85, 90, 88, 75]
}
df = pd.DataFrame(data)

print(df[df['점수']>= 80])

print(df[df['나이']<=26])

# 개념: 새 열 추가
data = {
    "이름": ["현기", "철수", "영희"],
    "키": [175, 180, 165],
    "몸무게": [70, 75, 55]
}
df = pd.DataFrame(data)

df['BMI'] = df['몸무게'] / ((df['키'] / 100) ** 2)

df['비만'] = df["BMI"] >= 25

print(df)

# 개념: 통계 함수
data = {
    "이름": ["현기", "철수", "영희", "민수", "지수"],
    "수학": [85, 90, 88, 75, 95],
    "영어": [80, 85, 90, 70, 88]
}
df = pd.DataFrame(data)

math_avg = df['수학'].mean()
print(f'{math_avg}')

eng_max = df['영어'].max()
print(f'{eng_max}')

math_sum = df['수학'].sum()
print(f'{math_sum}')

#문제: 정렬

import pandas as pd

data = {
    "이름": ["현기", "철수", "영희", "민수"],
    "나이": [28, 25, 30, 22],
    "점수": [85, 90, 88, 75]
}
df = pd.DataFrame(data)

df1 = df.sort_values('점수')
print(df1)

df2 = df.sort_values('나이', ascending=False)
print(df2)
'''