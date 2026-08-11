import matplotlib.pyplot as plt

plt.subplot(1,2,1)
plt.plot([1,2],[3,4])
plt.subplot(1,2,2)
plt.plot([1,2],[4,3])
plt.savefig("graph.png")

plt.show()