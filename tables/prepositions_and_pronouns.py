from tables.bsp import *

# Things required for a class
#  Title
#  [tables]
#   subtitle (headers)
#   [rows]
#    [cols]
#    [?tests]

title = "Prepositions and Pronouns:"
def tables(doc):
    return [
        table_24_30(doc),
        table_30_36(doc),
        table_36_42(doc),
        table_42_48(doc)
    ]
def table_24_30(doc):
    def one(doc):
        pattern = [isText("you","i","it")]
        return ["Uses subject pronouns: you, I, it", is_pattern(pattern, doc)]
    def two(doc):
        pattern = [isText("you","me","it")]
        return ["Uses object pronouns: you, me, it", is_pattern(pattern, doc)]
    def three(doc):
        pattern = [isText("my","your")]
        return ["Uses possessive pronouns pronouns: my, your", is_pattern(pattern, doc)]
    def four(doc):
        pattern = [isText("one")]
        return ["Uses pronoun: one", is_pattern(pattern, doc)]
    def five(doc):
        pattern = [isText("mine")]
        return ["Uses possessive nominative pronoun: mine", is_pattern(pattern, doc)]
    def six(doc):
        pattern = [isText("this","that")]
        return ["Uses demonstrative pronouns: this, that", is_pattern(pattern, doc)]
    def seven(doc):
        pattern = [isText("at","into","to","onto","up","from","off","around","near")]
        pattern2 = [*isPhrase("on top of")]
        return ["Uses adverb-place: at, into, to, onto, up, from, off, around, on top of, near", is_pattern(pattern, doc) or is_pattern(pattern2, doc)]
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
        pattern = [isText("above","across","by","out","under","over","through")]
        pattern2 = [*isPhrase("away from")]
        pattern3 = [*isPhrase("off of")]
        pattern4 = [*isPhrase("next to")]
        return ["Uses adverb-place: above, across, away from, down, below, by, out (of), under, over (to), through, off of, next to", is_pattern(pattern, doc) or is_pattern(pattern2, doc) or is_pattern(pattern3, doc) or is_pattern(pattern4, doc)]
    def two(doc):
        pattern = [isText("he")]
        return ["Uses subject pronoun: he", is_pattern(pattern, doc)]
    def three(doc):
        pattern = [isText("at","in","on")]
        return ["Uses adverb-time: at, in, on", is_pattern(pattern, doc)]
    def four(doc):
        pattern = [isText("with","without")]
        return ["Uses adverb-manner (how): with, without", is_pattern(pattern, doc)]
    def five(doc):
        pattern = [isText("something")]
        return ["Uses 'something'", is_pattern(pattern, doc)]
    def six(doc):
        pattern = [lambda token: isNounPhrase(token) and isText("here","there")(token)]
        return ["Uses 'here', 'there' as noun", is_pattern(pattern, doc)]
    def seven(doc):
        pattern = [isText("of","for","like")]
        return ["Uses prepositions: of, for, like", is_pattern(pattern, doc)]
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
        pattern = [isText("we","she","they")]
        return ["Uses subject pronouns: we, she, they", is_pattern(pattern, doc)]
    def two(doc):
        pattern = [isText("her","him","them")]
        return ["Uses object pronouns: her, him, them", is_pattern(pattern, doc)]
    def three(doc):
        pattern = [lambda token: token.tag_ == "PRP" and isText("it")(token)]
        return ["Use ambient 'it'", is_pattern(pattern, doc)]
    def four(doc):
        pattern = [isText("everybody","everyone","everything")]
        return ["Uses indefinite pronouns: everybody/one/thing", is_pattern(pattern, doc)]
    def five(doc):
        pattern = [isText("behind","between")]
        pattern2 = [*isPhrase("in back of")]
        pattern3 = [*isPhrase("in front of")]
        pattern4 = [*isPhrase("in the middle of")]
        return ["Uses adverb-place: behind, in back/front of, between, in the middle of", is_pattern(pattern, doc) or is_pattern(pattern2, doc) or is_pattern(pattern3, doc) or is_pattern(pattern4, doc)]
    def six(doc):
        pattern = [isText("with","without")]
        return ["Uses adverb-accompaniment (who, what): with, without", is_pattern(pattern, doc)]
    def seven(doc):
        pattern = [isText("during")]
        return ["Uses adverb-time: during", is_pattern(pattern, doc)]
    return [
        ["36-42 Months",""],
        one(doc),
        two(doc),
        three(doc),
        four(doc),
        five(doc),
        six(doc),
        seven(doc),
    ]
def table_42_48(doc):
    def one(doc):
        pattern = [isText("myself")]
        return ["Uses reflex pronoun: myself", is_pattern(pattern, doc)]
    def two(doc):
        pattern = [isText("its","her","his")]
        return ["Uses possessive pronouns: its, her, his", is_pattern(pattern, doc)]
    def three(doc):
        pattern = [isText("after","before","beside","beyond")]
        return ["Uses adverb-place: after, before, beside, beyond", is_pattern(pattern, doc)]
    def four(doc):
        pattern = [isText("from","to")]
        return ["Uses adverb-time: from, to", is_pattern(pattern, doc)]
    def five(doc):
        pattern = [isText("someone","somebody")]
        return ["Uses indefinite pronouns: someone/body", is_pattern(pattern, doc)]
    return [
        ["42-48 Months",""],
        one(doc),
        two(doc),
        three(doc),
        four(doc),
        five(doc),
    ]