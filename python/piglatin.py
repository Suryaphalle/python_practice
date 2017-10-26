'''Pig Latin is a game of alterations played on the English language game. To create the Pig Latin form of an English 
word the initial consonant sound is transposed to the end of the word and an ay is affixed 
(Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.
'''

def pig_latin(str):
  fst = str[0]
  if fst in ['a','e','i','o','u']:
    return str+"ay"
  else:
    return(str[1:]+"-"+fst+"ay")

text = pig_latin("input")
print(text)