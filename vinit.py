# pip install pandas
# version check:  print(pd.__version__)
# how to import pandas

import pandas as pd


# Data Dictionary ke format mein hota hai
data = {
    'Name': ['Yashika', 'Vinit'],
    'City': ['Ludhiana', 'Jaipur'],
    'Marks': [95, 90]
}

# DataFrame banana (Table create karna)
df = pd.DataFrame(data)

print(df)
# DataFrame ko CSV file mein save karna
df.to_csv('students.csv', index=False)
print("CSV file 'students.csv' created successfully.")

# CSV file ko read karna
df_read = pd.read_csv('students.csv')
print("\nData read from 'students.csv':")
print(df_read)

# Upar ki 5 rows dekhne ke liye
print(df.head()) 

# Neeche ki 5 rows dekhne ke liye
print(df.tail())

# Data ki kundali (Data Types, Null values, Memory)
print(df.info())

# Sirf ek column dekhna
print(df['Name'])

# FILTERING (Ye sabse important hai)
# Sirf wo log jinke marks 90 se jyada hain
toppers = df[df['Marks'] > 90]
print(toppers)

# Naya column add karna (Sabko 'A' grade de diya)
df['Grade'] = 'A'

# Kisi column ko hatana (axis=1 ka matlab column hota hai)
df = df.drop('City', axis=1)

print(df)

# Ye function magic hai. Count, Mean, Min, Max sab ek saath dega
print(df.describe())

# Alag se nikalna ho
print("Average Marks:", df['Marks'].mean())
print("Highest Marks:", df['Marks'].max())
print("Lowest Marks:", df['Marks'].min())