import sys
import spacy

if __name__ == "__main__":
    for item in sys.argv[1:]:
        print(f"{item}: {spacy.explain(item)}")