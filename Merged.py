import pandas as pd

# Source Data
df_source = pd.DataFrame(
    {
    "ID": [1, 2, 3],
    "NAME": ["A", "B", "C"]
}
)

# Target Data
df_target = pd.DataFrame(
    {
    "ID": [1, 2, 4],
    "NAME": ["A", "B", "D"]
}
)

print(df_source)
print(df_target)
# a = df_source.equals(df_target)
# print(a)
#
# b = df_source.compare(df_target)
# print(b)


# Merge
merged = df_source.merge(
    df_target,
    on="ID",
    how="outer",
    suffixes=("_source", "_target"),
    indicator=True
)

#SELECT * FROM T1 LEFT JOIN T2 ON ID=ID AND

print("Merged Data:")
print(merged)

# Filter common records
common_records = merged[  merged["_merge"]  == "both" ]

print("\nCommon Records:")
print(common_records)
