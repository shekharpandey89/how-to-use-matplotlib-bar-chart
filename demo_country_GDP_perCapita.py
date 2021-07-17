# demo_country_GDP_perCapita.py

import matplotlib.pyplot as plt
Country = ['Singapore','Canada','USA','Qatar','Saudi Arabia']
GDP_PerCapita = [55000,52000,62000,69000,57000]

plt.bar(Country, GDP_PerCapita)
plt.title('Demo Bar Chart')
plt.xlabel('Country')
plt.ylabel('GDP_PerCapita')
plt.show()