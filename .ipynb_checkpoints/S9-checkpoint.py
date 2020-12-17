import pandas as pd

with open("ramen-ratings.csv", "rt", encoding="UTF-8") as csv_file:
    print(csv_file.read())

ramen_df = pd.read_csv("ramen-ratings.csv")
ramen_df.head()