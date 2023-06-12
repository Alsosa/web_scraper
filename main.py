from bs4 import BeautifulSoup
import requests
import re

print("Let's search graphics cards!")
options = ['1050', '1060', '1080', '3050', '3060']

user_input = ''

input_message = "Pick an option:\n"

for index, item in enumerate(options):
    input_message += f'{index+1}) {item}\n'

input_message += 'Your choice: '

while user_input not in map(str, range(1, len(options) + 1)):
    user_input = input(input_message)

print('You picked: ' + options[int(user_input) - 1])

search_term = options[int(user_input) - 1]

url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

items_found = {}

for page in range(1, pages + 1):
	url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131&page={page}"
	page = requests.get(url).text
	doc = BeautifulSoup(page, "html.parser")

	div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
	items = div.find_all(string=re.compile(search_term))

	for item in items:
		parent = item.parent
		if parent.name != "a":
			continue

		link = parent['href']
		next_parent = item.find_parent(class_="item-container")
		try:
			price = next_parent.find(class_="price-current").find("strong").string
			items_found[item] = {"price": int(price.replace(",", "")), "link": link}
		except:
			pass

sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

for item in sorted_items:
	print(item[0])
	print(f"${item[1]['price']}")
	print(item[1]['link'])
	print("-------------------------------")