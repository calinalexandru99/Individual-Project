from googletrans import Translator
import yake
from enum import Enum
from googlesearch import search
import requests
from enums import Language
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import time
import sys

class Language(Enum):
    DUTCH = 0
    FRENCH = 1
    GERMAN = 2
    ITALIAN = 3
    POLISH = 4
    PORTUGUESE = 5
    ROMANIAN = 6
    SPANISH = 7
    SWEDISH = 8

translator = Translator()

# the function aggregates the translations of the initial document into a Python list
def get_array_of_translations(initial_document):
    return [get_dutch_translation(initial_document), get_french_translation(initial_document),
            get_german_translation(initial_document), get_italian_translation(initial_document),
            get_polish_translation(initial_document), get_portuguese_translation(initial_document),
            get_romanian_translation(initial_document), get_spanish_translation(initial_document),
            get_swedish_translation(initial_document)]


# the function receives as input the document submitted for evaluation and returns its translation into Dutch
def get_dutch_translation(initial_document):
    dutch_translation = translator.translate(initial_document, dest='nl', src='en')
    return dutch_translation.text


# the function receives as input the document submitted for evaluation and returns its translation into French
def get_french_translation(initial_document):
    french_translation = translator.translate(initial_document, dest='fr', src='en')
    return french_translation.text


# the function receives as input the document submitted for evaluation and returns its translation into German
def get_german_translation(initial_document):
    german_translation = translator.translate(initial_document, dest='de', src='en')
    return german_translation.text


# the function receives as input the document submitted for evaluation and returns its translation into Italian
def get_italian_translation(initial_document):
    italian_translation = translator.translate(initial_document, dest='it', src='en')
    return italian_translation.text


# the function receives as input the document submitted for evaluation and returns its translation into Polish
def get_polish_translation(initial_document):
    polish_translation = translator.translate(initial_document, dest='pl', src='en')
    return polish_translation.text


# the function receives as input the document submitted for evaluation and returns its translation into Portuguese
def get_portuguese_translation(initial_document):
    portuguese_translation = translator.translate(initial_document, dest='pt', src='en')
    return portuguese_translation.text


# the function receives as input the document submitted for evaluation and returns its translation into Romanian
def get_romanian_translation(initial_document):
    romanian_translation = translator.translate(initial_document, dest='ro', src='en')
    return romanian_translation.text


# the function receives as input the document submitted for evaluation and returns its translation into Spanish
def get_spanish_translation(initial_document):
    spanish_translation = translator.translate(initial_document, dest='es', src='en')
    return spanish_translation.text


# the function receives as input the document submitted for evaluation and returns its translation into Swedish
def get_swedish_translation(initial_document):
    swedish_translation = translator.translate(initial_document, dest='sv', src='en')
    return swedish_translation.text


# helper function used for converting the contents of a list into a string
def convert_list_to_string(target_list):
    string = ' '.join(target_list)
    return string


# the function aggregates the search phrase for each language into a Python list
# noinspection PyTypeChecker
def get_keyword_search_terms_array(keywords):
    search_array = []
    for language_keywords in keywords:
        search_array.append(convert_list_to_string(language_keywords))

    return [search_array[Language.DUTCH.value], search_array[Language.FRENCH.value],
            search_array[Language.GERMAN.value], search_array[Language.ITALIAN.value],
            search_array[Language.POLISH.value], search_array[Language.PORTUGUESE.value],
            search_array[Language.ROMANIAN.value], search_array[Language.SPANISH.value],
            search_array[Language.SWEDISH.value]]


# the function aggregates the keywords lists into a Python list
def get_keywords_array(translations):
    return [get_dutch_keywords(translations[Language.DUTCH.value]),
            get_french_keywords(translations[Language.FRENCH.value]),
            get_german_keywords(translations[Language.GERMAN.value]),
            get_italian_keywords(translations[Language.ITALIAN.value]),
            get_polish_keywords(translations[Language.POLISH.value]),
            get_portuguese_keywords(translations[Language.PORTUGUESE.value]),
            get_romanian_keywords(translations[Language.ROMANIAN.value]),
            get_spanish_keywords(translations[Language.SPANISH.value]),
            get_swedish_keywords(translations[Language.SWEDISH.value])]


# the function receives as input the Dutch translation of the document submitted for evaluation and returns the keywords
# of the translation
def get_dutch_keywords(dutch_translation):
    # the parameters of the KeywordExtractor are:
    # lan: language, in this case "nl" which is short for Dutch
    # top: the first n, in this case 3, most relevant keyword phrases to be returned
    # dedupLim: how much duplication is allowed between the keywords
    # n: the maximum number of words allowed in the keyword phrases
    dutch_keyword_extractor = yake.KeywordExtractor(lan="nl", top=3, dedupLim=0.20, n=2)
    keywords = dutch_keyword_extractor.extract_keywords(dutch_translation)

    # collecting all the keywords into a single list
    dutch_keyword_list = []
    for keyword in keywords:
        dutch_keyword_list.append(keyword[0])

    return dutch_keyword_list


# the function receives as input the French translation of the document submitted for evaluation and returns the keywords
# of the translation
def get_french_keywords(french_translation):
    french_keyword_extractor = yake.KeywordExtractor(lan="fr", top=3, dedupLim=0.20, n=2)
    keywords = french_keyword_extractor.extract_keywords(french_translation)

    french_keyword_list = []
    for keyword in keywords:
        french_keyword_list.append(keyword[0])

    return french_keyword_list


# the function receives as input the German translation of the document submitted for evaluation and returns the
# keywords of the translation
def get_german_keywords(german_translation):
    german_keyword_extractor = yake.KeywordExtractor(lan="de", top=3, dedupLim=0.20, n=2)
    keywords = german_keyword_extractor.extract_keywords(german_translation)

    german_keyword_list = []
    for keyword in keywords:
        german_keyword_list.append(keyword[0])

    return german_keyword_list


# the function receives as input the Italian translation of the document submitted for evaluation and returns the keywords
# of the translation
def get_italian_keywords(italian_translation):
    italian_keyword_extractor = yake.KeywordExtractor(lan="it", top=3, dedupLim=0.20, n=2)
    keywords = italian_keyword_extractor.extract_keywords(italian_translation)

    italian_keyword_list = []
    for keyword in keywords:
        italian_keyword_list.append(keyword[0])

    return italian_keyword_list


# the function receives as input the Polish translation of the document submitted for evaluation and returns the keywords
# of the translation
def get_polish_keywords(polish_translation):
    polish_keyword_extractor = yake.KeywordExtractor(lan="fr", top=3, dedupLim=0.20, n=2)
    keywords = polish_keyword_extractor.extract_keywords(polish_translation)

    polish_keyword_list = []
    for keyword in keywords:
        polish_keyword_list.append(keyword[0])
    return polish_keyword_list


# the function receives as input the Portuguese translation of the document submitted for evaluation and returns the keywords
# of the translation
def get_portuguese_keywords(portuguese_translation):
    portuguese_keyword_extractor = yake.KeywordExtractor(lan="pl", top=3, dedupLim=0.20, n=2)
    keywords = portuguese_keyword_extractor.extract_keywords(portuguese_translation)

    portuguese_keyword_list = []
    for keyword in keywords:
        portuguese_keyword_list.append(keyword[0])
    return portuguese_keyword_list


# the function receives as input the Romanian translation of the document submitted for evaluation and returns the keywords
# of the translation
def get_romanian_keywords(romanian_translation):
    romanian_keyword_extractor = yake.KeywordExtractor(lan="ro", top=3, dedupLim=0.20, n=2)
    keywords = romanian_keyword_extractor.extract_keywords(romanian_translation)

    romanian_keyword_list = []
    for keyword in keywords:
        romanian_keyword_list.append(keyword[0])

    return romanian_keyword_list


# the function receives as input the Spanish translation of the document submitted for evaluation and returns the keywords
# of the translation
def get_spanish_keywords(spanish_translation):
    spanish_keyword_extractor = yake.KeywordExtractor(lan="es", top=3, dedupLim=0.20, n=2)
    keywords = spanish_keyword_extractor.extract_keywords(spanish_translation)

    spanish_keyword_list = []
    for keyword in keywords:
        spanish_keyword_list.append(keyword[0])

    return spanish_keyword_list


# the function receives as input the Swedish translation of the document submitted for evaluation and returns the keywords
# of the translation
def get_swedish_keywords(swedish_translation):
    swedish_keyword_extractor = yake.KeywordExtractor(lan="sv", top=3, dedupLim=0.20, n=2)
    keywords = swedish_keyword_extractor.extract_keywords(swedish_translation)

    sweden_keyword_list = []
    for keyword in keywords:
        sweden_keyword_list.append(keyword[0])

    return sweden_keyword_list


# function used for returning the list of urls associated with a given search phrase
def get_urls_from_keyword_search_term(keyword_search_term, language):
    url_list = []

    # the search function is part of the googlesearch module; it returns the first num_results urls associated to a given
    # term in a given lang (language)
    for url in search(term=keyword_search_term, lang=language, num_results=3):
        url_list.append(url)

    return url_list


# the function receives as input the search phrase for Dutch and returns the first 6 urls computed by the Google search
# engine when searching the given search phrase
def get_dutch_urls(keyword_search_term):
    language = "nl"
    return get_urls_from_keyword_search_term(keyword_search_term, language)


# the function receives as input the search phrase for French and returns the first 6 urls computed by the Google search
# engine when searching the given search phrase
def get_french_urls(keyword_search_term):
    language = "fr"
    return get_urls_from_keyword_search_term(keyword_search_term, language)


