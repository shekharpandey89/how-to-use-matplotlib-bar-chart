# bar_chart_sorted_order.py

# import the matplotlib.pyplot package
import matplotlib.pyplot as plt

# Created two lists for x-axis and y-axis
Country = ['Singapore','Canada','USA','Qatar','Saudi Arabia']
GDP_PerCapita = [55000,52000,62000,69000,57000]
colors = ['purple', 'gold', 'red', 'green', 'blue']

# Sort the lists
GDP_sorted = sorted(GDP_PerCapita)
Country_ordered = [x for _, x in sorted(zip(GDP_PerCapita,Country ))]

print("Country_ordered", Country_ordered)

# pass both lists into the bar() method and here we change the width
# size value from 0.8 (default) to 0.5
# and the color=green
plt.bar(Country_ordered, GDP_sorted,width=0.5,color=colors)

# set the title name
plt.title('Demo Bar Chart sorted order')

# set the xlable name
plt.xlabel('Country')

# set the ylabel name
plt.ylabel('GDP_PerCapita')

# draw the graph
plt.show()