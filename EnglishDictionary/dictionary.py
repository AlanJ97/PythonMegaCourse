import json

def search_word(word):
    data = json.load(open("data.json"))
    searched_word = data[word]
    return searched_word

while True:
    word_to_search_for = input("What's your word?")
    if word_to_search_for != "salir":
        print(search_word(word_to_search_for))
    else: 
        break