# the function receives as input the search phrase for German and returns the first 6 urls computed by the Google search
# engine when searching the given search phrase
def get_german_urls(keyword_search_term):
    language = "de"
    return get_urls_from_keyword_search_term(keyword_search_term, language)


# the function receives as input the search phrase for Italian and returns the first 6 urls computed by the Google search
# engine when searching the given search phrase
def get_italian_urls(keyword_search_term):
    language = "it"
    return get_urls_from_keyword_search_term(keyword_search_term, language)


# the function receives as input the search phrase for Polish and returns the first 6 urls computed by the Google search
# engine when searching the given search phrase
def get_polish_urls(keyword_search_term):
    language = "pl"
    return get_urls_from_keyword_search_term(keyword_search_term, language)


# the function receives as input the search phrase for Portuguese and returns the first 6 urls computed by the Google search
# engine when searching the given search phrase
def get_portuguese_urls(keyword_search_term):
    language = "pt"
    return get_urls_from_keyword_search_term(keyword_search_term, language)


# the function receives as input the search phrase for Romanian and returns the first 6 urls computed by the Google search
# engine when searching the given search phrase
def get_romanian_urls(keyword_search_term):
    language = "ro"
    return get_urls_from_keyword_search_term(keyword_search_term, language)


# the function receives as input the search phrase for Spanish and returns the first 6 urls computed by the Google search
# engine when searching the given search phrase
def get_spanish_urls(keyword_search_term):
    language = "es"
    return get_urls_from_keyword_search_term(keyword_search_term, language)


# the function receives as input the search phrase for Swedish and returns the first 6 urls computed by the Google search
# engine when searching the given search phrase
def get_swedish_urls(keyword_search_term):
    language = "sv"
    return get_urls_from_keyword_search_term(keyword_search_term, language)


# the function takes as input a list of urls and returns the a list of htmls associated with the given urls
def get_html_from_urls(urls):
    htmls_list = []

    # loop through the urls
    for url in urls:
        try:
            # make a http get request from the url
            response = requests.get(url)
        # catch connection related exceptions
        except requests.exceptions.ConnectionError:
            response = "Connection error"

        # append the html content of the response to the list to be returned
        if type(response) != str:
            htmls_list.append(response.content)

    return htmls_list


# function used for removing the html related content of the webpage in order to obtain only the visible text parts
def get_texts_from_htmls(htmls):
    texts = []

    # loop through the htmls
    for html in htmls:
        # create a parser using the BeautifulSoup module with the lxml features
        parser = BeautifulSoup(html, "lxml")

        # search for script or style tags and remove them completely
        for removable_elements in parser(["script", "style"]):
            removable_elements.extract()

        # get the visible text
        text = parser.get_text(separator=" ", strip=True)

        # remove occurrences of non-breaking character '\xa0' which appears often
        text = text.replace(u'\xa0', u' ')

        # split the text into lines and remove leading and trailing white spaces on each line
        lines = (line.strip() for line in text.splitlines())

        # break multi-headlines into a line each
        bits = (phrase.strip() for line in lines for phrase in line.split("  "))

        # join all the chunks into a single text which is added to the list of texts to be returned
        texts.append(''.join(chunk for chunk in bits if chunk))

    return texts


# the function aggregates the urls associated to each search phrase into a Python list
def get_array_of_urls(keyword_search_terms):
    return [get_dutch_urls(keyword_search_terms[Language.DUTCH.value]),
            get_french_urls(keyword_search_terms[Language.FRENCH.value]),
            get_german_urls(keyword_search_terms[Language.GERMAN.value]),
            get_italian_urls(keyword_search_terms[Language.ITALIAN.value]),
            get_polish_urls(keyword_search_terms[Language.POLISH.value]),
            get_portuguese_urls(keyword_search_terms[Language.PORTUGUESE.value]),
            get_romanian_urls(keyword_search_terms[Language.ROMANIAN.value]),
            get_spanish_urls(keyword_search_terms[Language.SPANISH.value]),
            get_swedish_urls(keyword_search_terms[Language.SWEDISH.value])]


# the function aggregates the htmls associated with the urls into a Python list
def get_array_of_htmls(urls):
    return [get_html_from_urls(urls[Language.DUTCH.value]),
            get_html_from_urls(urls[Language.FRENCH.value]),
            get_html_from_urls(urls[Language.GERMAN.value]),
            get_html_from_urls(urls[Language.ITALIAN.value]),
            get_html_from_urls(urls[Language.POLISH.value]),
            get_html_from_urls(urls[Language.PORTUGUESE.value]),
            get_html_from_urls(urls[Language.ROMANIAN.value]),
            get_html_from_urls(urls[Language.SPANISH.value]),
            get_html_from_urls(urls[Language.SWEDISH.value])]


# the function aggregates the texts associated with each html into a Python list
def get_array_of_texts(htmls):
    return [get_texts_from_htmls(htmls[Language.DUTCH.value]), get_texts_from_htmls(htmls[Language.FRENCH.value]),
            get_texts_from_htmls(htmls[Language.GERMAN.value]), get_texts_from_htmls(htmls[Language.ITALIAN.value]),
            get_texts_from_htmls(htmls[Language.POLISH.value]), get_texts_from_htmls(htmls[Language.PORTUGUESE.value]),
            get_texts_from_htmls(htmls[Language.ROMANIAN.value]), get_texts_from_htmls(htmls[Language.SPANISH.value]),
            get_texts_from_htmls(htmls[Language.SWEDISH.value])]


def split_text_into_chunks(text, character_count):
    return [text[i:i + character_count] for i in range(0, len(text), character_count)]


def get_array_of_text_chunks(language_texts, character_count):
    chunks_array = []

    for language_text in language_texts:
        chunks_array.append(split_text_into_chunks(language_text, character_count))

    return chunks_array


def get_list_to_be_vectorized(translated_text, language_text_chunk):
    list_to_be_vectorized = [translated_text]

    for chunk in language_text_chunk:
        list_to_be_vectorized.append(chunk)

    return list_to_be_vectorized


def create_cosine_similarity_matrix(list_to_be_vectorized, language_stop_words):
    tf_idf_vectorizer = TfidfVectorizer(stop_words=language_stop_words)

    term_matrix = tf_idf_vectorizer.fit_transform(list_to_be_vectorized)

    cosine_similarity_matrix = cosine_similarity(term_matrix, term_matrix)

    return cosine_similarity_matrix


start_time = time.time()

dutch_stop_words = ["aan", "achte", "achter", "af", "al", "alle", "alleen", "alles", "als", "ander", "anders", "beetje",
                    "behalve", "beide", "beiden", "ben", "beneden", "bent", "bij", "bijna", "bijv", "blijkbaar",
                    "blijken", "boven", "bv", "daar", "daardoor", "daarin", "daarna", "daarom", "daaruit", "dan", "dat",
                    "de", "deden", "deed", "derde", "derhalve", "dertig", "deze", "dhr", "die", "dit", "doe", "doen",
                    "doet", "door", "drie", "duizend", "echter", "een", "eens", "eerst", "eerste", "eigen", "eigenlijk",
                    "elk", "elke", "en", "enige", "er", "erg", "ergens", "etc", "etcetera", "even", "geen", "genoeg",
                    "geweest", "haar", "haarzelf", "had", "hadden", "heb", "hebben", "hebt", "hedden", "heeft", "heel",
                    "hem", "hemzelf", "hen", "het", "hetzelfde", "hier", "hierin", "hierna", "hierom", "hij", "hijzelf",
                    "hoe", "honderd", "hun", "ieder", "iedere", "iedereen", "iemand", "iets", "ik", "in", "inderdaad",
                    "intussen", "is", "ja", "je", "jij", "jijzelf", "jou", "jouw", "jullie", "kan", "kon", "konden",
                    "kun", "kunnen", "kunt", "laatst", "later", "lijken", "lijkt", "maak", "maakt", "maakte", "maakten",
                    "maar", "mag", "maken", "me", "meer", "meest", "meestal", "men", "met", "mevr", "mij", "mijn",
                    "minder", "miss", "misschien", "missen", "mits", "mocht", "mochten", "moest", "moesten", "moet",
                    "moeten", "mogen", "mr", "mrs", "mw", "na", "naar", "nam", "namelijk", "nee", "neem", "negen",
                    "nemen", "nergens", "niemand", "niet", "niets", "niks", "noch", "nochtans", "nog", "nooit", "nu",
                    "nv", "of", "om", "omdat", "ondanks", "onder", "ondertussen", "ons", "onze", "onzeker", "ooit",
                    "ook", "op", "over", "overal", "overige", "paar", "per", "recent", "redelijk", "samen", "sinds",
                    "steeds", "te", "tegen", "tegenover", "thans", "tien", "tiende", "tijdens", "tja", "toch", "toe",
                    "tot", "totdat", "tussen", "twee", "tweede", "u", "uit", "uw", "vaak", "van", "vanaf", "veel",
                    "veertig", "verder", "verscheidene", "verschillende", "via", "vier", "vierde", "vijf", "vijfde",
                    "vijftig", "volgend", "volgens", "voor", "voordat", "voorts", "waar", "waarom", "waarschijnlijk",
                    "wanneer", "waren", "was", "wat", "we", "wederom", "weer", "weinig", "wel", "welk", "welke", "werd",
                    "werden", "werder", "whatever", "wie", "wij", "wijzelf", "wil", "wilden", "willen", "word",
                    "worden", "wordt", "zal", "ze", "zei", "zeker", "zelf", "zelfde", "zes", "zeven", "zich", "zij",
                    "zijn", "zijzelf", "zo", "zoals", "zodat", "zou", "zouden", "zulk", "zullen"]
