from textblob import TextBlob

First_word = TextBlob(" hello i am rupender.nice to meet you")
result1 = First_word.detect_language()
print(result1)

second_word = TextBlob("Tous les êtres humains naissent libres et égaux en dignité et en droits."
                       " Ils sont doués de raison et de conscience et doivent agir les uns envers les "
                       "autres dans un esprit de fraternité ")
result2 = second_word.detect_language()
print(result2)


third_word = TextBlob("Buenas tardes")
result3 = third_word.detect_language()
print(result3)

fourth_word = TextBlob("Namaste kese ho ")
result4 = fourth_word.detect_language()
print(result4)