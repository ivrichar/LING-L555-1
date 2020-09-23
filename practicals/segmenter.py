import sys

text = sys.stdin.read()

newtext = text.replace('. ', '.\n')

print(newtext)


"""
feel free to ignore this, i tried to write from a file into another file and got confused by python i/o
# note: I wanted to take the filename as an input and read in file name from standard input
#filename = sys.stdin.read()

#get text from file
#text = open(filename, "r")
with open("wiki.txt", "r") as l:
    text = l.read()

# write into a file called segmentedfile.txt
f = open("segmentedfile.txt", "w")

f.write(text.replace('. ','.\n'))


A segmenter should probably segment along a semi-colon, but it would still depend
on context.

A sentence with an ellipsis should be one sentence, I think.

An exclamation mark at the beginning of a sentence should be treated like a
part of the same sentence, but there can also be valid sentences that end in
exclamation marks, so it's hard to say. Words offset by a single comma at the
beginning of a sentence should be included in the sentence.

Transcription of human speech might be difficult. Commas would also be hard, as
they're used in lists as well as to offset clauses. Things like numbers might be
difficult (as they use periods and commas for non-grammatical purposes)
"""
