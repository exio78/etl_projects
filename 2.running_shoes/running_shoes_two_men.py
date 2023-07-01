import requests
from bs4 import BeautifulSoup
import pandas as pd

# set the variable to iterate over each webpage
# url2 = "https://runrepeat.com/catalog/running-shoes?page=2" --> we can add the number 2 at the end
next_page = 2

# write or copy the url from the webpage we are going to extract the data
url = "https://runrepeat.com/catalog/mens-running-shoes"

# create the list to append the dictionaries to create the dataframer later 
# with titles and prices
list_shoes_all_pages = []

for page in range(40): # Iterate over each page, we have 41 pages, index is 0

    # get response for the current url, the current webpage
    response = requests.get(url).text

    # parse the response into a lxml format for readability here in python
    soup = BeautifulSoup(response, "lxml")

    # select all the shoes in the current page 
    shoes_page = soup.find_all("li", class_ = "row product_list")

    for index, shoe in enumerate(shoes_page): # Iterate now over each individual pair of shoes in current page

        # from each pair of shoes extract the title where it has the brand and model
        print(index, shoe.find("div", class_ = "product-name hidden-md hidden-lg col-md-12 col-lg-12").text)
        
        # not all the shoes on this webpage have a price because some of them are out of stock
        # if we don't have a price we can't apply the .text attribute to the find() method, it will give us an error
        try: 

          # from each pair of shoes extract the price and discount
          price_shoes = shoe.find("div", class_ = "product-prices prices__full-width").text
          print(price_shoes)
        
        except: 

          # for those shoes which aren't in stock we replace that information with "out of stock"
          price_shoes = "out of stock"
          print(price_shoes)
        
        print()
        
        # create a dictionary to append into the list at the beginning of the code
        title_price = {
            "Title": shoe.find("div", class_ = "product-name hidden-md hidden-lg col-md-12 col-lg-12").text,
            "Price": price_shoes
            }

        # append these dictionaries into a list
        list_shoes_all_pages.append(title_price)

    # separate the pages for readability on the terminal
    print(">> Page finished --------------------") 

    # as we said in the beginning of this code update the url for the next page
    url = "https://runrepeat.com/catalog/mens-running-shoes?page=" + str(next_page)
    print(url)

    # increase the variable for the next page
    next_page += 1 
    
# create dataframe 
df = pd.DataFrame(list_shoes_all_pages)

# save the dataframe into a csv format
df.to_csv("Men_running_shoes_two.csv", index = False)