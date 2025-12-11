import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('titanic.csv')

print('=== Data Shpae ===')
print(f'Rows: {len(df)}, Columns: {len(df.columns)}')

print('\n=== First 5 Rows === ')
print(df.head())

print('\n=== Column Info ===')
print(df.info())

print('\n=== Survival Rate ===')
survival_rate = df['Survived'].mean() * 100
print(f'Total: {survival_rate:.2f}%')

print('\n=== Survival by Gender ===')
male = df[df['Sex'] == 'male']['Survived'].mean() * 100
print(f'male: {male:.2f}%')
female = df[df['Sex'] == 'female']['Survived'].mean() * 100
print(f'female: {female:.2f}%')

print('\n=== Survival by Class ===')
class1 = df[df['Pclass'] == 1 ]['Survived'].mean() * 100
print(f'Class1: {class1:.2f}%')
class2 = df[df['Pclass'] == 2 ]['Survived'].mean() * 100
print(f'Class2: {class2:.2f}%')
class3 = df[df['Pclass'] == 3 ]['Survived'].mean() * 100
print(f'Class3: {class3:.2f}%')

print('\n=== Survival by Age Group ===')
children = df[df['Age'] <= 12]['Survived'].mean() * 100
print(f'Children: {children:.2f}%')
teenagers = df[(df['Age'] > 12) & (df['Age'] <= 19)]['Survived'].mean() * 100
print(f'Teenagers: {teenagers:.2f}%')
adults = df[(df['Age'] > 19) & (df['Age'] <= 29)]['Survived'].mean() * 100
print(f'Adults: {adults:.2f}%')
elderly = df[df['Age'] > 60]['Survived'].mean() * 100
print(f'Elderly: {elderly:.2f}%')

plt.figure(figsize=(8,6))
class_survival = df.groupby('Pclass')['Survived'].mean() * 100
plt.bar(class_survival.index, class_survival.values)
plt.title('Survival Rate by Sex')
plt.xlabel('Sex')
plt.ylabel('Survival Rate(%)')
plt.ylim(0, 100)

plt.figure(figsize=(8,6))
gender_survival = df.groupby('Sex')['Survived'].mean() * 100
plt.bar(gender_survival.index, gender_survival.values)
plt.title('Survival Rate by Gender')
plt.xlabel('Gender')
plt.ylabel('Survival Rate(%)')
plt.ylim(0, 100)
plt.show()