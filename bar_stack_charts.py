# bar_stack_charts.py

# impor the required package
import matplotlib.pyplot as plt

# created two dummy data lists
data_1 = [25,83, 76, 45, 53]
data_2 = [45, 37, 25, 11, 19]

# pass dummy lists into the bar () method and also mentioned which data
# will be in bottom with the bottom parameter
plt.bar(range(len(data_1)), data_1)
plt.bar(range(len(data_2)), data_2, bottom=data_1)

# finally display the bar stack graph
plt.show()