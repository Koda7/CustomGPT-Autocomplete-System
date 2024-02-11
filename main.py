import pandas as pd
import json


def main():
    data = pd.read_csv("data.csv")
    lookup = {}
    for index, row in data.iterrows():
        query, count = row.values
        pref = ""
        for c in query:
            pref += c
            lookup.setdefault(pref, []).append((count, index))

    for key, value in lookup.items():
        lookup[key] = sorted(value, key=lambda x: x[0])

    with open("lookup.json", "w") as f:
        json.dump(lookup, f)


if __name__ == "__main__":
    main()
