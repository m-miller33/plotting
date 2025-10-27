import matplotlib.pyplot as plt

def make_hist(count, n_bins):
    plt.hist(count, bins = n_bins)
    plt.title("My Histogram")
    plt.show()

data = [4,2,6,7,5,6,8,5,8,6]
n_bins = 7
make_hist(data, n_bins)
