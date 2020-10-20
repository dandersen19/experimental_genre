# Experimental Genre Associations

## Introduction
The term “experimental” is used in discussions of musical genre in two contradictory ways: (1) to describe music that does not fit into any existing category, and (2) as a qualifier to describe music that occupies an aesthetically marginal position within a category (similar to the term “avant-garde”). To better understand the latter usage, I designed this project to identify the genre associations of musicians considered to be “experimental” using data from Wikipedia. I found that experimental musicians were most likely to also be categorized as rock music.

## Data and Methods
Because “experimental” is not consistently recognized as a genre in and of itself, instead of using genre labels I used a list of 184 experimental musicians from this page: https://en.wikipedia.org/wiki/List_of_experimental_musicians.

I used BeautifulSoup to parse the list and obtain the web addresses for each musician’s Wikipedia page. By scraping each musician’s Wikipedia page, I generated a list of 554 genre labels comprising 159 unique entries. I removed 93 results of “None,” in addition to one entry that was an editorial indication rather than a genre (“Edit section: Genres”), resulting in a dataset of 460 labels, of which 157 were unique.

As a final step, I consolidated the 157 unique labels into a handful of larger genre categories using substring matching. I began with well-established genre labels including hip hop/rap, pop, classical, rock, jazz, electronic, and dance. For hip hop/rap I combined the results of the substrings “hip hop” and “rap”; for electronic I used the substring “electro” (rather than “electronic”) so as to encompass words like “electroacoustic.” Next, I analyzed the list to determine if other terms were especially prevalent, and therefore warranted consolidation so as to be compared with the larger categories. I found that the terms metal, punk, and industrial were especially prevalent, and added these as well for a total of ten categories for comparison.

## Conclusion
Musicians considered to be experimental were most likely to be associated with rock music subgenres by a wide margin, followed by electronic, pop, and metal. Remarkably, the number of rock-related labels (88) exceeded even the number of instances of the label “experimental” (70).

![Prevalence of Genre Labels for Musicians Considered to Be Experimental](https://github.com/dandersen19/experimental_genre/blob/main/visualizations/results.png)

Of course, it bears mentioning that the sample size for this project is extremely small, and was drawn from a list that was generated manually, rather than automatically. Consequently, the list may be especially vulnerable to systemic biases of Wikipedia editors (https://en.wikipedia.org/wiki/Wikipedia:Systemic_bias). Nevertheless, this brief study is a starting point for better understanding the application of an especially ambiguous term.
