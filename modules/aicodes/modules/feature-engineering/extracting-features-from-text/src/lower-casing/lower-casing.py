import pandas as pd

# Settings.
pd.set_option("display.max_colwidth", None)
full_df = pd.read_csv("../Train_rev1.csv")

# Get only "df_FullDescription" column/feature.
df_FullDescription = full_df[["FullDescription"]]
df_FullDescription = df_FullDescription.astype({'FullDescription': 'string'}).head(3)  # Get only 3 rows.

# Add new column "processed_FullDescription" to the DataFrame.
df_FullDescription["processed_FullDescription"] = df_FullDescription["FullDescription"].str.lower()
print(df_FullDescription.head())
