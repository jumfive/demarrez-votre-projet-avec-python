# -*-coding:Utf-8 -*
import random

quitter = False
#page en cours
#https://openclassrooms.com/fr/courses/4262331-demarrez-votre-projet-avec-python/4268056-modifiez-des-nombres

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre.",
    "Un beau pet est bien plus drôle qu'un bon mot.",
    "Une épouse adultère ne se sent jamais coupable que des tromperies que son mari connaît.",
    "Une femme doit toujours avouer son âge quand il lui va bien."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]



# Show random quote:
def get_random_item_list(une_liste):
    nbAleatoire = random.randrange(0,len(quotes))
    return une_liste[nbAleatoire]


formater_une_citation = "{citation} - ({personnage})";
#initialisation
print(len(characters),' personnages')
print(len(quotes),' citations')



while quitter == False:
    user_answer = input("Tappe un truc (ou Q pour quitter)\n")
    if user_answer == 'Q':
        quitter = True
    else:
        print(formater_une_citation.format(citation=get_random_item_list(quotes),personnage=get_random_item_list(characters).capitalize()))
