from func_re import *

# helper sets
COPULAE = set(filter(None,(line.strip() for line in open('data/copulae.txt') if not line.startswith("#"))))
LOCATION_ADV = set(filter(None,(line.strip() for line in open('data/locations.txt') if not line.startswith("#"))))
TIME_NP = set(filter(None,(line.strip() for line in open('data/time.txt') if not line.startswith("#"))))

def isText(*text):
    return lambda token: token.text.lower() in text
def isLemma(*text):
    return lambda token: token.lemma_ in text
def isPos(*pos):
    return lambda token: token.pos_ in pos
def isTag(*tag):
    return lambda token: token.tag_ in tag
def isDep(*dep):
    return lambda token: token.dep_ in dep
def isIn(attr, set):
    return lambda token: getattr(token, attr) in set
def isPhrase(phrase):
    for text in phrase.split():
        yield isText(text.lower())

def isNounPhrase(token):
    # return token.dep_ == "nsubj" or ((token.pos_ == "NOUN" or token.pos_ == "PRON") and token.dep_ in {"dobj", "dative", "attr", "oprd", "pobj"})
    return token.dep_ == "nsubj" or (token.pos_ == "NOUN" or token.pos_ == "PRON" or token.pos_ == "PROPN")

def isCopula(token):
    return (
        # token.pos_ == "VERB" and any([child.pos_ == "ADP" and child.dep_ == "prep" for child in token.children]) or
        token.pos_ == "AUX" and token.lemma_ == "be" or
        token.pos_ == "VERB" and token.lemma_ in COPULAE and any([child.dep_ != "nsubj" for child in token.children if child.dep_ != "punct"])
    )

def isVerb(token):
    return token.pos_ == "VERB"

def isAdj(token):
    return token.pos_ == "ADJ"

def isAdpos(token):
    return token.pos_ == "ADP" and any([child.dep_ == "pobj" for child in token.children])

def isLocation(token):
    return isAdpos(token) and token.lemma_ in LOCATION_ADV

def isTime(token):
    return (token.pos_ == "ADV" or isNounPhrase(token)) and token.lemma_ in TIME_NP

def isRecipient(token):
    return any([child.dep_ == "poss" for child in token.children]) or token.pos_ == "PRON"

# NP + V
def isPatternI(doc):
    pattern = [isNounPhrase, isVerb]
    return is_pattern(pattern, doc)
    
# NP + V + NP
def isPatternII(doc):
    pattern = [isNounPhrase, isVerb, isNounPhrase]
    return is_pattern(pattern, doc)
    
# NP + Copula + ADJ
def isPatternIII(doc):
    pattern = [isNounPhrase, isCopula, isAdj]
    return is_pattern(pattern, doc)
    
# NP + Copula + NP
def isPatternIV(doc):
    pattern = [isNounPhrase, isCopula, isNounPhrase]
    return is_pattern(pattern, doc)
    
# NP + Copula + NP (location/recipient/time)
# def isPatternV(doc):
    # pattern = [isNounPhrase, isCopula, isNounPhrase]
    # result = search(pattern, doc)
    # if len(result) != len(pattern):
        # return False # Must be PatternIV to be PatternV
    # i,_ = result.pop()
    # token = doc[i]
    # return isLocation(token) or isRecipient(token) or isTime(token)
    
def isPatternV(doc):
    pattern = [isNounPhrase, isCopula, func_or(isLocation, isRecipient, isTime)]
    return is_pattern(pattern, doc)
    
title = "Basic Sentence Pattern:"
def tables(doc):
    return [morp_table(doc), bsp_table(doc)]
def morp_table(doc):
    return [["TEXT", "NP?", "ADJ?", "V?", "COP?", "ADV-LOC?", "RECIPIENT?", "TIME?"],*[[token.text, isNounPhrase(token), isAdj(token), isVerb(token), isCopula(token), isLocation(token), isRecipient(token), isTime(token)] for token in doc]]
def bsp_table(doc):
    return [["I?", "II?", "III?", "IV?", "V?"],[isPatternI(doc), isPatternII(doc), isPatternIII(doc), isPatternIV(doc), isPatternV(doc)]]