french_stop_words = ["a", "abord", "absolument", "afin", "ah", "ai", "aie", "ailleurs", "ainsi", "ait", "allaient",
                     "allo", "allons", "allô", "alors", "anterieur", "anterieure", "anterieures", "apres", "après",
                     "as", "assez", "attendu", "au", "aucun", "aucune", "aujourd", "aujourd'hui", "aupres", "auquel",
                     "aura", "auraient", "aurait", "auront", "aussi", "autre", "autrefois", "autrement", "autres",
                     "autrui", "aux", "auxquelles", "auxquels", "avaient", "avais", "avait", "avant", "avec", "avoir",
                     "avons", "ayant", "b", "bah", "bas", "basee", "bat", "beau", "beaucoup", "bien", "bigre", "boum",
                     "bravo", "brrr", "c", "car", "ce", "ceci", "cela", "celle", "celle-ci", "celle-là", "celles",
                     "celles-ci", "celles-là", "celui", "celui-ci", "celui-là", "cent", "cependant", "certain",
                     "certaine", "certaines", "certains", "certes", "ces", "cet", "cette", "ceux", "ceux-ci", "ceux-là",
                     "chacun", "chacune", "chaque", "cher", "chers", "chez", "chiche", "chut", "chère", "chères", "ci",
                     "cinq", "cinquantaine", "cinquante", "cinquantième", "cinquième", "clac", "clic", "combien",
                     "comme", "comment", "comparable", "comparables", "compris", "concernant", "contre", "couic",
                     "crac", "d", "da", "dans", "de", "debout", "dedans", "dehors", "deja", "delà", "depuis", "dernier",
                     "derniere", "derriere", "derrière", "des", "desormais", "desquelles", "desquels", "dessous",
                     "dessus", "deux", "deuxième", "deuxièmement", "devant", "devers", "devra", "different",
                     "differentes", "differents", "différent", "différente", "différentes", "différents", "dire",
                     "directe", "directement", "dit", "dite", "dits", "divers", "diverse", "diverses", "dix",
                     "dix-huit", "dix-neuf", "dix-sept", "dixième", "doit", "doivent", "donc", "dont", "douze",
                     "douzième", "dring", "du", "duquel", "durant", "dès", "désormais", "e", "effet", "egale",
                     "egalement", "egales", "eh", "elle", "elle-même", "elles", "elles-mêmes", "en", "encore", "enfin",
                     "entre", "envers", "environ", "es", "est", "et", "etant", "etc", "etre", "eu", "euh", "eux",
                     "eux-mêmes", "exactement", "excepté", "extenso", "exterieur", "f", "fais", "faisaient", "faisant",
                     "fait", "façon", "feront", "fi", "flac", "floc", "font", "g", "gens", "h", "ha", "hein", "hem",
                     "hep", "hi", "ho", "holà", "hop", "hormis", "hors", "hou", "houp", "hue", "hui", "huit",
                     "huitième", "hum", "hurrah", "hé", "hélas", "i", "il", "ils", "importe", "j", "je", "jusqu",
                     "jusque", "juste", "k", "l", "la", "laisser", "laquelle", "las", "le", "lequel", "les",
                     "lesquelles", "lesquels", "leur", "leurs", "longtemps", "lors", "lorsque", "lui", "lui-meme",
                     "lui-même", "là", "lès", "m", "ma", "maint", "maintenant", "mais", "malgre", "malgré", "maximale",
                     "me", "meme", "memes", "merci", "mes", "mien", "mienne", "miennes", "miens", "mille", "mince",
                     "minimale", "moi", "moi-meme", "moi-même", "moindres", "moins", "mon", "moyennant", "multiple",
                     "multiples", "même", "mêmes", "n", "na", "naturel", "naturelle", "naturelles", "ne", "neanmoins",
                     "necessaire", "necessairement", "neuf", "neuvième", "ni", "nombreuses", "nombreux", "non", "nos",
                     "notamment", "notre", "nous", "nous-mêmes", "nouveau", "nul", "néanmoins", "nôtre", "nôtres", "o",
                     "oh", "ohé", "ollé", "olé", "on", "ont", "onze", "onzième", "ore", "ou", "ouf", "ouias", "oust",
                     "ouste", "outre", "ouvert", "ouverte", "ouverts", "o|", "où", "p", "paf", "pan", "par", "parce",
                     "parfois", "parle", "parlent", "parler", "parmi", "parseme", "partant", "particulier",
                     "particulière", "particulièrement", "pas", "passé", "pendant", "pense", "permet", "personne",
                     "peu", "peut", "peuvent", "peux", "pff", "pfft", "pfut", "pif", "pire", "plein", "plouf", "plus",
                     "plusieurs", "plutôt", "possessif", "possessifs", "possible", "possibles", "pouah", "pour",
                     "pourquoi", "pourrais", "pourrait", "pouvait", "prealable", "precisement", "premier", "première",
                     "premièrement", "pres", "probable", "probante", "procedant", "proche", "près", "psitt", "pu",
                     "puis", "puisque", "pur", "pure", "q", "qu", "quand", "quant", "quant-à-soi", "quanta", "quarante",
                     "quatorze", "quatre", "quatre-vingt", "quatrième", "quatrièmement", "que", "quel", "quelconque",
                     "quelle", "quelles", "quelqu", "quelque", "quelques", "quels", "qui", "quiconque", "quinze",
                     "quoi", "quoique", "r", "rare", "rarement", "rares", "relative", "relativement", "remarquable",
                     "rend", "rendre", "restant", "reste", "restent", "restrictif", "retour", "revoici", "revoilà",
                     "rien", "s", "sa", "sacrebleu", "sait", "sans", "sapristi", "sauf", "se", "sein", "seize", "selon",
                     "semblable", "semblaient", "semble", "semblent", "sent", "sept", "septième", "sera", "seraient",
                     "serait", "seront", "ses", "seul", "seule", "seulement", "si", "sien", "sienne", "siennes",
                     "siens", "sinon", "six", "sixième", "soi", "soi-même", "soit", "soixante", "son", "sont", "sous",
                     "souvent", "specifique", "specifiques", "speculatif", "stop", "strictement", "subtiles",
                     "suffisant", "suffisante", "suffit", "suis", "suit", "suivant", "suivante", "suivantes",
                     "suivants", "suivre", "superpose", "sur", "surtout", "t", "ta", "tac", "tant", "tardive", "te",
                     "tel", "telle", "tellement", "telles", "tels", "tenant", "tend", "tenir", "tente", "tes", "tic",
                     "tien", "tienne", "tiennes", "tiens", "toc", "toi", "toi-même", "ton", "touchant", "toujours",
                     "tous", "tout", "toute", "toutefois", "toutes", "treize", "trente", "tres", "trois", "troisième",
                     "troisièmement", "trop", "très", "tsoin", "tsouin", "tu", "té", "u", "un", "une", "unes",
                     "uniformement", "unique", "uniques", "uns", "v", "va", "vais", "vas", "vers", "via", "vif", "vifs",
                     "vingt", "vivat", "vive", "vives", "vlan", "voici", "voilà", "vont", "vos", "votre", "vous",
                     "vous-mêmes", "vu", "vé", "vôtre", "vôtres", "w", "x", "y", "z", "zut", "à", "â", "ça", "ès",
                     "étaient", "étais", "était", "étant", "été", "être", "ô"]
