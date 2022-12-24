import spacy
import en_core_web_md
from log import logger

logger.debug("Loading NLP...")
nlp = en_core_web_md.load()
logger.debug("Loaded NLP")