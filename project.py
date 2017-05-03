import extract
import pprint
import collab

def main():
	# Define imdb ids of movies
	imdb_ids = ['tt4857264', 'tt2015381', 'tt0120338', 'tt1535109', 'tt3315342', 'tt3498820', 'tt0253474',
	 'tt0073486', 'tt0765429', 'tt0293662', 'tt0120735', 'tt1032755']

	print "[+] Extracting data"
	extracted_data = {}
	for imdb_id in imdb_ids:
		ratings = extract.extract_ratings(imdb_id)
		for key in ratings:
			if key not in extracted_data.keys():
				extracted_data[key] = {}
			extracted_data[key].update(ratings[key])
	pprint.pprint(extracted_data)

	print "---"

	print "[+] Collaborative filtering based on user classes"
	print "--- Top 3 similar user classes for each user class - Similarity function used: Cosine Distance"
	for current_uc in extracted_data:
		print "[-] " + current_uc
		top_similar = collab.top_similar(extracted_data, current_uc, 3, collab.minkowski_distance)
		pprint.pprint(top_similar)

	print "---"

	print "--- Recommend movies for each user class"
	for current_uc in extracted_data:
		print "[-] " + current_uc
		recs = collab.recommend(extracted_data, current_uc, 7.5, collab.manhattan_distance)
		pprint.pprint(recs)

if __name__ == '__main__':
    main()