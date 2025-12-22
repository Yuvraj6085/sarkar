import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)

s = pd.Series([100, 200, 300], index=["a", "b", "c"])

data = {"Math": 80, "Science": 90, "English": 85}
s = pd.Series(data)

s.values      # data
s.index       # index
s.dtype       # data type
s.shape
s.size
s.ndim


s[0]
s["a"]

s[0:2]



s[1] = 500
s["a"] = 999


s + 10
s * 2
s - 5
s / 2

s1 = pd.Series([10,20,30])
s2 = pd.Series([5,10,15])

s1 + s2

s > 50
s[s > 50]


s.sum()
s.mean()
s.min()
s.max()
s.std()
s.count()


s.sort_values()
s.sort_index()


s.isnull()
s.notnull()

s.fillna(0)
s.dropna()

s.unique()
s.nunique()
s.value_counts()


s.apply(lambda x: x * 10)

s.tolist()
s.to_numpy()


s.astype(int)
s.astype(float)


s = pd.Series(["apple", "banana", "mango"])

s.str.upper()
s.str.lower()
s.str.contains("a")
s.str.len()


s = pd.to_datetime(pd.Series(["2024-01-01", "2024-02-01"]))

s.dt.year
s.dt.month
s.dt.day


s.index = ["x", "y", "z"]
s.reset_index(drop=True)


s2 = s.copy()


s.where(s > 50, "Low")


s.replace(0, 100)

s1.add(s2, fill_value=0)

grade = {"A":90, "B":80, "C":70}
s.map(grade)

s.cumsum()
s.cummax()
s.cummin()

s.rank()


s.clip(lower=40, upper=90)

s.between(50, 90)


s.memory_usage()
