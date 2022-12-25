from tables.bsp import *
from tools.nlp import nlp

# Things required for a class
#  Title
#  [tables]
#   subtitle (headers)
#   [rows]
#    [cols]
#    [?tests]

title = "Nouns and Noun Modifiers:"
def tables(doc):
    return [
        table_24_30(doc),
        table_30_36(doc),
        table_36_42(doc),
        table_42_48(doc)
    ]
def table_24_30(doc):
    def one(doc):
        pattern = [isNounPhrase, lambda token: token.lemma_ == "and", isNounPhrase]
        return ["Conjoins nouns with and", is_pattern(pattern, doc)]
    def two(doc):
        pattern = [isAdj, isNounPhrase]
        return ["Uses modifier + noun as direct object", is_pattern(pattern, doc)]
    def three(doc):
        pattern = [lambda token: token.text.lower() == "a" and token.dep_ == "det"]
        return ["Uses indefinite article: a", is_pattern(pattern, doc)]
    def four(doc):
        color = nlp("red orange yellow green blue indigo violet")
        size = nlp("large small massive tiny")
        pattern = [lambda token: isAdj(token) and (color.similarity(doc) > 0.5 or size.similarity(doc) > 0.5)]
        return ["Uses color/size adjective", is_pattern(pattern, doc)]
    def five(doc):
        pattern = [lambda token: token.text.lower() == "some" or token.text.lower() == "another" or token.text.lower() == "other"]
        return ["Uses some, another, other", is_pattern(pattern, doc)]
    def six(doc):
        return ["Uses lots of", "lots of" in doc.text.lower()]
    def seven(doc):
        pattern = [lambda token: token.text.lower() == "number", lambda token: token.pos_ == "NUM"]
        return ["Uses number + N", is_pattern(pattern, doc)]
    def eight(doc):
        pattern = [lambda token: token.text.lower() == "some", lambda token: isNounPhrase(token) and not token.tag_ in {"NNS","NNPS"}]
        return ["Uses some with non-count nouns", is_pattern(pattern, doc)]
    def nine(doc):
        pattern = [lambda token: isNounPhrase(token) and token.dep_ == "compound"]
        return ["Uses nouns as modifiers", is_pattern(pattern, doc)]
    return [
        ["24-30 Months",""],
        one(doc),
        two(doc),
        three(doc),
        four(doc),
        five(doc),
        six(doc),
        seven(doc),
        eight(doc),
        nine(doc),
    ]
def table_30_36(doc):
    def one(doc):
        return ["Uses early relative clauses", "TODO"]
    def two(doc):
        pattern = [lambda token: token.text.lower() == "the" and token.dep_ == "det"]
        return ["Uses definite article: the", is_pattern(pattern, doc)]
    def three(doc):
        pattern = [lambda token: isNounPhrase(token) and all([child.dep_ == "det" or child.dep_ == "amod" for child in token.children]) and len([*token.children]) >= 2]
        return ["Uses elaborated noun phrases", is_pattern(pattern, doc)]
    def four(doc):
        pattern = [lambda token: token.text.lower() in {"many", "all"}]
        pattern2 = [lambda token: token.text.lower() == "a", lambda token: token.text.lower() == "lot", lambda token: token.text.lower() == "of"]
        return ["Uses quantifiers: many, all, a lot of", is_pattern(pattern, doc) or is_pattern(pattern2, doc)]
    def five(doc):
        pattern = [lambda token: token.text.lower() == "an" and token.dep_ == "det"]
        return ["Uses indefinite article: an", is_pattern(pattern, doc)]
    def six(doc):
        pattern = [isAdj, isAdj, isNounPhrase]
        return ["Uses double adjectives", is_pattern(pattern, doc)]
    def seven(doc):
        pattern = [lambda token: token.text.lower() in {"give","take","show"}, isNounPhrase, lambda token: token.text.lower() == "to", isNounPhrase]
        return ["Uses indirect objects", is_pattern(pattern, doc)]
    return [
        ["30-36 Months",""],
        one(doc),
        two(doc),
        three(doc),
        four(doc),
        five(doc),
        six(doc),
        seven(doc),
    ]
def table_36_42(doc):
    def one(doc):
        pattern = [lambda token: token.tag_ in {"NNS","NNPS"}]
        return ["Uses plural -s, -es", is_pattern(pattern, doc)]
    def two(doc):
        pattern = [lambda token: token.tag_ in {"POS"}]
        return ["Uses possessive 's", is_pattern(pattern, doc)]
    def three(doc):
        pattern = [lambda token: token.text in {"a","an","the"}]
        return ["Use a(n)/the to show specific vs. nonspecific", is_pattern(pattern, doc)]
    def four(doc):
        return ["Produces first opposites", "TODO"]
    def five(doc):
        pattern = [isNounPhrase]
        return ["Always uses a subject", is_pattern(pattern, doc)]
    def six(doc):
        return ["Noun phrase includes variety of modifiers", "TODO"]
    def seven(doc):
        pattern = [isText("just")]
        pattern2 = [*isPhrase("only a little bit")]
        pattern3 = [*isPhrase("a few more")]
        return ["Uses more elaborate modifiers (just/only a little bit/a few more)", is_pattern(pattern, doc) or is_pattern(pattern2, doc) or is_pattern(pattern3, doc)]
    def eight(doc):
        texture = {'craggy', 'fuzzy', 'bumpy', 'pokey', 'rocky', 'bristly', 'rubbery', 'lumpy', 'gritty', 'seedy', 'smooth', 'grainy', 'slippery', 'soft', 'hard'}
        pattern = [lambda token: isAdj(token) and isText(*texture)(token)]
        return ["Uses adjectives: texture", is_pattern(pattern, doc)]
    def nine(doc):
        pattern = [lambda token: token.text.lower() in {'ordinals', 'next', 'much', 'few', 'several', 'any', 'both', 'every', 'each', 'first', 'last'}]
        return ["Uses first/last/ordinals/next/both/any/each/few/every/much/several", is_pattern(pattern, doc)]
    def ten(doc):
        pattern = [lambda token: isNounPhrase(token) and any([child.pos_ == "VERB" and child.dep_ in {"amod","compound"} for child in token.children])]
        return ["Uses verbs as adjectives", is_pattern(pattern, doc)]
    return [
        ["36-42 Months",""],
        one(doc),
        two(doc),
        three(doc),
        four(doc),
        five(doc),
        six(doc),
        seven(doc),
        eight(doc),
        nine(doc),
        ten(doc),
    ]
def table_42_48(doc):
    def one(doc):
        pattern = [isTag("NNS"), isText("are")]
        return ["Uses are w/ plurals", is_pattern(pattern, doc)]
    def two(doc):
        pattern = [isText("a"), isNounPhrase, isText("of")]
        return ["uses pre-articles", is_pattern(pattern, doc)]
    def three(doc):
        pattern = [isText("most","least")]
        return ["Uses most,least", is_pattern(pattern, doc)]
    def four(doc):
        return ["Uses no article when acceptable", "TODO"]
    def five(doc):
        return ["Uses D.O. + relative same subject as main subject", "TODO"]
    return [
        ["42-48 Months",""],
        one(doc),
        two(doc),
        three(doc),
        four(doc),
        five(doc),
    ]