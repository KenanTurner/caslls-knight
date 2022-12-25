from tables.bsp import *

# Things required for a class
#  Title
#  [tables]
#   subtitle (headers)
#   [rows]
#    [cols]
#    [?tests]

title = "Verbs and Modals:"
def tables(doc):
    return [
        table_24_30(doc),
        table_30_36(doc),
        table_36_42(doc),
        table_42_48(doc)
    ]
def table_24_30(doc):
    def one(doc):
        return ["Uses sentence Pattern I: NP + V", isPatternI(doc)]
    def two(doc):
        return ["Uses sentence Pattern II: NP + V + NP", isPatternII(doc)]
    def three(doc):
        pattern = [isText("gonna","wanna")]
        pattern2 = [*isPhrase("gon na")]
        pattern3 = [*isPhrase("wan na")]
        return ["Uses gonna/wanna to express wish/intention", is_pattern(pattern, doc) or is_pattern(pattern2, doc) or is_pattern(pattern3, doc)]
    def four(doc):
        pattern = [isNounPhrase, isCopula, isLocation]
        return ["Uses sentence Pattern V: NP + cop. + location", is_pattern(pattern, doc)]
    def five(doc):
        pattern = [isText("is")]
        return ["Uses uncontractible copula: is", is_pattern(pattern, doc)]
    def six(doc):
        return ["Uses sentence Pattern IV: NP + cop. + equivalent", isPatternIV(doc)]
    def seven(doc):
        pattern = [lambda token: token.pos_ == "VERB" and any([child.dep_ == "prt" for child in token.children])]
        return ["Uses particle verbs", is_pattern(pattern, doc)]
    return [
        ["24-30 Months",""],
        one(doc),
        two(doc),
        three(doc),
        four(doc),
        five(doc),
        six(doc),
        seven(doc),
    ]
def table_30_36(doc):
    def one(doc):
        pattern = [isText("can","will","could")]
        pattern2 = [*isPhrase("it 's")]
        return ["Uses can, will, let's could", is_pattern(pattern, doc) or is_pattern(pattern2, doc)]
    def two(doc):
        pattern = [isVerb, isText("and"), isVerb]
        return ["Uses 'and' to conjoin verbs", is_pattern(pattern, doc)]
    def three(doc):
        pattern = [isText("to"), isVerb]
        return ["Uses simple infinitives", is_pattern(pattern, doc)]
    def four(doc):
        return ["Uses imperatives to make request or give command", "TODO"]
    def five(doc):
        pattern = [isText("am","are","is")]
        return ["Uses present tense copula be: am, are, is", is_pattern(pattern, doc)]
    def six(doc):
        return ["Uses sentence pattern III: NP + cop. + adjective", isPatternIII(doc)]
    def seven(doc):
        pattern = [lambda token: isCopula(token) and token.text[0] == "'"]
        return ["Uses contractible copula in Patterns III, IV, and V", (isPatternIII(doc) or isPatternIV(doc) or isPatternV(doc)) and is_pattern(pattern, doc)]
    def eight(doc):
        pattern = [lambda token: token.lemma_ == "will" and token.text[0] == "'"]
        return ["Uses contractible future", is_pattern(pattern, doc)]
    return [
        ["30-36 Months",""],
        one(doc),
        two(doc),
        three(doc),
        four(doc),
        five(doc),
        six(doc),
        seven(doc),
        eight(doc),
    ]
def table_36_42(doc):
    def one(doc):
        pattern = [isText("hafta","would","might","should")]
        pattern2 = [*isPhrase("got ta")]
        pattern3 = [*isPhrase("'d better")]
        return ["Uses hafta, gotta, would, might, should, 'd better", is_pattern(pattern, doc) or is_pattern(pattern2, doc) or is_pattern(pattern3, doc)]
    def two(doc):
        pattern = [*isPhrase("know how to")]
        return ["Uses 'know how to ___'", is_pattern(pattern, doc)]
    def three(doc):
        pattern = [isNounPhrase, isCopula, isRecipient]
        return ["Use sentence pattern V: NP + cop. + reason/recipient", is_pattern(pattern, doc)]
    def four(doc):
        pattern = [isNounPhrase, isCopula, isTime]
        return ["Use sentence pattern V: NP + cop. + adverb-time", is_pattern(pattern, doc)]
    def five(doc):
        pattern = [isLemma("look","taste","smell","feel","sound")]
        return ["Use sentence pattern IV with sense verbs", is_pattern(pattern, doc) and isPatternIV(doc)]
    def six(doc):
        return ["Uses 4.3 words/sentence", len(doc) > 4]
    return [
        ["36-42 Months",""],
        one(doc),
        two(doc),
        three(doc),
        four(doc),
        five(doc),
        six(doc),
    ]
def table_42_48(doc):
    def one(doc):
        pattern = [isText("must")]
        return ["Uses 'must'", is_pattern(pattern, doc)]
    def two(doc):
        pattern = [isText("was","were")]
        return ["Uses past tense copula: was, were", is_pattern(pattern, doc)]
    def three(doc):
        pattern = [isText("became","changed","turned")]
        return ["Use sentence pattern IV: became, changed/turned into", is_pattern(pattern, doc) and isPatternIV(doc)]
    return [
        ["42-48 Months",""],
        one(doc),
        two(doc),
        three(doc),
    ]