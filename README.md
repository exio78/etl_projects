<h1>Welcome to my ETL repository 🧐👋</h1>
<br>
<img src="https://miro.medium.com/v2/resize:fit:1400/1*Mkb6pMXJ7XeZY7fLonG9XA.gif" alt="My Image">
<br>
<h1>Description</h1>
<br>
<h1>This is the repository for my ETL projects, here is the summary and explanation for each one of them:</h1>
<br>
<h2>1.Running Shoes Runningwarehouse: Extract, Transform-clean, Visualize</h2>
<br>
<h2>Goals:</h2>
<br>
<p>Since i extracted information from a webpage where it sells running shoes of different brands (21 brands) for men and women, I am interested in knowing more about these questions: what is the price distribution between these two datasets? (men and women), is there a relationship between price and cushioning?, what is the average price per brand between these running shoes from this dataset?, since we can divide the prices of these shoes into 5 price ranges, what percentage of prices fall into those five categories?, where are the most discounted shoes in by brand?. These insights can help shoe retailers to make informed decisions to position their marketing strategy and setting competitive prices.</p>
<br>
<h2>Extraction:</h2>
<br>
<p>In this project I have extracted the data using web scrapping with beautiful soup from this webpage: https://www.runningwarehouse.com/.<br>
The extracted process can be watched in the files 2.running_warehouse_men and 2.running_warehouse_women inside of the folders men_running shoes and women_running shoes respectively, there is the code and explanation for each process of data extraction.</p>
<br>
<h2>Cleaning</h2>
<br>
<p>After the data extraction I did the second part of this project which was the data cleaning and feature engineering process that can be found on the cleaning_pipeline_men.ipynb and cleaning_pipeline_women.ipynb inside of the folders men_running_shoes and women_running_shoes respectively, in these cases of data cleaning i prefer to use jupyter notebook.</p>
<br>
<h2>Visualize insights</h2>
<br>
<p>The main goal of this project was to create a price comparison between running shoes of women and running shoes of men, however, in this case the data extracted from only one source so far is not very good for this purpose of price comparison, the running shoes of men and women are very similar, as a result of this issue i focused on other insights that i could found from this dataset, these insights an visualizations using matplotlib along with pandas are in the file insights.ipynb which is inside of the folder with the same name.</p>
<br></br>


<h2>2.Running Shoes Runrepeat: Extract, Transform-clean, Visualize</h2>
<br>
<h2>Goals:</h2>
<br>
<p>This time I extracted with the same technique of beautiful soup the running shoes information from a different webpage called runrepeat: https://runrepeat.com/catalog/running-shoes. I want to know more about these questions: What is the median, mean and mode
of these running shoes prices datasets of men and women?, what is the price distribution?, what is the average price per brand?,
what are the price ranges that these shoes fall in? (i want to do it with a pie chart as in the first project), how many discounted
prices we have per brand?.</p>
<br>
<h2>Extraction:</h2>
<br>
<p>In this project I have extracted the data using web scrapping with beautiful soup from this webpage: 
https://runrepeat.com/catalog/running-shoes.<br>
The extracted process can be watched in the files running_shoes_two_men and running_shoes_two_women inside of the folder 2.running_shoes shoes respectively, there is the code and explanation for each process of data extraction.</p>
<br>
<h2>Cleaning</h2>
<br>
<p>After the data extraction I did the second part of this project which was the data cleaning and feature engineering process that can be found on the file Cleaning_pipeline_insights_runrepeat inside of the folder 2.running_shoes shoes respectively, i prefer to use jupyter notebook in these cases of data cleaning.</p>
<br>
<h2>Visualize insights</h2>
<br>
<p>The main goal of this project was to create a price comparison between running shoes of women and running shoes of men, however, in this case too as well as in the first project, the data extracted of the running shoes of men and women are very similar, as a result of this issue i focused on other insights that i could found from this dataset, these insights an visualizations using matplotlib along with pandas are in the file Cleaning_pipeline_insights_runrepeat which is inside of the folder 2.running_shoes.</p>
<br>



<h2>1 and 2 combining with SQL: Price comparison between shoes of runrepeat and runningwarehouse webpages</h2>
<br>
<h2>Goals:</h2>
<br>
<p>Now that I have two datasets from two different webpages on csv formats, I can compare the prices between these two sources. Why this would be of interest for some people? well, here are the reasons:
<br>
<br>
<strong>To get the best possible deal:</strong> When you're comparing prices, you can be sure that you're getting the best possible price for the shoes you want. This is especially important if you're on a budget or if you're looking for a specific pair of shoes.
<br>
<br>
<strong>To identify price discrepancies:</strong> If you see that the price of a pair of shoes is significantly different from one source to another, it could be a sign of a price discrepancy. This could be due to a number of factors, such as a sale, a clearance event, or a pricing error. By identifying price discrepancies, you can save money by buying shoes at the best possible price.
<br>
<br>
<strong>To conduct market research:</strong> If you're in the business of selling shoes, comparing prices can help you to conduct market research and see how your prices compare to those of other retailers. This information can be helpful in setting your own prices and in making sure that you're competitive in the market..
<br>
</p>
<br>
<h2>Creating, loading and Combining Tables on SQL</h2>
<br>
<p>I created a folder called sql_one_two where I putted two csv files datasets, one from the webpage1 and the other from the webpage2, after that I applied a similarity measure based on the titles of the non repeated shoes of the webpage2 (runningwarehouse) with the most similar shoes based on the title of the webpage1 (runrepeat). Based on this analysis I created three new csv files: <strong>equal_titles.cs</strong>, <strong>running_warehouse.csv</strong>, <strong>runrepeat.csv</strong>, this process can be seen on the coding jupyter notebook file called Cleaning_shoe_tiles.ipynb
<br>
<br>
In MySQL I could compare the difference of prices between the running shoes of webpage1 with the running shoes of webpage2 based on a query I wrote on the file running_shoes.sql inside of the same folder called sql_one_two, I used join tables based on a primary key which was the index of pandas or ID on SQL to create the final price comparison objective on a csv file called price_comparison.
</p>
<br>

<br>
<h2>3.Economic Data: Extract, Transform-clean, Visualize</h2>
<br>
<h2>Goals:</h2>
<br>
<p>The main part of this project is in the file economic_data.ipynb where I developed a study of macroeconomic indicators comparing them across different countries like the US, UK, China, Germany and more during the time period of 2018-2023 on purpose in order to see how these countries developed during the coronavirus pandemic, what were their economic performance?.</p>
<br>
<h2>Extraction:</h2>
<br>
<p>I extracted the data from the FRED webpage: https://fred.stlouisfed.org and from the World bank webpage: https://www.worldbank.org/en/home using the datareader module in python, you can see how I did it on the economic_data.ipynb file inside of the directory 3. economic_data</p>
<br>
<h2>Cleaning</h2>
<br>
<p>After extractig the data, I cleaned it and organized it applying multidimensional tabular data and performing some exploratory data analysis, resampling dataframes in months and years and filling some missing values</p>
<br>
<h2>Visualize insights</h2>
<br>
<p>I visualized some insights like the correlation of gdp with unemployment, CPI (Consumer Price Index) and interest rates between different countries to see which one is more sensible to changes in GDP regarding a specific macroeconomic indicator along with an image to visualize each insight. I developed 9 insights that you can read on the economic_data.ipynb.</p>
<br></br>

