import matplotlib.pyplot as plt

x=[1,2,3,4]

y1=[2,4,6,8]
y2=[1,3,5,7]

plt.plot(x,y1)
plt.plot(x,y2)

plt.plot(x,y1,label="Science")
plt.plot(x,y2,label="Math")

plt.legend() # legend
plt.figure(figsize=(8,5)) # figure


plt.show()