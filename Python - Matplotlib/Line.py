import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[20,40,30,60,50]

plt.plot(x,y,color="red") # for color
plt.plot(x,y,linewidth=5) # for width 
plt.plot(x,y,linestyle="--") # for style 
plt.plot(x,y,marker="o") # for Marker (o, *, +, x, s, ^, D)
plt.plot(x,y,marker="o",markersize=10) # for marker size
plt.plot(x,y,marker="o",
markerfacecolor="red") # for marker color

plt.show()