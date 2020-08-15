import json

data = json.load(open("data.json"))

def search_word(word):    
    try:
        
        searched_word = data[word.lower()]
    except:
        return("Your word does nor exist in the records. Try with another")
    return searched_word    

while True:
    word_to_search_for = input("What's your word?")
    if word_to_search_for != "salir":
        print(search_word(word_to_search_for))
    else: 
        break
