import matplotlib.pyplot as plt
import pandas as pd
#dfs = [pd.read_csv("./csvs/Random {1, 2, 3}.csv", header=None)]
dfs = [
  pd.read_csv(f"./csvs/{game}.csv", header=None) for game in [
    "Clever {1, 2, 3}", "Random {1, 2, 3}", 
    "Clever {1, 3, 4}", "Random {1, 3, 4}"
  ]
]

"""
Currently messed up:
Random 0.8 {1, 2, 3}, Random 0.8 {1, 3, 4}, Random 0.7 {1, 2, 3}, Random 0.7 {1, 3, 4}
Clever 0.9 {1, 3, 4}
Clever 0.8 {1, 2, 3}, Clever 0.8 {1, 3, 4}, Clever 0.7 {1, 2, 3}, Clever 0.7 {1, 3, 4}
"""

if __name__ == "__main__":
  xax = range(100, 10001, 100)
  colors = ['', 'darkgreen', 'maroon', 'deepskyblue', 
            'goldenrod', 'magenta', 'teal', 'orangered']
  for frame in dfs:
    for x in range(7):
      #if x == 0:# or x == 2:
      plt.gca().set_xlim([100, 10000])
      plt.gca().set_ylim([0.0, 1.0])
      plt.grid(axis='both', color='0.75')
      df = frame.iloc[:104, 8*x:8*(x+1)]
      #print(df.head())
      title = df.iloc[0, 0]
      print(title)
      for i in range(1, 8):
        col = df.iloc[3:103, i].astype("float").to_list()
        #print(col[0:20])
        plt.plot(xax, col, color=colors[i])
        #avg = df.iloc[103, i]
        #plt.axhline(avg, color=colors[i], linestyle='--')
      plt.title(title)
      plt.legend(['0.9', '0.8', '0.7', '0.6', '0.5', '0.4', '0.3'], 
                bbox_to_anchor = (1.175, 0.5), loc='center right')
      plt.subplots_adjust(left=0.075, right=0.85, top=0.9, bottom=0.1)
      plt.savefig(f"graphs/{title}.png")
      plt.clf()