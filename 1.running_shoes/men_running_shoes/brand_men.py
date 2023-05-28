import re
import pandas as pd

men_brands = """
<li class="nav-item"><a class="nav-link" href="/adidas_Mens_Running_Shoes/catpage-MRSADIDAS.html">adidas</a></li>
<li class="nav-item"><a class="nav-link" href="/Altra_Mens_Running_Shoes/catpage-ALTRAMS.html">Altra</a></li>
<li class="nav-item"><a class="nav-link" href="/ASICSMens_Running_Shoes/catpage-MRSASICS.html">ASICS</a></li>
<li class="nav-item"><a class="nav-link" href="/Birkenstock_Mens_Recovery_Shoes/catpage-MRSBIRK.html">Birkenstock</a></li>
<li class="nav-item"><a class="nav-link" href="/Brooks_Mens_Running_Shoes/catpage-MRSBROOKS.html">Brooks</a></li>
<li class="nav-item"><a class="nav-link" href="/Craft_Mens_Running_Shoes/catpage-MRSCRAFT.html">Craft</a></li>
<li class="nav-item"><a class="nav-link" href="/Deckers_X_Lab_Mens_Recovery_Shoes/catpage-MRSDECKER.html">Deckers X Lab</a></li>
<li class="nav-item"><a class="nav-link" href="/HOKA_Mens_Running_Shoes/catpage-HOKAM.html">HOKA</a></li>
<li class="nav-item"><a class="nav-link" href="/inov-8_Mens_Running_Shoes/catpage-MRSINOV8.html">inov-8</a></li>
<li class="nav-item"><a class="nav-link" href="/Mizuno_Mens_Running_Shoes/catpage-MRSMIZUNO.html">Mizuno</a></li>
<li class="nav-item"><a class="nav-link" href="/New_BalanceMens_Running_Shoes/catpage-MRSNB.html">New Balance</a></li>
<li class="nav-item"><a class="nav-link" href="/Nike_Mens_Running_Shoes/catpage-MRSNIKE.html">Nike</a></li>
<li class="nav-item"><a class="nav-link" href="/NNormal_Mens_Running_Shoes/catpage-NNORMALMS.html">NNormal</a></li>
<li class="nav-item"><a class="nav-link" href="/On_Mens_Running_Shoes/catpage-MRSON.html">On</a></li>
<li class="nav-item"><a class="nav-link" href="/PUMA_Mens_Running_Shoes/catpage-PUMAMS.html">PUMA</a></li>
<li class="nav-item"><a class="nav-link" href="/Salomon_Mens_Running_Shoes/catpage-MRSSALOMON.html">Salomon</a></li>
<li class="nav-item"><a class="nav-link" href="/Saucony_Mens_Running_Shoes/catpage-MRSSAUCONY.html">Saucony</a></li>
<li class="nav-item"><a class="nav-link" href="/Skechers_Performance_Mens_Running_Shoes/catpage-MRSSKECHERS.html">Skechers Performance</a></li>
<li class="nav-item"><a class="nav-link" href="/The_North_FaceMens_Running_Shoes/catpage-MRSNF.html">The North Face</a></li>
<li class="nav-item"><a class="nav-link" href="/Topo_Athletic_Mens_Running_Shoes/catpage-MRSTO.html">Topo Athletic</a></li>
<li class="nav-item"><a class="nav-link" href="/Under_ArmourMens_Running_Shoes/catpage-MRSUA.html">Under Armour</a></li>

"""

men_web_page = "https://www.runningwarehouse.com"

links = re.findall('href="(.+?)">',men_brands)
brand = re.findall('html">(.+)</a>', men_brands)
#print(links)
#print(len(brand))

complete_links = []
for link in links:
    link = men_web_page + link
    complete_links.append(link)

dictionary = {"brand" : brand, "links" : complete_links}
#print(dictionary["brand"][7])
#
df = pd.DataFrame(dictionary)
print(df)
