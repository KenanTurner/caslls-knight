from tables.bsp import *

# Things required for a class
#  Title
#  [tables]
#   subtitle (headers)
#   [rows]
#    [cols]
#    [?tests]

title = "Emerging Complexity:"
def tables(doc):
    return [
        table_24_30(doc),
        table_30_36(doc),
        table_36_42(doc),
        table_42_48(doc)
    ]
def table_24_30(doc):
    def one(doc):
        title = "Uses adverb-time: now, already, again"
        pattern = [isText("now","already","again")]
        return [title, is_pattern(pattern, doc)]
    def two(doc):
        title = "Uses simple wh- clauses for direct objects"
        pattern = [isTag("WP","WDT","WP$","WRB"), isNounPhrase]
        return [title, is_pattern(pattern, doc)]
    def three(doc):
        title = "Uses locative adverbs: there, here, outside, up"
        pattern = [isText("there","here","outside","up")]
        return [title, is_pattern(pattern, doc)]
    def four(doc):
        title = "Uses too (inclusion)"
        pattern = [isText("too")]
        return [title, is_pattern(pattern, doc)]
    def five(doc):
        title = "Uses unmarked infinitives w/ help, watch, let, make"
        pattern = [isText("help","watch","let","make"),lambda token: token.lemma_ == token.text.lower() and isTag("VB")(token)]
        return [title, is_pattern(pattern, doc)]
    def six(doc):
        title = "Uses intensifiers: very, so, too, really"
        pattern = [lambda token: isText("very","so","too","really")(token) and isDep("advmod")(token)]
        return [title, is_pattern(pattern, doc)]
    return [
        ["24-30 Months",""],
        one(doc),
        two(doc),
        three(doc),
        four(doc),
        five(doc),
        six(doc),
    ]
def table_30_36(doc):
    def one(doc):
        title = "Uses 2 adverbs manner: fast, slowly, quietly, carefully"
        pattern = [isText("fast","slowly","quietly","carefully")]
        return [title, is_pattern(pattern, doc)]
    def two(doc):
        title = "Uses and (then) to conjoin sentences"
        pattern = [lambda token: isText("and")(token) and isTag("CC")(token)]
        return [title, is_pattern(pattern, doc)]
    def three(doc):
        title = "Uses adverb-time: later, never, yesterday, always, tomorrow, today"
        pattern = [isText("later","never","yesterday","always","tomorrow","today")]
        return [title, is_pattern(pattern, doc)]
    def four(doc):
        return ["Uses a full sentence for D.O.", "TODO"]
    def five(doc):
        title = "Uses 'or' to state choice"
        pattern = [lambda token: isText("or")(token) and isTag("CC")(token)]
        return [title, is_pattern(pattern, doc)]
    return [
        ["30-36 Months",""],
        one(doc),
        two(doc),
        three(doc),
        four(doc),
        five(doc),
    ]
def table_36_42(doc):
    def one(doc):
        title = "Uses and, but to oppose"
        pattern = [lambda token: isText("and","but")(token) and isTag("CC")(token)]
        return [title, is_pattern(pattern, doc)]
    def two(doc):
        return ["Uses multiple embeddings", "TODO"]
    def three(doc):
        title = "Uses first, then"
        pattern = [isText("first","then")]
        return [title, is_pattern(pattern, doc)]
    def four(doc):
        title = "Uses days of the week"
        pattern = [isText("monday","tuesday","wednesday","thursday","friday","saturday","sunday")]
        return [title, is_pattern(pattern, doc)]
    def five(doc):
        title = "Uses almost, hardly"
        pattern = [isText("almost","hardly")]
        return [title, is_pattern(pattern, doc)]
    def six(doc):
        title = "Uses just, only, even"
        pattern = [isText("just","only","even")]
        return [title, is_pattern(pattern, doc)]
    def seven(doc):
        title = "Uses soon, next, finally"
        pattern = [isText("soon","next","finally")]
        return [title, is_pattern(pattern, doc)]
    def eight(doc):
        title = "Uses 'all the time', 'every day'"
        pattern = [*isPhrase("all the time")]
        pattern2 = [*isPhrase("every day")]
        return [title, is_pattern(pattern, doc) or is_pattern(pattern2, doc)]
    def nine(doc):
        return ["Uses tenseless clauses as D.O.", "TODO"]
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
    ]
def table_42_48(doc):
    def one(doc):
        return ["Uses conjoined & embedded clauses in same sentence", "TODO"]
    def two(doc):
        title = "Uses infinitives after D.O."
        pattern = [isNounPhrase,isNounPhrase,isText("to"),isVerb]
        return [title, is_pattern(pattern, doc)]
    def three(doc):
        title = "Uses next/last + month/week/year"
        pattern = [isText("next","last"),isText("month","week","year")]
        return [title, is_pattern(pattern, doc)]
    def four(doc):
        title = "Uses 3+ adverbs-manner"
        pattern = [lambda token: isDep("advmod")(token) and token.text[-2:] == "ly"]
        return [title, is_pattern(pattern, doc)]
    def five(doc):
        title = "Uses 'but' to show exception"
        pattern = [isText("but")]
        return [title, is_pattern(pattern, doc)]
    def six(doc):
        title = "Uses verb forms as D.O."
        pattern = [isNounPhrase,isVerb,isDep("xcomp")]
        return [title, is_pattern(pattern, doc)]
    return [
        ["42-48 Months",""],
        one(doc),
        two(doc),
        three(doc),
        four(doc),
        five(doc),
        six(doc),
    ]