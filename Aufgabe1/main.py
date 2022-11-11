import re

book_text = open("Aufgabe1/Alice_im_Wunderland.txt").read()
search_term = open("Aufgabe1/stoerung0.txt").read()

regex_search_term = search_term.replace("_", "\S+")
all_matches = re.findall(regex_search_term, book_text, re.IGNORECASE)

print(all_matches)
