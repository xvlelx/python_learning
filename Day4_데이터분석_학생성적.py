import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('students.csv', encoding='utf-8')

print('=====데이터 첫 5줄====')
print(df.head())

print('=====데이터 정보====')
print(df.info())

print('=====과목별 평균 점수====')
print(df[['수학','영어','과학']].mean())

print('=====과목별 최고 점수====')
print(df[['수학','영어','과학']].max())

print('=====과목별 최저 점수====')
print(df[['수학','영어','과학']].min())

print('=====총점과 평균점수====')
df['총점'] = df['수학'] + df['영어'] + df['과학']
df['평균'] = df['총점'] / 3
print(df)

print("\n=== 총점 순위 ===")
print(df.sort_values('총점',ascending=False))

print("\n=== 평균 85점 이상 우수 학생 ===")
print(df[df['평균'] >= 85])

print("\n=== 반별 평균 점수 ===")
print('A반평균 :', df[df['반'] == 'A']['평균'].mean())
print('B반평균 :', df[df['반'] == 'B']['평균'].mean())
'''
plt.figure(figsize=(10,6))
subject_avg = df[['수학','영어','과학']].mean()
plt.bar(subject_avg.index, subject_avg.values)
plt.title('과목별 평균 점수')
plt.xlabel('과목')
plt.ylabel('평균 점수')
plt.ylim(0,100)
plt.figure(figsize=(10,6))
plt.bar(df['이름'], df['총점'])
plt.title('학생별 총 점수')
plt.xlabel('이름')
plt.ylabel('총점')
plt.ylim(0, 300)
plt.show()
'''