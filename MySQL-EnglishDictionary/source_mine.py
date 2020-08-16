
#LOADING MODULES AND PACKAGES
from difflib import  get_close_matches
import mysql.connector

#CREATING CONECTION
con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

#FUNCTION THAT SEARCHES FOR THE GIVEN WORD
def search_word(word):
    word = word.lower()

    try:
        query = cursor.execute(
            """
            SELECT Definition FROM Dictionary WHERE Expression = '%s'  
            OR Expression  = '%s' 
            OR Expression = '%s'
           """ % (word, word.title(), word.upper())
        )
        results = cursor.fetchall()
        
        query_comparison = cursor.execute("SELECT Expression FROM Dictionary")
        results_comparison = cursor.fetchall()
       
        if results:
            searched_word = results
          
        elif results_comparison:    
            words_list = []
            final_list = []
            for field in results_comparison:
                words_list.append(str(field))
            for i in words_list:
                final_list.append(i[2:-3])
    
            print( "Did you mean one of these options: {} ,  Which one? Or something different?".format(get_close_matches(word, [item for item in final_list])))
            right_word = "trying one more time"
            while right_word not in final_list:
                right_word = input("Give me your right option, dude ")
            
            query_correct = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % right_word)
            results_correct = cursor.fetchall()
            return results_correct
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


