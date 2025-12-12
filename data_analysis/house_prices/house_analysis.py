import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('house_prices.csv')

print('=== Data Overview ===')
print(f'Rows: {len(df)}, Columns: {len(df.columns)}')
print('\n',df.head())
print('\n',df.info())

print('\n=== Missing Values ===')
print(df.isnull().sum())
median = df['total_bedrooms'].median()
df['total_bedrooms'].fillna(median, inplace=True)

print('\n=== After Filling ===')
print(df.isnull().sum())
'''
plt.figure(figsize=(10, 8))
#틀린거 plt.scatter(df['latitude'], df['longitude'], # 경도 위도 위치 변경
plt.scatter(df['longitude'], df['latitude'],
            c=df['median_house_value'],
            cmap='winter',
            alpha=0.5,
            s=1)
plt.colorbar(label = 'Price')
plt.xlabel('latitude')
plt.ylabel('longitude')
plt.title('latitude or longitude house price')
plt.show()

plt.figure(figsize=(12, 6))
df.boxplot(column = 'median_house_value', by = 'ocean_proximity')
plt.title('Ocean View Price')
plt.suptitle('')
plt.show()

plt.figure(figsize=(10,6))
sns.regplot(x='median_income', y='median_house_value', data=df, scatter_kws={'alpha': 0.3})
plt.title('')
plt.show()
'''
plt.figure(figsize=(10, 8))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0)
plt.title('')
plt.show()