'''

  Authors: Daniel Navarro DeGiorgio (1167827), Jonas Matulis (1194815)
  Previous Author(s): Andrew Hamilton-Wright, Kassy Raymond
  python Q3_graph_script.py plot.csv plot.png

'''

import sys
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import ticker as ticktools


def main(argv):
    
  if len(argv) != 3:
    print("Usage: Q3_graph_script.py <data file> <graphics file>")
    sys.exit(-1)

  csv_filename = argv[1]
  graphics_filename = argv[2]
    

    #
    # Open the data file using "pandas", which will attempt to read
    # in the entire CSV file
    #
  try:
    csv_df = pd.read_csv(csv_filename)

  except IOError as err:
    print("Unable to open source file", csv_filename, ": {}".format(err), file=sys.stderr)
    sys.exit(-1)
  
  fig = plt.figure()
  #fig.suptitle('Ethno-Racial Group')
  plt.rcParams["figure.figsize"] = [7.00, 3.50]
  plt.rcParams["figure.autolayout"] = True

    #create funtion
  axs = sns.lineplot(x = 'date', y = 'Difference Between Share of Covid and Share of Population', hue = 'race', data = csv_df)
  plt.xticks(rotation = 45, ha = 'right')
  axs.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25),
          fancybox=True, shadow=True)
  # for us to a file
  fig.savefig(graphics_filename, bbox_inches="tight")
  plt.show()

main(sys.argv)
