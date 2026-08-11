import matplotlib.pyplot as plt

marks=[50,60,65,70,72,75,
80,82,85,90]

plt.hist(marks)
plt.hist(marks,bins=5) # bins 
plt.show()