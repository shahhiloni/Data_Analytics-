# Distribution of a variable

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.histplot(tips["total_bill"], bins=20)

plt.show()