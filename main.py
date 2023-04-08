from bs4 import BeautifulSoup

with open("index.html", "r") as f:      # open index.html file on read mode as f.
    doc = BeautifulSoup(f, "html.parser")   # parse the file

print(doc.prettify())  # print the parsed html using prettify for automatic indentation