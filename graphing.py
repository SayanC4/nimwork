import matplotlib.pyplot as plt
import matplotlib.colors as clr
import pandas as pd
import statistics as st
#dfs = [pd.read_csv("./csvs/Random {1, 2, 3}.csv", header=None)]
dfs = [
  pd.read_csv(f"./csvs/{game}.csv", header=None) for game in [
    "Clever {1, 2, 3}", "Random {1, 2, 3}", 
    "Clever {1, 3, 4}", "Random {1, 3, 4}"
  ]
]
titles = [
  "Clever, {1, 2, 3}",
  "Random, {1, 2, 3}",
  "Clever, {1, 3, 4}",
  "Random, {1, 3, 4}"
]
rolling = 0

if __name__ == "__main__":
  """
  # Heatmap: in col. idx vs. in row idx
  for (frame, title) in zip(dfs, titles):
    vals = frame.iloc[2:104]
    vals.columns = frame.iloc[1]
    avgs = frame.iloc[104:112, 0:8]
    title = f"Std. Dev. - {title}, 100 - 10,000"
    #title = f"Win Rate Deviance - {title}, 100 - 10,000"
    #title = f"Avg. Win Rates - {title}, 100 - 10,000"
    avg_bare = avgs.iloc[1:, 1:].astype(float)
    cvs = avg_bare.copy()
    players = [x / 10 for x in range(9, 2, -1)]
    ticks = range(len(players))
    for i in range(7):
      df = frame.iloc[:104, 8*i:8*(i+1)]
      for j in range(1, 8):
        col = df.iloc[2:102, j].astype("float").to_list()
        #print(df.iloc[1:102, j])
        print(st.stdev(col))
        print(avg_bare.iloc[i, j - 1])
        cvs.iloc[i, j - 1] = st.stdev(col)# / cvs.iloc[i, j - 1]
    #avg_t = pd.DataFrame(
    #  avg_bare.values.T, 
    #  index=avg_bare.index, 
    #  columns=avg_bare.columns)
    #deviance = 1 - (avg_bare + avg_t)
    #""/"
    
    fig, ax = plt.subplots()
    norm = clr.Normalize(vmin=cvs.min().min(),
                         vmax=cvs.max().max())
    #print(norm.vmax)
    #print(f"{deviance.min().min()} - {deviance.max().max()}")
    im = ax.imshow(cvs, cmap="coolwarm", norm=norm)
    ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
    ax.set_xticks(ticks, labels=players)
    ax.set_yticks(ticks, labels=players)
    cmat = im.cmap(im.norm(im.get_array()))
    #d_one = pd.concat(deviance[x] for x in deviance).sort_values()
    #rolling += 0.25 * d_one.mean()
    for i in ticks:
      for j in ticks:
        #val = avg_bare.iloc[i, j]
        val = cvs.iloc[i, j]
        text = ax.text(j, i, f"{val:.3f}", ha="center", va="center", 
                       #color='k' if val > 0.25 and val < 0.75 else 'w')
                       #color='k' if q[0.25] < val and val < q[0.75] else 'w')
                       color='k' if sum(cmat[i, j][:3]) / 3 > 0.55 else 'w')
    ax.set_title(title)
    plt.savefig(f"graphs/{title}.png")
    plt.clf()
  """
  #print(rolling)
  #""" Line graphs
  xax = range(100, 10001, 100)
  colors = ['darkgreen', 'maroon', 'deepskyblue', 
            'goldenrod', 'magenta', 'teal', 'orangered']
  for frame in dfs:
    for x in range(7):
    #if x == 0:# or x == 2:
      plt.gca().set_xlim([100, 10000])
      plt.gca().set_ylim([0.0, 1.0])
      plt.grid(axis='both', color='0.75')
      plt.gca().set_xlabel("Heap Size", fontsize=10, labelpad=5)
      plt.gca().set_ylabel("Player I Win Rate", fontsize=10, labelpad=5)
      #plt.axes().set_prop_cycle(color=colors)
      df = frame.iloc[:104, 8*x:8*(x+1)]
      #print(df.head())
      title = df.iloc[0, 0]
      #print(title)
      for i in range(1, 8):
        col = df.iloc[2:102, i].astype("float").to_list()
        #print(col[0:20])
        plt.plot(xax, col, color=colors[i - 1])
        #print(df.iloc[102, i])
        #plt.axhline(float(df.iloc[102, i]), xmin=100, xmax=10000, color=colors[i], # Error here
        #  label="_nolegend_", linestyle="--")
      #print(len(df.iloc[102, 1:8].astype("float").to_list()))
      #print(len(colors))
      plt.hlines(y=df.iloc[102, 1:8].astype("float").T, 
                 xmin=100, xmax=10000, color=colors, 
                 label="__nolegend__", linestyle="--", alpha=0.5)
      plt.title(title[:12] + 'accuracy ' + title[12:])
      plt.legend(['0.9', '0.8', '0.7', '0.6', '0.5', '0.4', '0.3'], 
                bbox_to_anchor = (1.185, 0.5), loc='center right',
                title="Opponent\nAccuracy")
      plt.subplots_adjust(left=0.11, right=0.85, top=0.92, bottom=0.12)
      plt.savefig(f"graphs/{title}.png")
      plt.clf()
#"""
  plt.close('all')