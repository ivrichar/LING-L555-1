"""
This project is clearly unfinished, but I wrote in a few rules for super elementary disambiguation.
the meat of the program is in the get_best_forms function

this program assumes that the input text is in a .src format, like in the utexas.src file.
produces text in a utexas.ref format

first: break the file down by sentences, label the sentence by number
a sentence is a list of lists containing a surface form (string),
and a list of form, tag(s) couplings such that
word[0] is the lemma and word[1] onward is the tags.
--> note: how would this possibly handle contractions? TODO work with contractions
"""

import sys, re

# takes in a form like "<s_sg3>wok<v><tv><inf>" and returns "wok"
def get_lemma(form):
    re.sub('<[^>]+>', '', form)

#takes in a form like "<s_sg3>wok<v><tv><inf>" and returns ("s_sg3", "v", "tv", "inf") the list of tags
def get_tags(form):
    forms = []
    current_tag = ""
    for i in form:
        if ((form[i-1] = "<") or (len(current_tag) > 0)) and (form[i] != '>'): #start adding characters to the tag in order to
            current_tag += form[i]
        else if (form[i] == '>'):
            forms.append(current_tag)
            current_tag = ""
    return forms


"""
general algorithm for this section:
parse the given text, and store each word and its given analyses in a greater list that represents the whole sentence.

run through rules:


each word structure contains:
surface form (string)
list of lemma, tag tuples stored like ((lemma, [tags]), (lemma, [tags]))
    the lemma in these tuples is always a string, and each tag is a string. NOTE: this does not deal with contractions
a word is a (surface form, lemma-tags tuple)
a sentence is a list of words
"""
# this checks if a given list of lemma-tags tuples contains some tag
def has_tag(lemma_tags, tag):
    tag_in_list = False
    i = 0
    while i < len(lemma_tags):
        if tag in lemma_tags[i][1]:
            tag_in_list = True
        i+=1
    return tag_in_list

def get_best_forms(sentence):
    lines = sentence.split('\n')
    all_words = []
    #while i < len(lines):

    for line in lines:
        parts = line.split('/')
        surface_form = parts[0].strip("^")
        if len(parts) = 2: # if  the length is equal to 2, there's no ambiguity
            lemma = get_lemma(parts[1])
            tags = get_tags(parts[1])
            this_word = (surface_form, [[lemma, [tags]]])
            all_words.append(this_word)
        else:
            lemma_tags = [] # add lemma-tag pairs to this
            i = 1
            while i < len(parts):
                lemma = get_lemma(parts[i])
                tags = get_tags(parts[i])
                lemma_tags.append(lemma, tags)
                i += 1
            this_word = (surface_form, lemma_tags)
            all_words.append(this_word)
    final_punct = all_words[-1][0] #surface form of punct mark at end of sentence.
    j = 0
    fixed_sentence = []
    while j < len(all_words):
        this_word = all_words[j]
        #further proof that AI is just nested if statements
        if len(this_word[1]) == 1: # if no ambiguity
            fixed_word = this_word
            continue
        if tag_in_list(this_word[1], "qst"): #checker for if the word could be a question word
            if final_punct == "?":
                fixed_word = (this_word[0], (this_word[1][0], ("qst")))
                continue
        if tag_in_list(this_word[j+1], "n"):#check following word for being a noun if this word is an adjective
            if tag_in_list(all_words[j], "adj"):
                fixed_word = (this_word[0], (this_word[1][0], ("adj")))
                continue
        #check following word for transitive/intransitive verb stuff
        #if the verb could be either transitive or intransitive, check if the next word is an adjective or noun.
        #if it is, it is probably a transitive verb, so mark it as such
        # NOTE: this only works to distinguish between transitive and intransitive forms, it won't distinguish between
        #individual transitive/intransitive forms. this would definitely need more refining.
        if (tag_in_list(this_word[1], "tv") and tag_in_list(this_word[1], "iv"):
            if (tag_in_list(all_words[j+1], "n") or tag_in_list(all_words[j+1], "adj")):
                 for word in this_word[1]:
                     if "tv" in word[1]:
                         fixed_word = word
            else:
                for word in this_word[1]:
                    if "iv" in word[1]:
                        fixed_word = word
        j+=1
        fixed_sentence.append(fixed_word)

    #NOTE: this will not print the tags out in the right order, find some way to do that. it will print them all out right after the lemma
    returned_sentence = ""
    for word in fixed_sentence:
        surface_form = word[0]
        lemma = word[1][0]
        tags = word[1][1]
        this_line = "^" + surface_form + "/" + lemma
        for tag in tags:
            this_line = this_line + "<" + tag + ">"
        returned_sentence = returned_sentence + this_line + "\n"
    return returned_sentence





"""
things to track:
if a question mark appears at the end of the sentence
if directly preceeding word is a determiner and the following word is ambiguous but possibly a noun, it must be a noun.
if a verb is unclear if it is transitive/intransitive and it is directly followed by another noun, mark it as transitive.

in cases like ^le/le<det>/le<prn><rel>$, check what follows it. if followed by a noun, determiner. otherwise, probably rel. prn


keep a triple that tracks the current word, previous word, and next word
"""

text = sys.stdin.read()
# this takes the input text and splits it into strings containing the sentences, etc.

sentences_split = text.split("\\n\\n");
for i in sentences_split:
    sentence = "" # will store the contents of the sentence
    lines = i.split("\n")
    pre  = ""# stores sentence id line, text line, etc
    for line in lines:
        if line[0] = '^':
            sentence += line
            sentence += "\n"
        else:
            pre += line
            pre += "\n"

    print(pre)
    disambiguated = get_best_forms(sentence) #takes in the ambiguous forms, disambiguates, and returns formatted like disambiguated in .ref file.
    print disambiguated
    #print out the disambiguated sentence
