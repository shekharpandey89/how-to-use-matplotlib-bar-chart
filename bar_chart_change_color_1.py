# bar_chart_change_color_1.py

# import the matplotlib.pyplot package
import matplotlib.pyplot as plt

# Created two lists for x-axis and y-axis
Country = ['Singapore','Canada','USA','Qatar','Saudi Arabia']
GDP_PerCapita = [55000,52000,62000,69000,57000]

# pass both lists into the bar() method and here we change the width
# size value from 0.8 (default) to 0.5
# and the color=green
plt.bar(Country, GDP_PerCapita,width=0.5,color='green')

# set the title name
plt.title('Demo Bar Chart change the colour')

# set the xlable name
plt.xlabel('Country')

# set the ylabel name
plt.ylabel('GDP_PerCapita')

# draw the graph
plt.show()