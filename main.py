from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/gigabyte-geforce-rtx-4070-ti-gv-n407tgaming-oc-12gd/p/N82E16814932580"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")


prices = doc.find_all(string="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)