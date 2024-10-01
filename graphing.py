import matplotlib.pyplot as pl
import pandas as pd

total = pd.read_csv("./csvs/Clever {1, 2, 3}.csv")

if __name__ == "__main__":
  for x in range(7): 
    data = df.iloc[:104, 8*x:8*(x+1)]
    title = data.iloc[0, 0]
    
