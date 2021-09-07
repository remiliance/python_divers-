import requests
from bs4 import BeautifulSoup
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.title)

titres = soup.find_all("a", class_="govuk-link")

print(titres)

#print(soup)

def mettre_au_carre(x):
    return x ** 2  # x ** 2 = x puissance 2, pour les cerveaux lents :-'


def appliquer_fonction(fonc, valeur):
    return fonc(valeur)  # On utilise la fonction callback fonc avec comme paramètre valeur.


print
appliquer_fonction(mettre_au_carre, 3)  # Affiche 9, c'est à dire mettre_au_carre(3)
