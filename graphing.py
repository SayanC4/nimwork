import matplotlib.pyplot as plt
import pandas as pd
#dfs = [pd.read_csv("./csvs/Random {1, 2, 3}.csv", header=None)]
dfs = [
  pd.read_csv(f"./csvs/{game}.csv", header=None) for game in [
    "Clever {1, 2, 3}", "Random {1, 2, 3}", 
    "Clever {1, 3, 4}", "Random {1, 3, 4}"
  ]
]

if __name__ == "__main__":
  xax = range(100, 10001, 100)
  colors = ['darkgreen', 'maroon', 'deepskyblue', 
            'goldenrod', 'magenta', 'teal', 'orangered']
  for frame in dfs:
    for x in range(7):
    #if x == 0:# or x == 2:
      plt.gca().set_xlim([100, 10000])
      plt.gca().set_ylim([0.0, 1.0])
      plt.grid(axis='both', color='0.75')
      #plt.axes().set_prop_cycle(color=colors)
      df = frame.iloc[:104, 8*x:8*(x+1)]
      #print(df.head())
      title = df.iloc[0, 0]
      print(title)
      for i in range(1, 8):
        col = df.iloc[3:103, i].astype("float").to_list()
        #print(col[0:20])
        plt.plot(xax, col, color=colors[i - 1])
        print(df.iloc[102, i])
        #plt.axhline(float(df.iloc[102, i]), xmin=100, xmax=10000, color=colors[i], # Error here
        #  label="_nolegend_", linestyle="--")
      #print(len(df.iloc[102, 1:8].astype("float").to_list()))
      #print(len(colors))
      plt.hlines(y=df.iloc[102, 1:8].astype("float").T, 
                 xmin=100, xmax=10000, color=colors, 
                 label="__nolegend__", linestyle="--", alpha=0.5)
      plt.title(title)
      plt.legend(['0.9', '0.8', '0.7', '0.6', '0.5', '0.4', '0.3'], 
                bbox_to_anchor = (1.175, 0.5), loc='center right')
      plt.subplots_adjust(left=0.075, right=0.85, top=0.9, bottom=0.1)
      plt.savefig(f"graphs/{title}.png")
      plt.clf()