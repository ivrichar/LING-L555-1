"""
nasty little rule-based disambiguator for kʼicheʼ
assumes that the input text is in a .src format, like in the utexas.src file.
produces text in a utexas.ref format

first: break the file down by sentences, label the sentence by number
next: keep an array of dicts (think about most efficient way of doing this) that stores the surface form, and all possible analyzed forms
if the number of analyzed forms is just 1, don't try to disambiguate (no ambiguity)
otherwise, do some fun stuff :)


store file contents as a list of (number, sentence) pairs
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

def get_best_forms
text = sys.stdin.read()
sentences = [] # will eventually contain the actual sentences
# this takes the input text and splits it into strings containing the sentences, etc.
sentences_split = text.split("\\n\\n");
for i in sentences_split: # nested loop because i hate my computer
    #sent_num = 0 # will get reassigned as the sentence index
    lines = i.split("\n")
    pre  = ""# stores sentence id line, text line, etc
    for line in lines:
        if line[0] = '^':
            parts = line.split('/')
            surface_form = parts[0].strip("^")
            if len(parts) = 2: # if  the length is equal to 2, there's no ambiguity
                lemma = get_lemma(surface_form)
                tags = get_tags(surface_form)
                #this_sentence = (lemma, tags) #do something w this?
            else:
                kf;

        else:
            pre += line
            pre += "\n"
