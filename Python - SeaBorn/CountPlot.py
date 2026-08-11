# Frequency of categories

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.countplot(data=tips, x="day")

plt.show()