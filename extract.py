import sys
import requests
from bs4 import BeautifulSoup

def extract_ratings(imdb_id):
	req = requests.get("http://www.imdb.com/title/" + imdb_id + "/ratings")
	soup = BeautifulSoup(req.text, "html.parser")

	# Extract movie title
	movie_title = soup.find("title").string.replace('- User ratings', '').strip()

	# Extract ratings table - 2nd table of the page
	tables = soup.find_all("table")
	ratings_table = tables[1]

	rows = ratings_table.find_all("tr")

	ratings = {}

	# Group by user class type
	for row in rows:
		details = row.find_all("td")
		if details[0].find('a') is None or details[2].find('img') is None:
			continue
		user_class = details[0].find('a').text
		user_rating = float(details[2].text.strip(" ").strip("&nbsp"))
		ratings.update({user_class: { movie_title: user_rating}})

	return ratings
