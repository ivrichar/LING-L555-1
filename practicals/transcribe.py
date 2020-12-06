import sys

# create a new list with the transcriptions in the table
transcriptions = []

# creates a list of tuples with the latin (nahuatl) alphabet
# and the ipa-ish character
fd = open('transtable.txt', 'r')
for line in fd.readlines():
    stripped = line.strip('\n')
    (latin, ipa) = stripped.split(' ')
    # for some reason it said it was split by spaces instead of tabs even though I used tabs, so I just had it split by space
    couple = (latin, ipa)
    transcriptions.append(couple)

# this function converts a string from nahuatl orthography to IPA (ish)
# it reads a string by character
def to_ipa(s):
    in_ipa = ""
    lowered = s.lower()
    for letter in lowered: # iterates by character through string
        for pair in transcriptions: #iterates by tuple in the transcription list
            if letter == pair[0]: #if the current letter of the given string is equal to the latin letter in the tuple
                in_ipa = in_ipa + pair[1] #concatenate the already transcribed characters and this new character
                continue # the character has been found, so we can break the inner loop over transcriptions for this character only
    return in_ipa

text = sys.stdin.read()

lines = text.split("\n") #split by line in input text



#for j in range(0, len(lines)):
for line in lines:

        #if '\t' not in line:
        #    continue
    row = line.split('\t')
    if len(row) != 10:
        print(row[0])
        continue
    transcribed = to_ipa(row[1])
    if (transcribed is None): # if something was not transcribed (punctuation mark, etc)
        row[9] = "IPA="
    else: # if something was transcribed
        row[9] = "IPA="+transcribed
    count = row[0]
    token = row[1]
    transcription = row[9]
    print(f'{count}\t{token}\t_\t_\t_\t_\t_\t_\t_\t{transcription}')


"""
Questions:

If there's an environment that triggers a certain sound, like if a letter is a certain sound
after a vowel and a different sound in other environments, then the program could look
at the environment surrounding the letter to see which

Each letter, instead of containing a single mapping, could contain a list of tuples containing an environment (like
a certain letter combination)
Similarly, we could check if there was no preceeding character or following character in this by checking what was
on either side of this character in the string.
"""
