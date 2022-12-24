from bsp import *

# Things required for a class
#  Title
#  [tables]
#   subtitle (headers)
#   [rows]
#    [cols]
#    [?tests]

title = "Tense and Negation:"
def tables(doc):
    return [
        table_24_30(doc),
        table_30_36(doc),
        table_36_42(doc),
        table_42_48(doc)
    ]
def table_24_30(doc):
    def one(doc):
        pattern = [lambda token: token.text[-3:].lower() == "ing" and isVerb(token)]
        pattern2 = [isCopula]
        return ["Uses '-ing' with no auxiliary 'be'", is_pattern(pattern, doc) and not is_pattern(pattern2, doc)]
    def two(doc):
        pattern = [isNounPhrase, isText("no"), isVerb]
        return ["Uses NP no VP", is_pattern(pattern, doc)]
    def three(doc):
        pattern = [*isPhrase("do n't")]
        pattern2 = [*isPhrase("ca n't")]
        return ["Uses don't,can't to indicate nonexistence, disappearance, nonoccurrence", is_pattern(pattern, doc) or is_pattern(pattern2, doc)]
    def four(doc):
        pattern = [lambda token: isText("no")(token) and token.dep_ == "det"]
        return ["Uses no as a negative determiner", is_pattern(pattern, doc)]
    def five(doc):
        pattern = [lambda token: token.tag_ == "VBD" and token.text[-2:].lower() != "ed"]
        return ["Uses a few irregular past tense forms", is_pattern(pattern, doc)]
    return [
        ["24-30 Months",""],
        one(doc),
        two(doc),
        three(doc),
        four(doc),
        five(doc),
    ]
def table_30_36(doc):
    def one(doc):
        pattern = [isNounPhrase, isText("not"), isVerb]
        return ["Uses NP not VP", is_pattern(pattern, doc)]
    def two(doc):
        pattern = [lambda token: token.tag_ == "VBD" and token.text[-2:].lower() == "ed"]
        return ["Uses over-generalized '-ed'", is_pattern(pattern, doc)]
    def three(doc):
        pattern = [*isPhrase("do n't")]
        pattern2 = [*isPhrase("ca n't")]
        pattern3 = [*isPhrase("not gon na")]
        return ["Uses can't/don't/not gonna to reject & prohibit", is_pattern(pattern, doc) or is_pattern(pattern2, doc) or is_pattern(pattern3, doc)]
    def four(doc):
        pattern = [*isPhrase("that 's not")]
        pattern2 = [*isPhrase("it 's not")]
        return ["Uses That's not..., It's not...", is_pattern(pattern, doc) or is_pattern(pattern2, doc)]
    def five(doc):
        # pattern = [isText("'s", "'m"), lambda token: token.tag_ == "VBG"]
        return ["Uses contractible forms for present progressive", "TODO"]
    def six(doc):
        pattern = [isText("nothing","none")]
        return ["Uses nothing, none", is_pattern(pattern, doc)]
    def seven(doc):
        pattern = [*isPhrase("i 'm not")]
        pattern2 = [isText("i 'm never")]
        return ["Uses I'm not/never", is_pattern(pattern, doc) or is_pattern(pattern2, doc)]
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
        title = "Uses won't"
        pattern = [*isPhrase("wo n't")]
        return [title, is_pattern(pattern, doc)]
    def two(doc):
        title = "Uses present progressive: is/are/am + verb -ing"
        pattern = [lambda token: isText("is","are","am"), lambda token: isVerb(token) and token.text[-3:] == "ing"]
        return [title, is_pattern(pattern, doc)]
    def three(doc):
        # title = "Uses uncontractible present progessive"
        # pattern = [isText("am", "is", "are", "was", "were"), lambda token: token.tag_ == "VBG"]
        # pattern2 = [isText("'m","'s","'re")]
        return ["Uses uncontractible present progessive", "TODO"]
    def four(doc):
        title = "Uses 'don't know how to'"
        pattern = [*isPhrase("do n't know how to")]
        return [title, is_pattern(pattern, doc)]
    def five(doc):
        title = "Uses nobody, none"
        pattern = [isText("nobody","none")]
        return [title, is_pattern(pattern, doc)]
    def six(doc):
        title = "Uses couldn't, wouldn't"
        pattern = [*isPhrase("could n't")]
        pattern2 = [*isPhrase("would n't")]
        return [title, is_pattern(pattern, doc) or is_pattern(pattern2, doc)]
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
        title = "Uses copula be + negation"
        pattern = [isCopula, isLemma("not")]
        return [title, is_pattern(pattern, doc)]
    def two(doc):
        title = "Uses infrequent present perfect"
        pattern = [isLemma("have"), isTag("VBN")]
        return [title, is_pattern(pattern, doc)]
    def three(doc):
        title = "Uses past tense '-ed'"
        pattern = [lambda token: token.tag_ == "VBD" and token.text[-2:].lower() == "ed"]
        return [title, is_pattern(pattern, doc)]
    def four(doc):
        title = "Uses many irregular past forms"
        pattern = [lambda token: token.tag_ == "VBD" and token.text[-2:].lower() != "ed"]
        return [title, is_pattern(pattern, doc)]
    def five(doc):
        title = "Uses 3rd person singular present tense: -s"
        pattern = [lambda token: isTag("VBZ")(token) and token.lemma_ != "be" and token.text[-1] == "s"]
        return [title, is_pattern(pattern, doc)]
    return [
        ["42-48 Months",""],
        one(doc),
        two(doc),
        three(doc),
        four(doc),
        five(doc),
    ]