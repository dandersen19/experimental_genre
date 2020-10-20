from bs4 import BeautifulSoup
import requests

all_genres = []

for i in sites:
    current_site = sites[i]
    print(current_site)
    response = requests.get(url=current_site,)
    soup = BeautifulSoup(response.content, 'html.parser')
    for elem in soup(text='Genres'):
	    whole = elem.parent.parent
	    links = whole.find_all('a')
	    for link in links:
		    title = link.get('title')
		    all_genres.append(title)

# elem.parent.parent gets entire table row from artist info box
# containing "Genres" header cell and all genre labels
# (elem.parent only gets header cell)

# <a> tag titles are more consistent than text labels
# (so we use those)

# print list of all genres found
print(all_genres)

# import into Excel to review/filter/clean

# or just do it in Python

# for example, removes duplicates by converting to dict (and back)
all_genres = list(dict.fromkeys(all_genres))
