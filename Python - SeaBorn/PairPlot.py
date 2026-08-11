# Relationships among multiple variables

import seaborn as sns

iris = sns.load_dataset("iris")

sns.pairplot(iris, hue="species")