german_stop_words = ["a", "ab", "aber", "ach", "acht", "achte", "achten", "achter",
                     "achtes", "ag", "alle", "allein", "allem", "allen", "aller", "allerdings", "alles", "allgemeinen",
                     "als", "also", "am", "an", "andere", "anderen", "andern", "anders", "au", "auch", "auf", "aus",
                     "ausser", "ausserdem", "außer", "außerdem", "b", "bald", "bei", "beide", "beiden", "beim",
                     "beispiel", "bekannt", "bereits", "besonders", "besser", "besten", "bin", "bis", "bisher", "bist",
                     "c", "d", "d.h", "da", "dabei", "dadurch", "dafür", "dagegen", "daher", "dahin", "dahinter",
                     "damals", "damit", "danach", "daneben", "dank", "dann", "daran", "darauf", "daraus", "darf",
                     "darfst", "darin", "darum", "darunter", "darüber", "das", "dasein", "daselbst", "dass", "dasselbe",
                     "davon", "davor", "dazu", "dazwischen", "daß", "dein", "deine", "deinem", "deiner", "dem",
                     "dementsprechend", "demgegenüber", "demgemäss", "demgemäß", "demselben", "demzufolge", "den",
                     "denen", "denn", "denselben", "der", "deren", "derjenige", "derjenigen", "dermassen", "dermaßen",
                     "derselbe", "derselben", "des", "deshalb", "desselben", "dessen", "deswegen", "dich", "die",
                     "diejenige", "diejenigen", "dies", "diese", "dieselbe", "dieselben", "diesem", "diesen", "dieser",
                     "dieses", "dir", "doch", "dort", "drei", "drin", "dritte", "dritten", "dritter", "drittes", "du",
                     "durch", "durchaus", "durfte", "durften", "dürfen", "dürft", "e", "eben", "ebenso", "ehrlich",
                     "ei", "ei,", "eigen", "eigene", "eigenen", "eigener", "eigenes", "ein", "einander", "eine",
                     "einem", "einen", "einer", "eines", "einige", "einigen", "einiger", "einiges", "einmal", "eins",
                     "elf", "en", "ende", "endlich", "entweder", "er", "erst", "erste", "ersten", "erster", "erstes",
                     "es", "etwa", "etwas", "euch", "euer", "eure", "f", "folgende", "früher", "fünf", "fünfte",
                     "fünften", "fünfter", "fünftes", "für", "g", "gab", "ganz", "ganze", "ganzen", "ganzer", "ganzes",
                     "gar", "gedurft", "gegen", "gegenüber", "gehabt", "gehen", "geht", "gekannt", "gekonnt", "gemacht",
                     "gemocht", "gemusst", "genug", "gerade", "gern", "gesagt", "geschweige", "gewesen", "gewollt",
                     "geworden", "gibt", "ging", "gleich", "gott", "gross", "grosse", "grossen", "grosser", "grosses",
                     "groß", "große", "großen", "großer", "großes", "gut", "gute", "guter", "gutes", "h", "habe",
                     "haben", "habt", "hast", "hat", "hatte", "hatten", "hattest", "hattet", "heisst", "her", "heute",
                     "hier", "hin", "hinter", "hoch", "hätte", "hätten", "i", "ich", "ihm", "ihn", "ihnen", "ihr",
                     "ihre", "ihrem", "ihren", "ihrer", "ihres", "im", "immer", "in", "indem", "infolgedessen", "ins",
                     "irgend", "ist", "j", "ja", "jahr", "jahre", "jahren", "je", "jede", "jedem", "jeden", "jeder",
                     "jedermann", "jedermanns", "jedes", "jedoch", "jemand", "jemandem", "jemanden", "jene", "jenem",
                     "jenen", "jener", "jenes", "jetzt", "k", "kam", "kann", "kannst", "kaum", "kein", "keine",
                     "keinem", "keinen", "keiner", "kleine", "kleinen", "kleiner", "kleines", "kommen", "kommt",
                     "konnte", "konnten", "kurz", "können", "könnt", "könnte", "l", "lang", "lange", "leicht", "leide",
                     "lieber", "los", "m", "machen", "macht", "machte", "mag", "magst", "mahn", "mal", "man", "manche",
                     "manchem", "manchen", "mancher", "manches", "mann", "mehr", "mein", "meine", "meinem", "meinen",
                     "meiner", "meines", "mensch", "menschen", "mich", "mir", "mit", "mittel", "mochte", "mochten",
                     "morgen", "muss", "musst", "musste", "mussten", "muß", "mußt", "möchte", "mögen", "möglich",
                     "mögt", "müssen", "müsst", "müßt", "n", "na", "nach", "nachdem", "nahm", "natürlich", "neben",
                     "nein", "neue", "neuen", "neun", "neunte", "neunten", "neunter", "neuntes", "nicht", "nichts",
                     "nie", "niemand", "niemandem", "niemanden", "noch", "nun", "nur", "o", "ob", "oben", "oder",
                     "offen", "oft", "ohne", "p", "q", "r", "recht", "rechte", "rechten", "rechter", "rechtes",
                     "richtig", "rund", "s", "sa", "sache", "sagt", "sagte", "sah", "satt", "schlecht", "schon",
                     "sechs", "sechste", "sechsten", "sechster", "sechstes", "sehr", "sei", "seid", "seien", "sein",
                     "seine", "seinem", "seinen", "seiner", "seines", "seit", "seitdem", "selbst", "sich", "sie",
                     "sieben", "siebente", "siebenten", "siebenter", "siebentes", "sind", "so", "solang", "solche",
                     "solchem", "solchen", "solcher", "solches", "soll", "sollen", "sollst", "sollt", "sollte",
                     "sollten", "sondern", "sonst", "soweit", "sowie", "später", "startseite", "statt", "steht",
                     "suche", "t", "tag", "tage", "tagen", "tat", "teil", "tel", "tritt", "trotzdem", "tun", "u", "uhr",
                     "um", "und", "und?", "uns", "unser", "unsere", "unserer", "unter", "v", "vergangenen", "viel",
                     "viele", "vielem", "vielen", "vielleicht", "vier", "vierte", "vierten", "vierter", "viertes",
                     "vom", "von", "vor", "w", "wahr", "wann", "war", "waren", "wart", "warum", "was", "wegen", "weil",
                     "weit", "weiter", "weitere", "weiteren", "weiteres", "welche", "welchem", "welchen", "welcher",
                     "welches", "wem", "wen", "wenig", "wenige", "weniger", "weniges", "wenigstens", "wenn", "wer",
                     "werde", "werden", "werdet", "weshalb", "wessen", "wie", "wieder", "wieso", "will", "willst",
                     "wir", "wird", "wirklich", "wirst", "wissen", "wo", "wohl", "wollen", "wollt", "wollte", "wollten",
                     "worden", "wurde", "wurden", "während", "währenddem", "währenddessen", "wäre", "würde", "würden",
                     "x", "y", "z", "z.b", "zehn", "zehnte", "zehnten", "zehnter", "zehntes", "zeit", "zu", "zuerst",
                     "zugleich", "zum", "zunächst", "zur", "zurück", "zusammen", "zwanzig", "zwar", "zwei", "zweite",
                     "zweiten", "zweiter", "zweites", "zwischen", "zwölf", "über", "überhaupt", "übrigens"]
italian_stop_words = ["a", "abbastanza", "abbia", "abbiamo", "abbiano", "abbiate", "accidenti", "ad", "adesso",
                      "affinche", "agl", "agli", "ahime", "ahimè", "ai", "al", "alcuna", "alcuni", "alcuno", "all",
                      "alla", "alle", "allo", "allora", "altri", "altrimenti", "altro", "altrove", "altrui", "anche",
                      "ancora", "anni", "anno", "ansa", "anticipo", "assai", "attesa", "attraverso", "avanti", "avemmo",
                      "avendo", "avente", "aver", "avere", "averlo", "avesse", "avessero", "avessi", "avessimo",
                      "aveste", "avesti", "avete", "aveva", "avevamo", "avevano", "avevate", "avevi", "avevo", "avrai",
                      "avranno", "avrebbe", "avrebbero", "avrei", "avremmo", "avremo", "avreste", "avresti", "avrete",
                      "avrà", "avrò", "avuta", "avute", "avuti", "avuto", "basta", "bene", "benissimo", "berlusconi",
                      "brava", "bravo", "c", "casa", "caso", "cento", "certa", "certe", "certi", "certo", "che", "chi",
                      "chicchessia", "chiunque", "ci", "ciascuna", "ciascuno", "cima", "cio", "cioe", "cioè", "circa",
                      "citta", "città", "ciò", "co", "codesta", "codesti", "codesto", "cogli", "coi", "col", "colei",
                      "coll", "coloro", "colui", "come", "cominci", "comunque", "con", "concernente", "conciliarsi",
                      "conclusione", "consiglio", "contro", "cortesia", "cos", "cosa", "cosi", "così", "cui", "d", "da",
                      "dagl", "dagli", "dai", "dal", "dall", "dalla", "dalle", "dallo", "dappertutto", "davanti",
                      "degl", "degli", "dei", "del", "dell", "della", "delle", "dello", "dentro", "detto", "deve", "di",
                      "dice", "dietro", "dire", "dirimpetto", "diventa", "diventare", "diventato", "dopo", "dov",
                      "dove", "dovra", "dovrà", "dovunque", "due", "dunque", "durante", "e", "ebbe", "ebbero", "ebbi",
                      "ecc", "ecco", "ed", "effettivamente", "egli", "ella", "entrambi", "eppure", "era", "erano",
                      "eravamo", "eravate", "eri", "ero", "esempio", "esse", "essendo", "esser", "essere", "essi", "ex",
                      "fa", "faccia", "facciamo", "facciano", "facciate", "faccio", "facemmo", "facendo", "facesse",
                      "facessero", "facessi", "facessimo", "faceste", "facesti", "faceva", "facevamo", "facevano",
                      "facevate", "facevi", "facevo", "fai", "fanno", "farai", "faranno", "fare", "farebbe",
                      "farebbero", "farei", "faremmo", "faremo", "fareste", "faresti", "farete", "farà", "farò",
                      "fatto", "favore", "fece", "fecero", "feci", "fin", "finalmente", "finche", "fine", "fino",
                      "forse", "forza", "fosse", "fossero", "fossi", "fossimo", "foste", "fosti", "fra", "frattempo",
                      "fu", "fui", "fummo", "fuori", "furono", "futuro", "generale", "gia", "giacche", "giorni",
                      "giorno", "già", "gli", "gliela", "gliele", "glieli", "glielo", "gliene", "governo", "grande",
                      "grazie", "gruppo", "ha", "haha", "hai", "hanno", "ho", "i", "ieri", "il", "improvviso", "in",
                      "inc", "infatti", "inoltre", "insieme", "intanto", "intorno", "invece", "io", "l", "la",
                      "lasciato", "lato", "lavoro", "le", "lei", "li", "lo", "lontano", "loro", "lui", "lungo", "luogo",
                      "là", "ma", "macche", "magari", "maggior", "mai", "male", "malgrado", "malissimo", "mancanza",
                      "marche", "me", "medesimo", "mediante", "meglio", "meno", "mentre", "mesi", "mezzo", "mi", "mia",
                      "mie", "miei", "mila", "miliardi", "milioni", "minimi", "ministro", "mio", "modo", "molti",
                      "moltissimo", "molto", "momento", "mondo", "mosto", "nazionale", "ne", "negl", "negli", "nei",
                      "nel", "nell", "nella", "nelle", "nello", "nemmeno", "neppure", "nessun", "nessuna", "nessuno",
                      "niente", "no", "noi", "non", "nondimeno", "nonostante", "nonsia", "nostra", "nostre", "nostri",
                      "nostro", "novanta", "nove", "nulla", "nuovo", "o", "od", "oggi", "ogni", "ognuna", "ognuno",
                      "oltre", "oppure", "ora", "ore", "osi", "ossia", "ottanta", "otto", "paese", "parecchi",
                      "parecchie", "parecchio", "parte", "partendo", "peccato", "peggio", "per", "perche", "perchè",
                      "perché", "percio", "perciò", "perfino", "pero", "persino", "persone", "però", "piedi", "pieno",
                      "piglia", "piu", "piuttosto", "più", "po", "pochissimo", "poco", "poi", "poiche", "possa",
                      "possedere", "posteriore", "posto", "potrebbe", "preferibilmente", "presa", "press", "prima",
                      "primo", "principalmente", "probabilmente", "proprio", "puo", "pure", "purtroppo", "può",
                      "qualche", "qualcosa", "qualcuna", "qualcuno", "quale", "quali", "qualunque", "quando", "quanta",
                      "quante", "quanti", "quanto", "quantunque", "quasi", "quattro", "quel", "quella", "quelle",
                      "quelli", "quello", "quest", "questa", "queste", "questi", "questo", "qui", "quindi", "realmente",
                      "recente", "recentemente", "registrazione", "relativo", "riecco", "salvo", "sara", "sarai",
                      "saranno", "sarebbe", "sarebbero", "sarei", "saremmo", "saremo", "sareste", "saresti", "sarete",
                      "sarà", "sarò", "scola", "scopo", "scorso", "se", "secondo", "seguente", "seguito", "sei",
                      "sembra", "sembrare", "sembrato", "sembri", "sempre", "senza", "sette", "si", "sia", "siamo",
                      "siano", "siate", "siete", "sig", "solito", "solo", "soltanto", "sono", "sopra", "sotto",
                      "spesso", "srl", "sta", "stai", "stando", "stanno", "starai", "staranno", "starebbe",
                      "starebbero", "starei", "staremmo", "staremo", "stareste", "staresti", "starete", "starà",
                      "starò", "stata", "state", "stati", "stato", "stava", "stavamo", "stavano", "stavate", "stavi",
                      "stavo", "stemmo", "stessa", "stesse", "stessero", "stessi", "stessimo", "stesso", "steste",
                      "stesti", "stette", "stettero", "stetti", "stia", "stiamo", "stiano", "stiate", "sto", "su",
                      "sua", "subito", "successivamente", "successivo", "sue", "sugl", "sugli", "sui", "sul", "sull",
                      "sulla", "sulle", "sullo", "suo", "suoi", "tale", "tali", "talvolta", "tanto", "te", "tempo",
                      "ti", "titolo", "torino", "tra", "tranne", "tre", "trenta", "troppo", "trovato", "tu", "tua",
                      "tue", "tuo", "tuoi", "tutta", "tuttavia", "tutte", "tutti", "tutto", "uguali", "ulteriore",
                      "ultimo", "un", "una", "uno", "uomo", "va", "vale", "vari", "varia", "varie", "vario", "verso",
                      "vi", "via", "vicino", "visto", "vita", "voi", "volta", "volte", "vostra", "vostre", "vostri",
                      "vostro", "è"]
