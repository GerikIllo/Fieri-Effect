import requests
from bs4 import BeautifulSoup

url = "https://www.yelp.com/search?find_desc=br&find_loc=Portland%2C+OR%2C+US&ns=1"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

#for link in soup.find_all("a"):
#        print "<a href='%s'>%s</a>" %(link.get("href"), link.text)



    
g_data = soup.find_all("div", {"class": "info"})

for item in g_data:
    print item.contents[0].find_all("a", {"class": "business-name"})[0].text
    print item.contents[1].find_all("p", {"class": "adr"})[0].text

    try:
        print item.contents[1].find_all("span", {"itemprop": "address"})[0].text
        print item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text
    except:
        pass



    try:
        print item.contents[1].find_all("li", {"class": "primary"})[0].text
    except:
        pass
    print "\n"
