# horizontal_demo.py

# import the required package
import matplotlib.pyplot as plt

# created two dummy lists for x-axis and y-axis
Country = ['Singapore','Canada','USA','Qatar','Saudi Arabia']
GDP_PerCapita = [55000,52000,62000,69000,57000]

# we using here barh () method (horizontal) not bar () method
plt.barh(Country, GDP_PerCapita)

# set the title of the bar chart
plt.title('Demo Horizontal Bar Chart')

# set the xlable and ylabel of the bar chart
plt.xlabel('Country')
plt.ylabel('GDP_PerCapita')

# finally display the graph
plt.show()