import matplotlib.pyplot as plt

x=[1,2,3,4,5]

y=[10,25,15,40,35]

plt.scatter(x,y)
plt.scatter(x,y,color="red") # for color
plt.scatter(x,y,s=200) # for size
plt.fill_between(x,y)

plt.show()  