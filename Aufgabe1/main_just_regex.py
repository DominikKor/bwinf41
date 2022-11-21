import re

book_text = open("Alice_im_Wunderland.txt").read()
search_term = open("stoerung0.txt").read()

regex_search_term = search_term.replace("_", "\S+")
all_matches = re.findall(regex_search_term, book_text, re.IGNORECASE)

print(all_matches)
