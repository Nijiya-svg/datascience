import matplotlib.pyplot as plt
rollnos=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
marks=[22,34,56,78,34,56,78,98,65,43,21,24,35,67,89]

plt.xlabel("roll numbers")
plt.ylabel("marks")
plt.scatter(rollnos,marks,color='blue',marker='o')
plt.title("scatter plot of roll no Vs marks")
plt.show()
