import matplotlib.pyplot as pl
import pandas as pd

total = pd.read_csv("./csvs/Clever {1, 2, 3}.csv")

if __name__ == "__main__":
  print(total.head())