polish_stop_words = ["aby", "ach", "aj", "albo", "ale", "ani", "aż", "bardzo", "bez", "bo", "bowiem", "by", "byli",
                     "bym", "być", "był", "była", "było", "były", "będzie", "będą", "chce", "choć", "ci", "ciebie",
                     "cię", "co", "coraz", "coś", "czy", "czyli", "często", "daleko", "dla", "dlaczego", "dlatego",
                     "do", "dobrze", "dokąd", "dość", "dr", "dużo", "dwa", "dwaj", "dwie", "dwoje", "dzisiaj", "dziś",
                     "gdy", "gdyby", "gdyż", "gdzie", "go", "godz", "hab", "i", "ich", "ii", "iii", "ile", "im", "inne",
                     "inny", "inż", "iv", "ix", "iż", "ja", "jak", "jakby", "jaki", "jakie", "jako", "je", "jeden",
                     "jedna", "jednak", "jedno", "jednym", "jedynie", "jego", "jej", "jemu", "jest", "jestem",
                     "jeszcze", "jeśli", "jeżeli", "już", "ją", "każdy", "kiedy", "kierunku", "kilku", "kto", "która",
                     "które", "którego", "której", "który", "których", "którym", "którzy", "ku", "lat", "lecz", "lub",
                     "ma", "mają", "mam", "mamy", "mgr", "mi", "miał", "mimo", "mnie", "mną", "mogą", "moi", "moja",
                     "moje", "może", "można", "mu", "musi", "my", "mój", "na", "nad", "nam", "nami", "nas", "nasi",
                     "nasz", "nasza", "nasze", "natychmiast", "nawet", "nic", "nich", "nie", "niego", "niej", "niemu",
                     "nigdy", "nim", "nimi", "nią", "niż", "no", "nowe", "np", "nr", "o", "o.o.", "obok", "od", "ok",
                     "około", "on", "ona", "one", "oni", "ono", "oraz", "owszem", "pan", "pl", "po", "pod", "ponad",
                     "ponieważ", "poza", "prof", "przed", "przede", "przedtem", "przez", "przy", "raz", "razie", "roku",
                     "również", "sam", "sama", "się", "skąd", "sobie", "sposób", "swoje", "są", "ta", "tak", "taki",
                     "takich", "takie", "także", "tam", "te", "tego", "tej", "tel", "temu", "ten", "teraz", "też", "to",
                     "tobie", "tobą", "trzeba", "tu", "tutaj", "twoi", "twoja", "twoje", "twój", "ty", "tych", "tylko",
                     "tym", "tys", "tzw", "tę", "u", "ul", "vi", "vii", "viii", "vol", "w", "wam", "wami", "was",
                     "wasi", "wasz", "wasza", "wasze", "we", "wie", "więc", "wszystko", "wtedy", "www", "wy", "właśnie",
                     "wśród", "xi", "xii", "xiii", "xiv", "xv", "z", "za", "zawsze", "zaś", "ze", "zł", "żaden", "że",
                     "żeby"]
portuguese_stop_words = ["a", "acerca", "adeus", "agora", "ainda", "algmas", "algo", "algumas", "alguns", "ali", "além",
                         "ambos", "ano", "anos", "antes", "ao", "aos", "apenas", "apoio", "apontar", "após", "aquela",
                         "aquelas", "aquele", "aqueles", "aqui", "aquilo", "as", "assim", "através", "atrás", "até",
                         "aí", "baixo", "bastante", "bem", "bom", "breve", "cada", "caminho", "catorze", "cedo",
                         "cento", "certamente", "certeza", "cima", "cinco", "coisa", "com", "como", "comprido",
                         "conhecido", "conselho", "contra", "corrente", "custa", "cá", "da", "daquela", "daquele",
                         "dar", "das", "de", "debaixo", "demais", "dentro", "depois", "desde", "desligado", "dessa",
                         "desse", "desta", "deste", "deve", "devem", "deverá", "dez", "dezanove", "dezasseis",
                         "dezassete", "dezoito", "dia", "diante", "direita", "diz", "dizem", "dizer", "do", "dois",
                         "dos", "doze", "duas", "dá", "dão", "dúvida", "e", "ela", "elas", "ele", "eles", "em",
                         "embora", "enquanto", "entre", "então", "era", "essa", "essas", "esse", "esses", "esta",
                         "estado", "estar", "estará", "estas", "estava", "este", "estes", "esteve", "estive",
                         "estivemos", "estiveram", "estiveste", "estivestes", "estou", "está", "estás", "estão", "eu",
                         "exemplo", "falta", "fará", "favor", "faz", "fazeis", "fazem", "fazemos", "fazer", "fazes",
                         "fazia", "faço", "fez", "fim", "final", "foi", "fomos", "for", "fora", "foram", "forma",
                         "foste", "fostes", "fui", "geral", "grande", "grandes", "grupo", "hoje", "horas", "há",
                         "iniciar", "inicio", "ir", "irá", "isso", "ista", "iste", "isto", "já", "lado", "ligado",
                         "local", "logo", "longe", "lugar", "lá", "maior", "maioria", "maiorias", "mais", "mal", "mas",
                         "me", "meio", "menor", "menos", "meses", "mesmo", "meu", "meus", "mil", "minha", "minhas",
                         "momento", "muito", "muitos", "máximo", "mês", "na", "nada", "naquela", "naquele", "nas",
                         "nem", "nenhuma", "nessa", "nesse", "nesta", "neste", "no", "noite", "nome", "nos", "nossa",
                         "nossas", "nosso", "nossos", "nova", "nove", "novo", "novos", "num", "numa", "nunca", "não",
                         "nível", "nós", "número", "o", "obra", "obrigada", "obrigado", "oitava", "oitavo", "oito",
                         "onde", "ontem", "onze", "os", "ou", "outra", "outras", "outro", "outros", "para", "parece",
                         "parte", "partir", "pegar", "pela", "pelas", "pelo", "pelos", "perto", "pessoas", "pode",
                         "podem", "poder", "poderá", "podia", "ponto", "pontos", "por", "porque", "porquê", "posição",
                         "possivelmente", "posso", "possível", "pouca", "pouco", "povo", "primeira", "primeiro",
                         "promeiro", "próprio", "próximo", "puderam", "pôde", "põe", "põem", "qual", "qualquer",
                         "quando", "quanto", "quarta", "quarto", "quatro", "que", "quem", "quer", "quero", "questão",
                         "quieto", "quinta", "quinto", "quinze", "quê", "relação", "sabe", "saber", "se", "segunda",
                         "segundo", "sei", "seis", "sem", "sempre", "ser", "seria", "sete", "seu", "seus", "sexta",
                         "sexto", "sim", "sistema", "sob", "sobre", "sois", "somente", "somos", "sou", "sua", "suas",
                         "são", "sétima", "sétimo", "tal", "talvez", "também", "tanto", "tarde", "te", "tem", "temos",
                         "tempo", "tendes", "tenho", "tens", "tentar", "tentaram", "tente", "tentei", "ter", "terceira",
                         "terceiro", "teu", "teus", "teve", "tipo", "tive", "tivemos", "tiveram", "tiveste", "tivestes",
                         "toda", "todas", "todo", "todos", "trabalhar", "trabalho", "treze", "três", "tu", "tua",
                         "tuas", "tudo", "tão", "têm", "um", "uma", "umas", "uns", "usa", "usar", "vai", "vais",
                         "valor", "veja", "vem", "vens", "ver", "verdade", "verdadeiro", "vez", "vezes", "viagem",
                         "vindo", "vinte", "você", "vocês", "vos", "vossa", "vossas", "vosso", "vossos", "vários",
                         "vão", "vêm", "vós", "zero", "à", "às", "área", "é", "és", "último"]
