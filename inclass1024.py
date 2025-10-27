import matplotlib.pyplot as plt

data = [4,5,6,9,2,3]
plt.hist(data, bins = 6)
plt.ylabel("counts")
plt.title("measuring height in inches")

plt.show()


