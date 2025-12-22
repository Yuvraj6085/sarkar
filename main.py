import pandas as pd

df = pd.read_csv("vinit.csv")
# print(df)
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())

# print(df["Name"])
# print(df[["Name", "Marks", "City"]])

# print(df.loc[0])
# print(df.iloc[3])

# filtered
# print(df[df["Marks"] > 80])
# print(df[df["Gender"] == "Female"])
# print(df[(df["Course"] == "BCA") & (df["Year"] == 2)])

print(df.isnull().sum())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print(df)


print(df.isnull().sum())

df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

print(df["Result"])

df["Grade"] = pd.cut(
    df["Marks"],
    bins=[0,40,60,75,100],
    labels=["Fail","C","B","A"]
)
print(df["Grade"])

print(df.sort_values("Marks", ascending=False))

print(df.groupby("Course")["Marks"].mean())

result = df.groupby("Gender").agg({
    "Marks": ["mean", "max"],
    "Attendance": "mean"
})
print(result)

result.columns = ["Marks_Avg", "Marks_Max", "Attendance_Avg"]
print(result)


df["City"].value_counts()
df["Scholarship"].value_counts()


df["Name"].str.upper()
df["Remarks"].str.contains("Good")

df["ExamDate"] = pd.to_datetime(df["ExamDate"])

df["ExamYear"] = df["ExamDate"].dt.year
df["ExamDay"] = df["ExamDate"].dt.day


df.rename(columns={"Marks":"TotalMarks"}, inplace=True)

df.drop("Remarks", axis=1, inplace=True)


df.to_csv("final_output.csv", index=False)
df.to_excel("final_output.xlsx", index=False)
