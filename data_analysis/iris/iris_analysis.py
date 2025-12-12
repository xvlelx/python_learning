import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('iris.csv')

print('=== Data Shape ===')
print(f'Rows :{len(df)}, Columns :{len(df.columns)}')

print('\n=== First 5 Rows ===')
print(df.head())

print('\n=== Column Info ===')
print(df.info())

print('\n=== Speies Count ===')
print(df['species'].value_counts())

print('\n=== Average by Species ===')
print(df.groupby('species').mean())

print('\n=== Lage Flowers ===')
large = df[df['petal_length'] > 5.0]
print(f'Count: {len(large)}')
print(large['species'].value_counts())
'''
plt.figure(figsize=(10, 6))
for species in df['species'].unique():
    data = df[df['species'] == species]
    plt.scatter(data['petal_length'],data['petal_width'], label=species)
plt.xlabel('petal_length')
plt.ylabel('petal_width')
plt.title('length vs width')
plt.legend()
plt.show()
'''
plt.figure(figsize=(10, 6))
df.boxplot(column='petal_length', by='species')
plt.title('species petal_length')
plt.show()