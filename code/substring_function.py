import pandas as pd
data = pd.read_csv("/Users/drakeandersen/data science/count_by_genre.csv")

# function
def find_genre(genre):
	total = 0
	for i in data.index:
		if genre.lower() in data['Genre'][i].lower():
			total = data['Count'][i] + total
	print(total)

# then try various substrings
find_genre("rock")
find_genre("classical")
find_genre("hip hop")
