import matplotlib.pyplot as plt

subjects=["Math","Sci","Eng"]

marks=[90,85,95]

plt.bar(subjects,marks)
plt.barh(subjects,marks) # For Horizontal Bar
plt.bar(subjects,marks,color="green") # for color
plt.show()