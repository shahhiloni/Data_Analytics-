import matplotlib.pyplot as plt

data=[40,30,20,10]

labels=["A","B","C","D"]

plt.pie(data,labels=labels)
plt.pie(data,
labels=labels,
autopct="%1.1f%%")  # for Percentage

explode=(0,0.2,0,0)

plt.pie(data,
labels=labels,
explode=explode) # for explode

plt.show()