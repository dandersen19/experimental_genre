from bs4 import BeautifulSoup

# open page source downloaded into HTML file
with open("/Users/drakeandersen/list_of_experimental_musicians.html") as fp:
	soup = BeautifulSoup(fp, 'html.parser')

# gives contents of all <li> tags
soup.find_all('li')

# gives list of artists
for tag in soup.ul.find_all("li", recursive=True):
	name = tag.text.split(" –", 1)
	print(name[0])

# en-dash is used as delimiter between artist name and descriptive text

# gather links to artist wiki pages
for link in soup.find_all('a'):
	print(link.get('href'))

# this requires some cleaning since there are additional links

# format as list (I used Excel to enclose in '' and append commas)
sites = ['https://en.wikipedia.org/wiki/Robert_Ashley', ]
