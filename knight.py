# Capture all stdout to disk
import sys
import re
from io import TextIOBase
from datetime import date
class Tee(TextIOBase):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    def __init__(self, stream, file):
        self.stream = stream
        self.log = file
    def write(self, message):
        result = self.stream.write(message)
        self.log.write(Tee.ansi_escape.sub('', message))
        return result
    def read(self, size=-1):
        result = self.stream.read(size)
        self.log.write(Tee.ansi_escape.sub('', result))
        return result
    def readline(self, size=-1):
        result = self.stream.readline(size)
        self.log.write(Tee.ansi_escape.sub('', result))
        return result

# Spacy and nlp imports
import spacy
from spacy.glossary import GLOSSARY
from nlp import nlp

# logging
from log import logger
import atexit

# Formatting imports
from tabulate import tabulate
from colorama import just_fix_windows_console, Fore, Back, Style
def colored(text, fore="RESET", back="RESET", style="NORMAL"):
    return getattr(Fore, fore.upper()) + getattr(Back, back.upper()) + getattr(Style, style.upper()) + text + Style.RESET_ALL
def printTables(doc, ref):
    print(colored(ref.title,"CYAN",style="BRIGHT"))
    for table in ref.tables(doc):
        str = tabulate(table, headers="firstrow", tablefmt="pretty")
        str = str.replace("True", colored("True","GREEN",style="BRIGHT")).replace("False", colored("False","RED",style="BRIGHT")).replace("TODO", colored("TODO","YELLOW",style="BRIGHT"))
        print(str)
    print()

# table imports
import tokens
import bsp
import nouns_and_noun_modifiers
import prepositions_and_pronouns
import verbs_and_modals
import tense_and_negation
import emerging_complexity
import questions

# TODO Remove
SENTENCES = list(filter(None,(line.strip() for line in open('data/sentences.txt') if not line.startswith("#"))))
sentences = SENTENCES

if __name__ == "__main__":
    try:
        # write stdout and stdin to history file
        log = open(f'history-{str(date.today())}.txt','a')
        sys.stdout = Tee(sys.stdout, log)
        sys.stdin = Tee(sys.stdin, log)
        
        # Setup logger
        def onExit(logger):
            logger.info("#################### __main__ halted ####################")
        atexit.register(lambda : onExit(logger))
        logger.info("#################### __main__ started ####################")
        
        # colorama
        just_fix_windows_console()
        
        # Help mode (duh)
        help_mode = False
        
        while True:
            if help_mode:
                sentence = input(colored("Please enter a keyword to lookup (or type 'exit' to leave help mode) (or type ctrl-c to exit):\n","YELLOW",style="BRIGHT")).strip()
                logger.debug(f"HELP: '{sentence}'")
                
                if sentence.lower() == "exit":
                    print(colored("Now exiting help mode...","YELLOW",style="BRIGHT"))
                    help_mode = False
                    print(Style.RESET_ALL)
                    continue
                
                if sentence in GLOSSARY:
                    print(colored(GLOSSARY[sentence],"GREEN",style="BRIGHT"))
                else:
                    print(colored("Unknown term. ","RED",style="BRIGHT"))
                    if sentence.upper() in GLOSSARY:
                        print(colored("Perhaps you forgot to capitalize?","RED",style="BRIGHT"))
            else:
                sentence = input(colored("Please enter a sentence (or type 'help' to enter help mode) (or type ctrl-c to exit):\n","MAGENTA",style="BRIGHT")).strip()
                # sentence = sentences.pop(0)
                logger.debug(f"Input: '{sentence}'")
                
                if sentence.lower() == "help":
                    print(colored("Now entering help mode...","YELLOW",style="BRIGHT"))
                    print(colored("The full glossary of terms can be found at the following sites:","CYAN",style="BRIGHT"))
                    print(colored("Universal POS Tags: http://universaldependencies.org/u/pos/","CYAN",style="BRIGHT"))
                    print(colored("Penn Treebank POS Tags: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html","CYAN",style="BRIGHT"))
                    print(colored("Universal Dependency Labels: https://github.com/clir/clearnlp-guidelines/blob/master/md/specifications/dependency_labels.md","CYAN",style="BRIGHT"))
                    help_mode = True
                    continue
                
                doc = nlp(sentence)
                
                print()
                printTables(doc, tokens)
                printTables(doc, bsp)
                printTables(doc, nouns_and_noun_modifiers)
                printTables(doc, prepositions_and_pronouns)
                printTables(doc, verbs_and_modals)
                printTables(doc, tense_and_negation)
                printTables(doc, emerging_complexity)
                printTables(doc, questions)
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as err:
        print("Uncaught Exception! Exiting...")
        logger.error(f"Uncaught Exception!", exc_info=1)
        print("See castle.log for more info")