romanian_stop_words = ["a", "acea", "aceasta", "această", "aceea", "acei", "aceia", "acel", "acela", "acele", "acelea",
                       "acest", "acesta", "aceste", "acestea", "aceşti", "aceştia", "acolo", "acord", "acum", "ai",
                       "aia", "aibă", "aici", "al", "ale", "alea", "altceva", "altcineva", "am", "ar", "are",
                       "asemenea", "asta", "astea", "astăzi", "asupra", "au", "avea", "avem", "aveţi", "azi", "aş",
                       "aşadar", "aţi", "bine", "bucur", "bună", "ca", "care", "caut", "ce", "cel", "ceva", "chiar",
                       "cinci", "cine", "cineva", "contra", "cu", "cum", "cumva", "curând", "curînd", "când", "cât",
                       "câte", "câtva", "câţi", "cînd", "cît", "cîte", "cîtva", "cîţi", "că", "căci", "cărei", "căror",
                       "cărui", "către", "da", "dacă", "dar", "datorită", "dată", "dau", "de", "deci", "deja",
                       "deoarece", "departe", "deşi", "din", "dinaintea", "dintr", "dintre", "doi", "doilea", "două",
                       "drept", "după", "dă", "ea", "ei", "el", "ele", "eram", "este", "eu", "eşti", "face", "fata",
                       "fi", "fie", "fiecare", "fii", "fim", "fiu", "fiţi", "frumos", "fără", "graţie", "halbă", "iar",
                       "ieri", "la", "le", "li", "lor", "lui", "lângă", "lîngă", "mai", "mea", "mei", "mele", "mereu",
                       "meu", "mi", "mie", "mine", "mult", "multă", "mulţi", "mulţumesc", "mâine", "mîine", "mă", "ne",
                       "nevoie", "nici", "nicăieri", "nimeni", "nimeri", "nimic", "nişte", "noastre", "noastră", "noi",
                       "noroc", "nostru", "nouă", "noştri", "nu", "opt", "ori", "oricare", "orice", "oricine", "oricum",
                       "oricând", "oricât", "oricînd", "oricît", "oriunde", "patra", "patru", "patrulea", "pe",
                       "pentru", "peste", "pic", "poate", "pot", "prea", "prima", "primul", "prin", "printr", "puţin",
                       "puţina", "puţină", "până", "pînă", "rog", "sa", "sale", "sau", "se", "spate", "spre", "sub",
                       "sunt", "suntem", "sunteţi", "sută", "sînt", "sîntem", "sînteţi", "să", "săi", "său", "ta",
                       "tale", "te", "timp", "tine", "toate", "toată", "tot", "totuşi", "toţi", "trei", "treia",
                       "treilea", "tu", "tăi", "tău", "un", "una", "unde", "undeva", "unei", "uneia", "unele", "uneori",
                       "unii", "unor", "unora", "unu", "unui", "unuia", "unul", "vi", "voastre", "voastră", "voi",
                       "vostru", "vouă", "voştri", "vreme", "vreo", "vreun", "vă", "zece", "zero", "zi", "zice", "îi",
                       "îl", "îmi", "împotriva", "în", "înainte", "înaintea", "încotro", "încât", "încît", "între",
                       "întrucât", "întrucît", "îţi", "ăla", "ălea", "ăsta", "ăstea", "ăştia", "şapte", "şase", "şi",
                       "ştiu", "ţi", "ţie"]
spanish_stop_words = ["a", "actualmente", "acuerdo", "adelante", "ademas", "además", "adrede", "afirmó", "agregó",
                      "ahi", "ahora", "ahí", "al", "algo", "alguna", "algunas", "alguno", "algunos", "algún", "alli",
                      "allí", "alrededor", "ambos", "ampleamos", "antano", "antaño", "ante", "anterior", "antes",
                      "apenas", "aproximadamente", "aquel", "aquella", "aquellas", "aquello", "aquellos", "aqui",
                      "aquél", "aquélla", "aquéllas", "aquéllos", "aquí", "arriba", "arribaabajo", "aseguró", "asi",
                      "así", "atras", "aun", "aunque", "ayer", "añadió", "aún", "b", "bajo", "bastante", "bien",
                      "breve", "buen", "buena", "buenas", "bueno", "buenos", "c", "cada", "casi", "cerca", "cierta",
                      "ciertas", "cierto", "ciertos", "cinco", "claro", "comentó", "como", "con", "conmigo", "conocer",
                      "conseguimos", "conseguir", "considera", "consideró", "consigo", "consigue", "consiguen",
                      "consigues", "contigo", "contra", "cosas", "creo", "cual", "cuales", "cualquier", "cuando",
                      "cuanta", "cuantas", "cuanto", "cuantos", "cuatro", "cuenta", "cuál", "cuáles", "cuándo",
                      "cuánta", "cuántas", "cuánto", "cuántos", "cómo", "d", "da", "dado", "dan", "dar", "de", "debajo",
                      "debe", "deben", "debido", "decir", "dejó", "del", "delante", "demasiado", "demás", "dentro",
                      "deprisa", "desde", "despacio", "despues", "después", "detras", "detrás", "dia", "dias", "dice",
                      "dicen", "dicho", "dieron", "diferente", "diferentes", "dijeron", "dijo", "dio", "donde", "dos",
                      "durante", "día", "días", "dónde", "e", "ejemplo", "el", "ella", "ellas", "ello", "ellos",
                      "embargo", "empleais", "emplean", "emplear", "empleas", "empleo", "en", "encima", "encuentra",
                      "enfrente", "enseguida", "entonces", "entre", "era", "eramos", "eran", "eras", "eres", "es",
                      "esa", "esas", "ese", "eso", "esos", "esta", "estaba", "estaban", "estado", "estados", "estais",
                      "estamos", "estan", "estar", "estará", "estas", "este", "esto", "estos", "estoy", "estuvo",
                      "está", "están", "ex", "excepto", "existe", "existen", "explicó", "expresó", "f", "fin", "final",
                      "fue", "fuera", "fueron", "fui", "fuimos", "g", "general", "gran", "grandes", "gueno", "h", "ha",
                      "haber", "habia", "habla", "hablan", "habrá", "había", "habían", "hace", "haceis", "hacemos",
                      "hacen", "hacer", "hacerlo", "haces", "hacia", "haciendo", "hago", "han", "hasta", "hay", "haya",
                      "he", "hecho", "hemos", "hicieron", "hizo", "horas", "hoy", "hubo", "i", "igual", "incluso",
                      "indicó", "informo", "informó", "intenta", "intentais", "intentamos", "intentan", "intentar",
                      "intentas", "intento", "ir", "j", "junto", "k", "l", "la", "lado", "largo", "las", "le", "lejos",
                      "les", "llegó", "lleva", "llevar", "lo", "los", "luego", "lugar", "m", "mal", "manera",
                      "manifestó", "mas", "mayor", "me", "mediante", "medio", "mejor", "mencionó", "menos", "menudo",
                      "mi", "mia", "mias", "mientras", "mio", "mios", "mis", "misma", "mismas", "mismo", "mismos",
                      "modo", "momento", "mucha", "muchas", "mucho", "muchos", "muy", "más", "mí", "mía", "mías", "mío",
                      "míos", "n", "nada", "nadie", "ni", "ninguna", "ningunas", "ninguno", "ningunos", "ningún", "no",
                      "nos", "nosotras", "nosotros", "nuestra", "nuestras", "nuestro", "nuestros", "nueva", "nuevas",
                      "nuevo", "nuevos", "nunca", "o", "ocho", "os", "otra", "otras", "otro", "otros", "p", "pais",
                      "para", "parece", "parte", "partir", "pasada", "pasado", "paìs", "peor", "pero", "pesar", "poca",
                      "pocas", "poco", "pocos", "podeis", "podemos", "poder", "podria", "podriais", "podriamos",
                      "podrian", "podrias", "podrá", "podrán", "podría", "podrían", "poner", "por", "porque", "posible",
                      "primer", "primera", "primero", "primeros", "principalmente", "pronto", "propia", "propias",
                      "propio", "propios", "proximo", "próximo", "próximos", "pudo", "pueda", "puede", "pueden",
                      "puedo", "pues", "q", "qeu", "que", "quedó", "queremos", "quien", "quienes", "quiere", "quiza",
                      "quizas", "quizá", "quizás", "quién", "quiénes", "qué", "r", "raras", "realizado", "realizar",
                      "realizó", "repente", "respecto", "s", "sabe", "sabeis", "sabemos", "saben", "saber", "sabes",
                      "salvo", "se", "sea", "sean", "segun", "segunda", "segundo", "según", "seis", "ser", "sera",
                      "será", "serán", "sería", "señaló", "si", "sido", "siempre", "siendo", "siete", "sigue",
                      "siguiente", "sin", "sino", "sobre", "sois", "sola", "solamente", "solas", "solo", "solos",
                      "somos", "son", "soy", "soyos", "su", "supuesto", "sus", "suya", "suyas", "suyo", "sé", "sí",
                      "sólo", "t", "tal", "tambien", "también", "tampoco", "tan", "tanto", "tarde", "te", "temprano",
                      "tendrá", "tendrán", "teneis", "tenemos", "tener", "tenga", "tengo", "tenido", "tenía", "tercera",
                      "ti", "tiempo", "tiene", "tienen", "toda", "todas", "todavia", "todavía", "todo", "todos",
                      "total", "trabaja", "trabajais", "trabajamos", "trabajan", "trabajar", "trabajas", "trabajo",
                      "tras", "trata", "través", "tres", "tu", "tus", "tuvo", "tuya", "tuyas", "tuyo", "tuyos", "tú",
                      "u", "ultimo", "un", "una", "unas", "uno", "unos", "usa", "usais", "usamos", "usan", "usar",
                      "usas", "uso", "usted", "ustedes", "v", "va", "vais", "valor", "vamos", "van", "varias", "varios",
                      "vaya", "veces", "ver", "verdad", "verdadera", "verdadero", "vez", "vosotras", "vosotros", "voy",
                      "vuestra", "vuestras", "vuestro", "vuestros", "w", "x", "y", "ya", "yo", "z", "él", "ésa", "ésas",
                      "ése", "ésos", "ésta", "éstas", "éste", "éstos", "última", "últimas", "último", "últimos"]
