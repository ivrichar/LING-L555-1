import sys

text = sys.stdin.read()


text.replace(",", " ,")
text.replace(":", ": ")
text.replace("(", "( ")
text.replace(")", " )")
text.replace(" ", "\n")

"""
We should split punctuation from the token so that we can properly process
both the token and the punctuation marks. If we didn't, the program would count
things like the string "here" and "here:" as two seperate tokens, even when it
shouldn't.

Abbreviations should be written as a single token, as well as large numerals.



Contractions and clitics should be multiple tokens.
"""
