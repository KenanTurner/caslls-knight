# Things required for a class
#  Title
#  [tables]
#   subtitle (headers)
#   [rows]
#    [cols]
#    [?tests]

title = "Tokenization (see help mode for term definitions):"
def tables(doc):
    return [table(doc)]
def table(doc):
    return [["TEXT", "LEMMA", "POS", "TAG", "DEP", "CHILDREN"],*[[token.text, token.lemma_, token.pos_, token.tag_, token.dep_, ", ".join([child.text for child in token.children])] for token in doc]]