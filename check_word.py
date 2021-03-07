from textblob import TextBlob

print("Enter words  to check correct_spelling: ")


myTuple = input(str(""))
corrected_word = []

for input  in myTuple:
   corrected_word.append(TextBlob(input))
print("Corrected list words are: ")
for input  in corrected_word:
   print(input.correct(), end="")
