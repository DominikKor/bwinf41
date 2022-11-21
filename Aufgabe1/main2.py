def find_all(search_term: str, text: str):
    text = text.split()
    terms = search_term.split()
    result = []
    for idx, word in enumerate(text):
        if word.lower() == terms[0].lower():
            found_passage = True
            for idx2, term in enumerate(terms):
                if term == "_":
                    continue
                if not terms[idx2].lower() == text[idx+idx2].lower():
                    found_passage = False
                print("horray")
            if found_passage:        
                result.append(text[idx:idx+(len(terms))])


def main():
    with open("Aufgabe1/Alice_im_Wunderland.txt", encoding="utf-8") as file:
        book_text = file.read()

    with open("Aufgabe1/extra_stoerung0.txt", encoding="utf-8") as file:
        search_term = file.read()

    result = find_all(search_term, book_text)
    print(result)


if __name__ == "__main__":
    main()
