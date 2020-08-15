#LOADING MODULES AND PACKAGES
from difflib import  get_close_matches
import json
#SETTING THE CLASS

#LOADING FILES WITH WORDS
data = json.load(open("data.json"))

#FUNCTION THAT SEARCHES FOR THE GIVEN WORD
def search_word(word):   
    try:
        word = word.lower()
        if word in data:
            searched_word = data[word]
        elif word.title() in data:
            searched_word = data[word.title()]
        elif word.upper() in data: 
            searched_word = data[word.upper()]
        elif len(get_close_matches(word, data.keys())) > 0:
            print( "Did you mean one of these options: {} ,  Which one? Or something different?".format(get_close_matches(word, data.keys())))
            right_word = "trying one more time"
            while right_word not in data:
                right_word = input("Give me your right option, dude ")
            return data[right_word]
        else:
            return "Your word does not exist in the records. Try with another"

    except:
        return("Something went wrong with the program. Try once more later")
    return searched_word    

#CYCLE THAT EXECUTES THE PROGRAM
while True:
    print(" To finish the program enter 'salir' ")
    word_to_search_for = input("What's your word? ")
    if word_to_search_for != "salir":
        output = search_word(word_to_search_for.strip())
        print("")
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)
        print("")
    else: 
        break
