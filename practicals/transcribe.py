import sys

transcriptions = []

# creates a list of tuples with the latin (nahuatl) alphabet
# and the ipa-ish character
fd = open('transtable.txt', 'r')
for line in fd.readlines():
    (latin, ipa) = line.split(' ')
    # for some reason it said it was split by spaces instead of tabs even though I used tabs, so I just had it split by space
    couple = (latin, ipa)
    transcriptions.append(couple)

# this function converts a string from nahuatl orthography to IPA (ish)
# it reads a string by character
def to_ipa(s):
    in_ipa = ""
    for letter in s: # iterates by character through string
        for pair in transcriptions: #iterates by tuple in the transcription list
            if letter == pair[0]: #if the current letter of the given string is equal to the latin letter in the tuple
                in_ipa = in_ipa + pair[1] #concatenate the already transcribed characters and this new character
                continue # the character has been found, so we can break the inner loop over transcriptions for this character only

text = sys.stdin.read()

lines = text.split(".\n") #split by line in input text

n = 0
for j in range(0, len(lines)):
    for line in lines:
        print(n)
        n=n+1
        if '\t' not in line:
            continue
        row = line.split('\t')
        if len(row) != 10:
            continue
        transcribed = to_ipa(row[1])
        if (transcribed is None): # if something was not transcribed (punctuation mark, etc)
            row[9] = "IPA="
        else: # if something was transcribed
            row[9] = "IPA="+transcribed
        print(row)
