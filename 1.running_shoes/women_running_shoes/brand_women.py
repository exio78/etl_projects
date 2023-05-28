import re
import pandas as pd

women_brands = """
<li class="nav-item"><span class="nav-link offcanvas-menu-list-heading is-sub">Shop by Brand</span></li>
<li class="nav-item"><a class="nav-link" href="/adidas_Womens_Running_Shoes/catpage-WRSADIDAS.html">adidas</a></li>
<li class="nav-item"><a class="nav-link" href="/Altra_Womens_Running_Shoes/catpage-ALTRAWS.html">Altra</a></li>
<li class="nav-item"><a class="nav-link" href="/ASICS_Womens_Running_Shoes/catpage-WRSASICS.html">ASICS</a></li>
<li class="nav-item"><a class="nav-link" href="/Birkenstock_Womens_Recovery_Shoes/catpage-WRSBIRK.html">Birkenstock</a></li>
<li class="nav-item"><a class="nav-link" href="/Brooks_Womens_Running_Shoes/catpage-WRSBROOKS.html">Brooks</a></li>
<li class="nav-item"><a class="nav-link" href="/Craft_Womens_Running_Shoes/catpage-WRSCRAFT.html">Craft</a></li>
<li class="nav-item"><a class="nav-link" href="/Deckers_X_Lab_Womens_Recovery_Shoes/catpage-WRSDECKER.html">Deckers X Lab</a></li>
<li class="nav-item"><a class="nav-link" href="/HOKA_Womens_Running_Shoes/catpage-HOKAW.html">HOKA</a></li>
<li class="nav-item"><a class="nav-link" href="/inov-8_Womens_Running_Shoes/catpage-INWS.html">inov-8</a></li>
<li class="nav-item"><a class="nav-link" href="/Mizuno_Womens_Running_Shoes/catpage-WRSMIZUNO.html">Mizuno</a></li>
<li class="nav-item"><a class="nav-link" href="/New_BalanceWomens_Running_Shoes/catpage-WRSNB.html">New Balance</a></li>
<li class="nav-item"><a class="nav-link" href="/Nike_Womens_Running_Shoes/catpage-WRSNIKE.html">Nike</a></li>
<li class="nav-item"><a class="nav-link" href="/NNormal_Womens_Running_Shoes/catpage-NNORMALWS.html">NNormal</a></li>
<li class="nav-item"><a class="nav-link" href="/On_Womens_Running_Shoes/catpage-WRSON.html">On</a></li>
<li class="nav-item"><a class="nav-link" href="/PUMA_Womens_Running_Shoes/catpage-PUMAWS.html">PUMA</a></li>
<li class="nav-item"><a class="nav-link" href="/Salomon_Womens_Running_Shoes/catpage-WRSSALOMON.html">Salomon</a></li>
<li class="nav-item"><a class="nav-link" href="/Saucony_Womens_Running_Shoes/catpage-WRSSAUCONY.html">Saucony</a></li>
<li class="nav-item"><a class="nav-link" href="/Skechers_Performance_Womens_Running_Shoes/catpage-WRSSKECHERS.html">Skechers Performance</a></li>
<li class="nav-item"><a class="nav-link" href="/The_North_FaceWomens_Running_Shoes/catpage-WRSNF.html">The North Face</a></li>
<li class="nav-item"><a class="nav-link" href="/Topo_Athletic_Womens_Running_Shoes/catpage-WRSTO.html">Topo Athletic</a></li>
<li class="nav-item"><a class="nav-link" href="/Under_ArmourWomens_Running_Shoes/catpage-WRSUA.html">Under Armour</a>
"""

womens_web_page = "https://www.runningwarehouse.com"

links = re.findall('href="(.+?)">',women_brands)
brand = re.findall('html">(.+)</a>', women_brands)
#print(links)
#print(len(brand))

complete_links = []
for link in links:
    link = womens_web_page + link
    complete_links.append(link)

dictionary = {"brand" : brand, "links" : complete_links}
#print(dictionary["brand"][7])
#
#df = pd.DataFrame(dictionary)
#print(df)