swedish_stop_words = ["aderton", "adertonde", "adjö", "aldrig", "alla", "allas", "allt", "alltid", "alltså", "andra",
                      "andras", "annan", "annat", "artonde", "artonn", "att", "av", "bakom", "bara", "behöva",
                      "behövas", "behövde", "behövt", "beslut", "beslutat", "beslutit", "bland", "blev", "bli", "blir",
                      "blivit", "bort", "borta", "bra", "bäst", "bättre", "båda", "bådas", "dag", "dagar", "dagarna",
                      "dagen", "de", "del", "delen", "dem", "den", "denna", "deras", "dess", "dessa", "det", "detta",
                      "dig", "din", "dina", "dit", "ditt", "dock", "du", "där", "därför", "då", "efter", "eftersom",
                      "ej", "elfte", "eller", "elva", "en", "enkel", "enkelt", "enkla", "enligt", "er", "era", "ert",
                      "ett", "ettusen", "fanns", "fem", "femte", "femtio", "femtionde", "femton", "femtonde", "fick",
                      "fin", "finnas", "finns", "fjorton", "fjortonde", "fjärde", "fler", "flera", "flesta", "fram",
                      "framför", "från", "fyra", "fyrtio", "fyrtionde", "få", "får", "fått", "följande", "för", "före",
                      "förlåt", "förra", "första", "genast", "genom", "gick", "gjorde", "gjort", "god", "goda",
                      "godare", "godast", "gott", "gälla", "gäller", "gällt", "gärna", "gå", "går", "gått", "gör",
                      "göra", "ha", "hade", "haft", "han", "hans", "har", "heller", "hellre", "helst", "helt", "henne",
                      "hennes", "hit", "hon", "honom", "hundra", "hundraen", "hundraett", "hur", "här", "hög", "höger",
                      "högre", "högst", "i", "ibland", "icke", "idag", "igen", "igår", "imorgon", "in", "inför", "inga",
                      "ingen", "ingenting", "inget", "innan", "inne", "inom", "inte", "inuti", "ja", "jag", "ju",
                      "jämfört", "kan", "kanske", "knappast", "kom", "komma", "kommer", "kommit", "kr", "kunde",
                      "kunna", "kunnat", "kvar", "legat", "ligga", "ligger", "lika", "likställd", "likställda", "lilla",
                      "lite", "liten", "litet", "länge", "längre", "längst", "lätt", "lättare", "lättast", "långsam",
                      "långsammare", "långsammast", "långsamt", "långt", "man", "med", "mellan", "men", "mer", "mera",
                      "mest", "mig", "min", "mina", "mindre", "minst", "mitt", "mittemot", "mot", "mycket", "många",
                      "måste", "möjlig", "möjligen", "möjligt", "möjligtvis", "ned", "nederst", "nedersta", "nedre",
                      "nej", "ner", "ni", "nio", "nionde", "nittio", "nittionde", "nitton", "nittonde", "nog", "noll",
                      "nr", "nu", "nummer", "när", "nästa", "någon", "någonting", "något", "några", "nödvändig",
                      "nödvändiga", "nödvändigt", "nödvändigtvis", "och", "också", "ofta", "oftast", "olika", "olikt",
                      "om", "oss", "på", "rakt", "redan", "rätt", "sade", "sagt", "samma", "sedan", "senare", "senast",
                      "sent", "sex", "sextio", "sextionde", "sexton", "sextonde", "sig", "sin", "sina", "sist", "sista",
                      "siste", "sitt", "sitta", "sju", "sjunde", "sjuttio", "sjuttionde", "sjutton", "sjuttonde",
                      "själv", "sjätte", "ska", "skall", "skulle", "slutligen", "små", "smått", "snart", "som", "stor",
                      "stora", "stort", "större", "störst", "säga", "säger", "sämre", "sämst", "så", "sådan", "sådana",
                      "sådant", "tack", "tidig", "tidigare", "tidigast", "tidigt", "till", "tills", "tillsammans",
                      "tio", "tionde", "tjugo", "tjugoen", "tjugoett", "tjugonde", "tjugotre", "tjugotvå", "tjungo",
                      "tolfte", "tolv", "tre", "tredje", "trettio", "trettionde", "tretton", "trettonde", "två",
                      "tvåhundra", "under", "upp", "ur", "ursäkt", "ut", "utan", "utanför", "ute", "vad", "var", "vara",
                      "varför", "varifrån", "varit", "varje", "varken", "vars", "varsågod", "vart", "vem", "vems",
                      "verkligen", "vi", "vid", "vidare", "viktig", "viktigare", "viktigast", "viktigt", "vilka",
                      "vilkas", "vilken", "vilket", "vill", "vänster", "vänstra", "värre", "vår", "våra", "vårt", "än",
                      "ännu", "är", "även", "åt", "åtminstone", "åtta", "åttio", "åttionde", "åttonde", "över",
                      "övermorgon", "överst", "övre"]

# the text to be evaluated
input_text = sys.argv[1]

input_text_character_count = len(input_text)

print("Text has been received")

# the variable translation_array contains the translation of input_text in 9 different languages
translation_array = get_array_of_translations(input_text)

# printing all the translations, for testing purposes
# i = 1
# for language in translation_array:
#     print(i)
#     print(language + '\n')
#     i = i + 1

print("Text has been translated to nine different languages")

# the keywords_array variable contains the 3 most important keyword phrases for each of the 9 languages
keywords_array = get_keywords_array(translation_array)

# printing all the keyword lists, for testing purposes
# i = 1
# for language_keywords in keywords_array:
#     print("----")
#     print("----")
#     print(i)
#     print("----")
#     print("----")
#     for keywords in language_keywords:
#         print(keywords)
#     i = i + 1

print("Keywords have been extracted for each of the nine different translations")

# the keyword_search_terms_array contains a single string made out of the keyword phrases for each language that will
# be used as the search phrase in the next step
keyword_search_terms_array = get_keyword_search_terms_array(keywords_array)

# printing all the search phrases, for testing purposes
# i = 1
# for keyword_search_term in keyword_search_terms_array:
#     print("----")
#     print("----")
#     print(i)
#     print("----")
#     print("----")
#     print(keyword_search_term)
#     i = i + 1

print("Keyword search phrases have been created")

# the urls_array contains the first n (to be decided) google search results that appear when searching each keyword_search_term
urls_array = get_array_of_urls(keyword_search_terms_array)

# printing all the urls corresponding to each language, for testing purposes
# i = 1
# for urls in urls_array:
#     print("----")
#     print("----")
#     print(i)
#     print("----")
#     print("----")
#     print(urls)
#     i = i + 1

print("Candidate URLs have been extracted for each different language")

# the htmls_array contains the raw html of the websites corresponding to the urls in urls_array
htmls_array = get_array_of_htmls(urls_array)

# printing all the htmls corresponding to each language, for testing purposes
# i = 1
# for htmls in htmls_array:
#     print("----")
#     print("----")
#     print(i)
#     print("----")
#     print("----")
#     print(htmls)
#     i = i + 1

print("The HTML content associated with each URL has been extracted")

# the texts_array contains only the visible text parts of the htmls that were previously collected
texts_array = get_array_of_texts(htmls_array)

# printing all the texts corresponding to each language, for testing purposes
# i = 1
# j = 1
# for texts in texts_array:
#     print("----")
#     print("----")
#     print(i)
#     for text in texts:
#         print(j)
#         print("----")
#         print("----")
#         print(text)
#         print("----")
#         print("----")
#         j = j + 1
#     print("----")
#     print("----")
#     i = i + 1

print("The visible text of the web pages has been filtered")

