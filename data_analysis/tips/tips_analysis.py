import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('tips.csv')
print(df.head())
print(df.info())

print('=== Correlation ===')
print(df[['total_bill', 'tip']].corr())

print('\n=== Size Correlation ===')
print(df[['size', 'tip']].corr())
print(df[['size','total_bill']].corr())
print(df[['size', 'tip','total_bill']].corr())

print('\n=== Tip Rate ===')
df['tip_rate'] = (df['tip'] / df['total_bill']) * 100
print(df[['tip_rate', 'tip','total_bill']].head())
print(f'\nAverage Tip Rate : {df['tip_rate'].mean():.2f}%')

print('\n=== Tip Rate by Group ===')
sex_tip = df.groupby('sex')['tip_rate'].mean()
print(f'Sex Tip :{sex_tip}%')
smoker_tip = df.groupby('smoker')['tip_rate'].mean()
print(f'Smoker Tip :{smoker_tip}%')

print('\n=== Pivot Table ===')
pivot = df.pivot_table(
    values='tip_rate',
    index='day',
    columns='smoker',
    aggfunc='mean'
)
print(pivot)

print('\n=== Pivot Sex Tip ===')
pivot_sex = df.pivot_table(
    values='tip_rate',
    index='time',
    columns='sex',
    aggfunc='mean'
)
print(pivot_sex)

plt.figure(figsize=(8,6))
sns.heatmap(pivot, annot=True, fmt='.2f', cmap='YlOrRd')
plt.title('heatmap')

plt.figure(figsize=(8,6))
sns.heatmap(pivot_sex, annot=True, fmt='.2f', cmap='YlOrRd')
plt.title('heatmap')
plt.show()