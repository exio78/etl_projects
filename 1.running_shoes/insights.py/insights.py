import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. What is the price distribution between these two datasets?

men = pd.read_csv("men_running_shoes.csv")
women = pd.read_csv("women_running_shoes.csv")

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.hist(men["price"], bins = 40, color = "#01a3a4", label = "men")
ax1.set_title("MEN")
ax1.set_xlabel("Men Price shoes $")
ax1.set_ylabel("Ocurrences")

ax2.hist(women["price"], bins = 40, color = "#5f27cd", label = "women")
ax2.set_title("WOMEN")
ax2.set_xlabel("Women Price shoes $")

plt.tight_layout()
plt.show()

# Using conditional selection to create a histogram with prices between 100$ and 200$ 

filter_price_men = (men["price"] >= 100) & (men["price"] <= 200)
filter_price_women = (women["price"] >= 100) & (women["price"] <= 200)

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.hist(men[filter_price_men]["price"], bins = 40, color = "#01a3a4", label = "men")
ax1.set_title("MEN")
ax1.set_xlabel("Men Price shoes $")
ax1.set_ylabel("Ocurrences")

ax2.hist(women[filter_price_women]["price"], bins = 40, color = "#5f27cd", label = "women")
ax2.set_title("WOMEN")
ax2.set_xlabel("Women Price shoes $")

plt.tight_layout()
plt.show()

# 2. Is there a relationship between price and cushioning?

# Cushioning

mean_price_cushioning = men.groupby("cushioning").mean()
mean_price_cushioning = mean_price_cushioning.sort_values("price")

fig, ax = plt.subplots()

ax.bar(mean_price_cushioning.index, mean_price_cushioning["price"], color = "#01a3a4")
ax.set_title("Cushioning Levels and Price")
ax.set_xlabel("Cushioning")
ax.set_ylabel("Price in Dollars $")

plt.show()

# It is important to see how many ocurrences we have per each cushioning category.

men["cushioning"] = men["cushioning"].replace(np.nan, "no info")
#print(men["cushioning"])


fig, axes = plt.subplots(2, 3)
fig.suptitle("Distribution of prices by Cushioning")

# Plot the data on the figure object
axes[0, 0].hist(men[men["cushioning"] == "Minimal"]["price"], color = "#01a3a4", bins = 20)
axes[0, 0].set_title("Minimal")

axes[0, 1].hist(men[men["cushioning"] == "Low"]["price"], color = "#01a3a4", bins = 20)
axes[0, 1].set_title("Low")

axes[0, 2].hist(men[men["cushioning"] == "Medium"]["price"], color = "#01a3a4", bins = 20)
axes[0, 2].set_title("Medium")

axes[1, 0].hist(men[men["cushioning"] == "High"]["price"], color = "#01a3a4", bins = 20)
axes[1, 0].set_title("High")

axes[1, 1].hist(men[men["cushioning"] == "Maximal"]["price"], color = "#01a3a4", bins = 20)
axes[1, 1].set_title("Maximal")

axes[1, 2].hist(men[men["cushioning"] == "no info"]["price"], color = "#01a3a4", bins = 20)
axes[1, 2].set_title("no info")

plt.tight_layout()
plt.show()

# Stability, the higher the stability the higher the price?

mean_price_stability = men.groupby("stability").mean()
mean_price_stability = mean_price_stability.sort_values("price")
mean_price_stability

fig, ax = plt.subplots()

ax.bar(mean_price_stability.index, mean_price_stability["price"], color = "#01a3a4")
ax.set_title("Stability and Price")
ax.set_xlabel("Stability")
ax.set_ylabel("Price in Dollars $")

plt.show()

# 3. Let's explore the average price per brand 

average_brand = men.groupby("brand").mean()

average_brand = average_brand.sort_values("price")

plt.barh(average_brand.index, average_brand["price"], color = "#01a3a4")
plt.title("Average Price of brands")
plt.xlabel("price in dollars $")
plt.tight_layout()
plt.show()

# but we need to see how many observations we have per brand

count_brand = men.groupby("brand").count()

count_brand = count_brand.sort_values("price")

plt.barh(count_brand.index, count_brand["price"], color = "#01a3a4")
plt.title("Observations per brands")
plt.xlabel("Number of observations")
plt.tight_layout()
plt.show()

# 4. Porcentage of the price that falls in price ranges

filt_49_100 = (men["price"] >= 49) & (men["price"] <= 100)

men[filt_49_100]["price"].count()

filt_100_150 = (men["price"] > 100) & (men["price"] <= 150)

men[filt_100_150]["price"].count()

filt_100_150 = (men["price"] > 100) & (men["price"] <= 150)

men[filt_100_150]["price"].count()

filt_150_200 = (men["price"] > 150) & (men["price"] <= 200)

men[filt_150_200]["price"].count()

filt_200_250 = (men["price"] > 200) & (men["price"] <= 250)

men[filt_200_250]["price"].count()

filt_250_300 = (men["price"] > 250) & (men["price"] <= 300)

men[filt_250_300]["price"].count()

# let's plot the pie chart.

one = men[filt_49_100]["price"].count()
two = men[filt_100_150]["price"].count()
three = men[filt_150_200]["price"].count()
four = men[filt_200_250]["price"].count()
five = men[filt_250_300]["price"].count()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

five_parts = [one, two, three, four, five]
labels = ["49-100$", "100-150$", "150-200$", "200-250$", "250-300$"]
colours = ["#00d2d3", "#2e86de", "#ff9f43", "#ee5253", "#5f27cd"]

ax.pie(five_parts, colors = colours, autopct ="%1.2f%%", pctdistance = 1.17, wedgeprops= {"edgecolor": "#222f3e"})

ax.set_title("Price Ranges Running Shoes")
ax.legend(labels, loc = [0.9, 0.05])
fig.set_facecolor("#c8d6e5")
plt.show()

# 5. 