dutch_texts = texts_array[Language.DUTCH.value]
french_texts = texts_array[Language.FRENCH.value]
german_texts = texts_array[Language.GERMAN.value]
italian_texts = texts_array[Language.ITALIAN.value]
polish_texts = texts_array[Language.POLISH.value]
portuguese_texts = texts_array[Language.PORTUGUESE.value]
romanian_texts = texts_array[Language.ROMANIAN.value]
spanish_texts = texts_array[Language.SPANISH.value]
swedish_texts = texts_array[Language.SWEDISH.value]

dutch_texts_chunks = get_array_of_text_chunks(dutch_texts, input_text_character_count)
french_texts_chunks = get_array_of_text_chunks(french_texts, input_text_character_count)
german_texts_chunks = get_array_of_text_chunks(german_texts, input_text_character_count)
italian_texts_chunks = get_array_of_text_chunks(italian_texts, input_text_character_count)
polish_texts_chunks = get_array_of_text_chunks(polish_texts, input_text_character_count)
portuguese_texts_chunks = get_array_of_text_chunks(portuguese_texts, input_text_character_count)
romanian_texts_chunks = get_array_of_text_chunks(romanian_texts, input_text_character_count)
spanish_texts_chunks = get_array_of_text_chunks(spanish_texts, input_text_character_count)
swedish_texts_chunks = get_array_of_text_chunks(swedish_texts, input_text_character_count)

print("Performing detailed analysis for Dutch")
print("----")

j = 0
for chunks in dutch_texts_chunks:
    dutch_list_to_be_vectorized = get_list_to_be_vectorized(translation_array[Language.DUTCH.value], chunks)

    dutch_cosine_similarity_matrix = create_cosine_similarity_matrix(dutch_list_to_be_vectorized, dutch_stop_words)

    results_row = dutch_cosine_similarity_matrix[0]

    i = 0
    flag = 1
    for cosine_sim in results_row:
        if cosine_sim > 0.2 and round(cosine_sim) != 1:
            if flag == 1:
                print(urls_array[Language.DUTCH.value][j])
                print("----")
                flag = 0
            print(dutch_list_to_be_vectorized[i])
            print("cosine similarity of:", cosine_sim,
                  " above the 0.2 threshold, inspection of the URL recommended")
            print("----")
        i = i + 1
    j = j + 1

print("Performing detailed analysis for French")
print("----")

j = 0
for chunks in french_texts_chunks:
    french_list_to_be_vectorized = get_list_to_be_vectorized(translation_array[Language.FRENCH.value], chunks)

    french_cosine_similarity_matrix = create_cosine_similarity_matrix(french_list_to_be_vectorized, french_stop_words)

    results_row = french_cosine_similarity_matrix[0]

    i = 0
    flag = 1
    for cosine_sim in results_row:
        if cosine_sim > 0.2 and round(cosine_sim) != 1:
            if flag == 1:
                print(urls_array[Language.FRENCH.value][j])
                print("----")
                flag = 0
            print(french_list_to_be_vectorized[i])
            print("cosine similarity of:", cosine_sim,
                  " above the 0.2 threshold, inspection of the URL recommended")
            print("----")
        i = i + 1
    j = j + 1

print("Performing detailed analysis for German")
print("----")

j = 0
for chunks in german_texts_chunks:
    german_list_to_be_vectorized = get_list_to_be_vectorized(translation_array[Language.GERMAN.value], chunks)

    german_cosine_similarity_matrix = create_cosine_similarity_matrix(german_list_to_be_vectorized, german_stop_words)

    results_row = german_cosine_similarity_matrix[0]

    i = 0
    flag = 1
    for cosine_sim in results_row:
        if cosine_sim > 0.2 and round(cosine_sim) != 1:
            if flag == 1:
                print(urls_array[Language.GERMAN.value][j])
                print("----")
                flag = 0
            print(german_list_to_be_vectorized[i])
            print("cosine similarity of:", cosine_sim,
                  " above the 0.2 threshold, inspection of the URL recommended")
            print("----")
        i = i + 1
    j = j + 1

print("Performing detailed analysis for Italian")
print("----")

j = 0
for chunks in italian_texts_chunks:
    italian_list_to_be_vectorized = get_list_to_be_vectorized(translation_array[Language.ITALIAN.value], chunks)

    italian_cosine_similarity_matrix = create_cosine_similarity_matrix(italian_list_to_be_vectorized,
                                                                       italian_stop_words)

    results_row = italian_cosine_similarity_matrix[0]

    i = 0
    flag = 1
    for cosine_sim in results_row:
        if cosine_sim > 0.2 and round(cosine_sim) != 1:
            if flag == 1:
                print(urls_array[Language.ITALIAN.value][j])
                print("----")
                flag = 0
            print(italian_list_to_be_vectorized[i])
            print("cosine similarity of:", cosine_sim,
                  " above the 0.2 threshold, inspection of the URL recommended")
            print("----")
        i = i + 1
    j = j + 1

print("Performing detailed analysis for Polish")
print("----")

j = 0
for chunks in polish_texts_chunks:
    polish_list_to_be_vectorized = get_list_to_be_vectorized(translation_array[Language.POLISH.value], chunks)

    polish_cosine_similarity_matrix = create_cosine_similarity_matrix(polish_list_to_be_vectorized, polish_stop_words)

    results_row = polish_cosine_similarity_matrix[0]

    i = 0
    flag = 1
    for cosine_sim in results_row:
        if cosine_sim > 0.2 and round(cosine_sim) != 1:
            if flag == 1:
                print(urls_array[Language.POLISH.value][j])
                print("----")
                flag = 0
            print(polish_list_to_be_vectorized[i])
            print("cosine similarity of:", cosine_sim,
                  " above the 0.2 threshold, inspection of the URL recommended")
            print("----")
        i = i + 1
    j = j + 1

print("Performing detailed analysis for Portuguese")
print("----")

j = 0
for chunks in portuguese_texts_chunks:
    portuguese_list_to_be_vectorized = get_list_to_be_vectorized(translation_array[Language.PORTUGUESE.value], chunks)

    portuguese_cosine_similarity_matrix = create_cosine_similarity_matrix(portuguese_list_to_be_vectorized,
                                                                          portuguese_stop_words)

    results_row = portuguese_cosine_similarity_matrix[0]

    i = 0
    flag = 1
    for cosine_sim in results_row:
        if cosine_sim > 0.2 and round(cosine_sim) != 1:
            if flag == 1:
                print(urls_array[Language.PORTUGUESE.value][j])
                print("----")
                flag = 0
            print(portuguese_list_to_be_vectorized[i])
            print("cosine similarity of:", cosine_sim,
                  " above the 0.2 threshold, inspection of the URL recommended")
            print("----")
        i = i + 1
    j = j + 1

print("Performing detailed analysis for Romanian")
print("----")

j = 0
for chunks in romanian_texts_chunks:
    romanian_list_to_be_vectorized = get_list_to_be_vectorized(translation_array[Language.ROMANIAN.value], chunks)

    romanian_cosine_similarity_matrix = create_cosine_similarity_matrix(romanian_list_to_be_vectorized,
                                                                        romanian_stop_words)

    results_row = romanian_cosine_similarity_matrix[0]

    i = 0
    flag = 1
    for cosine_sim in results_row:
        if cosine_sim > 0.2 and round(cosine_sim) != 1:
            if flag == 1:
                print(urls_array[Language.ROMANIAN.value][j])
                print("----")
                flag = 0
            print(romanian_list_to_be_vectorized[i])
            print("cosine similarity of:", cosine_sim,
                  " above the 0.2 threshold, inspection of the URL recommended")
            print("----")
        i = i + 1
    j = j + 1

print("Performing detailed analysis for Spanish")
print("----")

j = 0
for chunks in spanish_texts_chunks:
    spanish_list_to_be_vectorized = get_list_to_be_vectorized(translation_array[Language.SPANISH.value], chunks)

    spanish_cosine_similarity_matrix = create_cosine_similarity_matrix(spanish_list_to_be_vectorized,
                                                                       spanish_stop_words)

    results_row = spanish_cosine_similarity_matrix[0]

    i = 0
    flag = 1
    for cosine_sim in results_row:
        if cosine_sim > 0.2 and round(cosine_sim) != 1:
            if flag == 1:
                print(urls_array[Language.SPANISH.value][j])
                print("----")
                flag = 0
            print(spanish_list_to_be_vectorized[i])
            print("cosine similarity of:", cosine_sim,
                  " above the 0.2 threshold, inspection of the URL recommended")
            print("----")
        i = i + 1
    j = j + 1

print("Performing detailed analysis for Swedish")
print("----")

j = 0
for chunks in swedish_texts_chunks:
    swedish_list_to_be_vectorized = get_list_to_be_vectorized(translation_array[Language.SWEDISH.value], chunks)

    swedish_cosine_similarity_matrix = create_cosine_similarity_matrix(swedish_list_to_be_vectorized,
                                                                       swedish_stop_words)

    results_row = swedish_cosine_similarity_matrix[0]

    i = 0
    flag = 1
    for cosine_sim in results_row:
        if cosine_sim > 0.2 and round(cosine_sim) != 1:
            if flag == 1:
                print(urls_array[Language.SWEDISH.value][j])
                print("----")
                flag = 0
            print(swedish_list_to_be_vectorized[i])
            print("cosine similarity of:", cosine_sim,
                  " above the 0.2 threshold, inspection of the URL recommended")
            print("----")
        i = i + 1
    j = j + 1

# timing the whole process
print("--- %s seconds ---" % (time.time() - start_time))
