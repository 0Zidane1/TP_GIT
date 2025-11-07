from bs4 import BeautifulSoup

# Nom du fichier HTML d’origine
fichier_html = "page_simple.html"
# Nom du fichier de sortie
fichier_modifie = "page_simple_modifie.html"

# Lecture du fichier HTML
with open(fichier_html, "r", encoding="utf-8") as f:
    contenu = f.read()

# Analyse du HTML avec BeautifulSoup
soup = BeautifulSoup(contenu, "html.parser")

# Création d’un nouveau bouton
nouveau_bouton = soup.new_tag("a", href="#", **{"class": "button"})
nouveau_bouton.string = "Nouveau bouton"

# Optionnel : tu peux en créer plusieurs
autre_bouton = soup.new_tag("a", href="#", **{"class": "button"})
autre_bouton.string = "Bouton secondaire"

# Trouve l’élément <main> pour y insérer les boutons
main = soup.find("main")

# Insère les boutons avant la fermeture du <main>
main.append(nouveau_bouton)
main.append(soup.new_tag("br"))
main.append(autre_bouton)

# Sauvegarde le nouveau HTML
with open(fichier_modifie, "w", encoding="utf-8") as f:
    f.write(str(soup.prettify()))

print("✅ Les boutons ont été ajoutés dans", fichier_modifie)
