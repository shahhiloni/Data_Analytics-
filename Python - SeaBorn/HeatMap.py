# Correlation matrix or tabular values

import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")

pivot = flights.pivot(index="month", columns="year", values="passengers")

sns.heatmap(pivot, annot=True, cmap="YlGnBu")

plt.show()  