import sys

text = sys.stdin.read()

originaltext = text.split(".\n")

text = text.replace(" ", "\n")
text = text.replace(",", " ,")
text = text.replace(":", " :")
text = text.replace("(", "( ")
text = text.replace(")", " )")

lines = text.split(".\n") #list of lines in the txt

sentences = [] # empty list now, will contain list of all words grouped by sentence


for i in range(0, len(lines)): # repeats with i from 0 to length of the list minus 1 (index of last element)
    thesewords = lines[i].split() #splits into a string based on the whitespace
    sentences.append(thesewords) # adds this list of words to the big list of sentences

# now sentences and lines are equal length, with one containing strings and the other containing lists of strings
for j in range(0, len(sentences)):
    print('# sent_id = %d' % (j+1))
    print('# text = %s' % (originaltext[j]))
    for k in range(0, len(sentences[j])):
        count = k+1
        token = sentences[j][k]
        print(f'{count} \t {token} \t _ \t _ \t _ \t _ \t _ \t _ \t _ \t _')


"""

We should split punctuation from the token so that we can properly process
both the token and the punctuation marks. If we didn't, the program would count
things like the string "here" and "here:" as two seperate tokens, even when it
shouldn't.

Abbreviations should be written as a single token, as well as large numerals.



Contractions and clitics should be multiple tokens.
"""
