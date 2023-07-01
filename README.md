<h1>Welcome to my ETL repository 🧐👋</h1>
<br>
<img src="https://miro.medium.com/v2/resize:fit:1400/1*Mkb6pMXJ7XeZY7fLonG9XA.gif" alt="My Image">
<br>
<h1>Description</h1>
<br>
<h1>This is the repository for my ETL projects, here is the summary and explanation for each one of them:</h1>
<br>
<h2>1.Running Shoes: Extract, Transform-clean, Visualize</h2>
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
