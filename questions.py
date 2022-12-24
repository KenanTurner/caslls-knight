from bsp import *

# Things required for a class
#  Title
#  [tables]
#   subtitle (headers)
#   [rows]
#    [cols]
#    [?tests]

title = "Questions:"
def tables(doc):
    return [
        table_24_30(doc),
        table_30_36(doc),
        table_36_42(doc),
        table_42_48(doc)
    ]
def table_24_30(doc):
    def one(doc):
        return ["Continues to use rising intonation to ask questions", "TODO"]
    def two(doc):
        title = "Uses What + NP or VP?"
        pattern = [isText("what"), lambda token: isNounPhrase(token) or isVerb(token)]
        return [title, is_pattern(pattern, doc)]
    def three(doc):
        title = "Uses Where + NP or VP?"
        pattern = [isText("where"), lambda token: isNounPhrase(token) or isVerb(token)]
        return [title, is_pattern(pattern, doc)]
    def four(doc):
        title = "Uses What NP doing?"
        pattern = [isText("what"),isNounPhrase,isText("doing")]
        return [title, is_pattern(pattern, doc)]
    def five(doc):
        title = "Uses What color?"
        pattern = [isText("what"),isText("color")]
        return [title, is_pattern(pattern, doc)]
    def six(doc):
        title = "Uses Who is X?"
        pattern = [isText("who"),isText("is"),isNounPhrase]
        return [title, is_pattern(pattern, doc)]
    def seven(doc):
        title = "Asks How many/much?"
        pattern = [isText("how"), isText("many","much")]
        return [title, is_pattern(pattern, doc)]
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
        title = "Uses wh-word + sentence"
        pattern = [isTag("WP","WDT","WP$","WRB"), isNounPhrase, isVerb]
        return [title, is_pattern(pattern, doc)]
    def two(doc):
        title = "Asks Why not?"
        pattern = [isText("why"),isText("not")]
        return [title, is_pattern(pattern, doc)]
    def three(doc):
        title = "Asks What for?"
        pattern = [isText("what"),isText("for")]
        return [title, is_pattern(pattern, doc)]
    def four(doc):
        title = "Asks How about + sentence"
        pattern = [isText("how"), isText("about"), isNounPhrase, isVerb]
        return [title, is_pattern(pattern, doc)]
    def five(doc):
        title = "Asks who, how"
        pattern = [isText("who","how")]
        return [title, is_pattern(pattern, doc)]
    def six(doc):
        title = "Asks Can you...? May I...?"
        pattern = [isText("can","may"),isText("you","i")]
        return [title, is_pattern(pattern, doc)]
    def seven(doc):
        title = "Asks What happened?"
        pattern = [isText("what"),isText("happened")]
        return [title, is_pattern(pattern, doc)]
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
        title = "Inconsistently uses auxilary inversion"
        pattern = [isCopula,isNounPhrase]
        pattern2 = [isNounPhrase,isCopula]
        return [title, is_pattern(pattern, doc) and not is_pattern(pattern2, doc)]
    def two(doc):
        title = "Uses 'do' to ask yes/no and wh- questions"
        pattern = [isText("do")]
        return [title, is_pattern(pattern, doc)]
    def three(doc):
        title = "Asks What is/are with Sentence Patterns III,IV,V"
        pattern = [isText("what"),isText("is","are")]
        return [title, is_pattern(pattern, doc) and (isPatternIII(doc) or isPatternIV(doc) or isPatternV(doc))]
    def four(doc):
        title = "Asks Who as object question"
        pattern = [isText("who")]
        return [title, is_pattern(pattern, doc)]
    def five(doc):
        title = "Asks When questions"
        pattern = [isText("when")]
        return [title, is_pattern(pattern, doc)]
    def six(doc):
        return ["Uses future questions", "TODO"]
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
        title = "Uses did to ask yes/no questions without inversion"
        pattern = [isText("did")]
        return [title, is_pattern(pattern, doc) and search(pattern, doc)[0][0] == 0]
    def two(doc):
        title = "Consistently uses inversion of auxiliary and subject noun/pronoun"
        pattern = [isCopula,isNounPhrase]
        pattern2 = [isNounPhrase,isCopula]
        return [title, is_pattern(pattern, doc) and not is_pattern(pattern2, doc)]
    def three(doc):
        return ["Asks for detailed explanations", "TODO"]
    def four(doc):
        title = "Asks Do you know how to...?"
        pattern = [*isPhrase("do you know how to")]
        return [title, is_pattern(pattern, doc)]
    def five(doc):
        title = "Asks What's that for?"
        pattern = [*isPhrase("what 's that for")]
        return [title, is_pattern(pattern, doc)]
    def six(doc):
        title = "Asks What was/were...?"
        pattern = [isText("what"),isText("was","were")]
        return [title, is_pattern(pattern, doc)]
    def seven(doc):
        title = "Asks Was/Were...?"
        pattern = [isText("was","were")]
        return [title, is_pattern(pattern, doc) and search(pattern, doc)[0][0] == 0]
    def eight(doc):
        title = "Asks Which...?"
        pattern = [isText("which")]
        return [title, is_pattern(pattern, doc) and search(pattern, doc)[0][0] == 0]
    def nine(doc):
        title = "Asks Would/could/should...?"
        pattern = [isText("would","could","should")]
        return [title, is_pattern(pattern, doc) and search(pattern, doc)[0][0] == 0]
    return [
        ["42-48 Months",""],
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