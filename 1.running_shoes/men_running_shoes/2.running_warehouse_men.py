import requests
from bs4 import BeautifulSoup
import pandas as pd
import brand_men
# we import a dictionary created in the brand_men.py file, 
# this dictionary contains the brand and the link as key values inside of that dictionary
# we are going to enter on each brand page inside of that website with a for loop.

brands_links = brand_men.dictionary["links"]

brand_csv = 0 # ---> this will be the index of the file csv per brand
for brand in brands_links:

    html_text = requests.get(brand).text # we get the webpage link with requests module
    soup_running_warehouse = BeautifulSoup(html_text, "lxml") # then we parse it with beautifoul soup

    shoes = soup_running_warehouse.find_all("div", class_ = "cattable-wrap-cell gtm_impression")
    # Now we are going to find each pair of shoes inside the current web brand page with find_all()

    title_list = []
    sex_list = []
    price_list = []
    technology_list = []
    links_per_brand = []

    best_use_range_list = [] # this will be the cushioning and stability in one item of this list
    best_use_surface_list = []

    # Before extracting the information of each pair of shoes we create 7 lists which are going to be
    # our features

    for shoe in shoes: # Now we iterate over each shoe
                        # we extract in this case with find() unique information per pair of shoes

        shoe_title = shoe.find("div", class_ ="cattable-wrap-cell-info-name")
        shoe_sex = shoe.find("div", class_ = "cattable-wrap-cell-info-sub")
        shoe_price = shoe.find("div", class_ = "cattable-wrap-cell-info-price")

        # After getting title, sex and price of the pair of shoes, we are going to get the link
        # of that pair of shoes and parse it to enter on the current webpage of this pair of shoes.  
        shoe_page_link = shoe.find("a", class_ = "cattable-wrap-cell-info")["href"]
        links_per_brand.append(shoe_page_link)

        shoe_page = requests.get(shoe_page_link).text
        shoe_page_parsed = BeautifulSoup(shoe_page, "lxml")

        # Here we are going to extract the best use and surface for which the shoe is intended to be used
        # in one list, the level of cushioning and stability in another list 
        # and the technology (midsole, outsole, upper) in another list.
        best_use_surface = shoe_page_parsed.find_all("div", class_ = "col-6 col-md-4 bestuse-type")

        best_use_range = shoe_page_parsed.find_all("div", class_ = "col is-active")

        technology = shoe_page_parsed.find(id = "product_tech")# here i look for id rather than class_

        title_list.append(shoe_title.text)
        sex_list.append(shoe_sex.text) 
        price_list.append(shoe_price.text)

        # In the case of technology id = "product_tech", with some brands it allows me to extract
        # the text of the html code parsed and with some brands it does not, as a result of this 
        # I will use a try except block of code, if i can extract only the text 
        # to simplify the process instead of getting all the tags it will do so, if not, then it will
        # take all the tags but we will not get an error of this code file and it will continue running.

        try:
            technology_list.append(technology.text)
        except:
            technology_list.append(technology)

        #here we have nested lists, and sometimes the technology too
        best_use_range_list.append(best_use_range)
        best_use_surface_list.append(best_use_surface)

    # Now i create the dictionary of the features to construct the dataframe for the csv file
    # but only for the current brand, when the look is finished it will do the same 
    # for the following brand.
    features = {"title" : title_list, "sex": sex_list, "price": price_list, 
        "technology": technology_list, "best_use_range": best_use_range_list, 
        "best_use_surface": best_use_surface_list, "link_shoes": links_per_brand}
        
    csv_file_brand = pd.DataFrame(features)
    print(csv_file_brand)

    # It is important to note here that the variable brand_csv is at the beginning of this code file
    # before the first for loop, and this will be our index for the name of our file, since I want
    # to create a csv file with all this features per each and every brand inside of this webpage.
    # The name of the current csv file will be a string which is the name of the brand 
    # inside of the dictionay imported from other file indexed with this variable
    # and it will be concatenated with the extension .csv 

    csv_file_brand.to_csv(brand_men.dictionary["brand"][brand_csv] + ".csv")
    brand_csv += 1