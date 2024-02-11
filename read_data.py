import pandas as pd

rows = []
columns = ["Query", "Count"]

with open("medical-questions", "r", encoding="utf-8") as f:
    for line in f.readlines():
        query, count = line[:-1].split("\t")
        rows.append([query, count])
data = pd.DataFrame(columns=columns, data=rows)
data.to_csv("data.csv", index=False)
