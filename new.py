import matplotlib.pyplot as plt

# List of years
year = [2000, 2005, 2010, 2015, 2020, 2025]

# Corresponding population data (in millions)
pop = [6.12, 6.52, 6.92, 7.35, 7.79, 8.20]

plt.plot(year,pop)
plt.xlabel("year")
plt.ylabel("population")
plt.title("world populations")
plt.yticks([6,7,8],['6B','7B','8B'])
plt.show()