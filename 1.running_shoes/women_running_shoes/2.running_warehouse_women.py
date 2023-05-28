import requests
from bs4 import BeautifulSoup
import pandas as pd
import brand_women

brands_links = brand_women.dictionary["links"]

brand_csv = 0
for brand in brands_links:

    html_text = requests.get(brand).text
    soup_running_warehouse = BeautifulSoup(html_text, "lxml")

    shoes = soup_running_warehouse.find_all("div", class_ = "cattable-wrap-cell gtm_impression")
    #print(shoes)

    title_list = []
    sex_list = []
    price_list = []
    technology_list = []
    links_per_brand = []

    best_use_range_list = []
    best_use_surface_list = []

    for shoe in shoes:

        shoe_title = shoe.find("div", class_ ="cattable-wrap-cell-info-name")
        shoe_sex = shoe.find("div", class_ = "cattable-wrap-cell-info-sub")
        shoe_price = shoe.find("div", class_ = "cattable-wrap-cell-info-price")

        shoe_page_link = shoe.find("a", class_ = "cattable-wrap-cell-info")["href"]
        links_per_brand.append(shoe_page_link)

        shoe_page = requests.get(shoe_page_link).text
        shoe_page_parsed = BeautifulSoup(shoe_page, "lxml")

        best_use_surface = shoe_page_parsed.find_all("div", class_ = "col-6 col-md-4 bestuse-type")# best use and surface

        best_use_range = shoe_page_parsed.find_all("div", class_ = "col is-active") #cushioning and stability

        technology = shoe_page_parsed.find(id = "product_tech")

        title_list.append(shoe_title.text)
        sex_list.append(shoe_sex.text) 
        price_list.append(shoe_price.text)
        try:
            technology_list.append(technology.text)
        except:
            technology_list.append(technology)

        #here we have nested lists
        best_use_range_list.append(best_use_range)
        best_use_surface_list.append(best_use_surface)

    features = {"title" : title_list, "sex": sex_list, "price": price_list, 
        "technology": technology_list, "best_use_range": best_use_range_list, 
        "best_use_surface": best_use_surface_list, "link_shoes": links_per_brand}
        
    csv_file_brand = pd.DataFrame(features)
    print(csv_file_brand)
    csv_file_brand.to_csv(brand_women.dictionary["brand"][brand_csv] + ".csv")
    brand_csv += 1



    #for index, item in enumerate(technology_list):
    #    print(item.text, index)

    #print(technology.text)
    #print(best_use_range)
    #print(best_use_surface)
    #print(shoe_price.text)
    #print(shoe_sex.text)
    #print(shoe_title.text)