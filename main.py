import json
import os

FICHIER_JSON = "bibliotheque.json"


def charger_bibliotheque():
    if os.path.exists(FICHIER_JSON):
        with open(FICHIER_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    return []



def sauvegarder_bibliotheque(bibliotheque):
    with open(FICHIER_JSON, "w", encoding="utf-8") as f:
        json.dump(bibliotheque, f, indent=4, ensure_ascii=False)


def generer_id(bibliotheque):
    if not bibliotheque:
        return 1
    return max(livre["ID"] for livre in bibliotheque) + 1


def afficher_livres(bibliotheque):
    if not bibliotheque:
        print("La bibliothèque est vide.")
        return
    for livre in bibliotheque:
        print(f'\nID: {livre["ID"]}')
        print(f'Titre: {livre["Titre"]}')
        print(f'Auteur: {livre["Auteur"]}')
        print(f'Année: {livre["Année"]}')
        print("Lu :", "Oui" if livre["Lu"] else "Non")
        if livre["Lu"]:
            print(f'Note: {livre["Note"]}')
            print(f'Commentaire: {livre.get("Commentaire", "")}')


def ajouter_livre(bibliotheque):
    titre = input("Titre: ")
    auteur = input("Auteur: ")
    try:
        annee = int(input("Année de publication: "))
    except ValueError:
        print("Année invalide.")
        return
    livre = {
        "ID": generer_id(bibliotheque),
        "Titre": titre,
        "Auteur": auteur,
        "Année": annee,
        "Lu": False,
        "Note": None
    }
    bibliotheque.append(livre)
    print("Livre ajouté.")


def supprimer_livre(bibliotheque):
    try:
        id_supprimer = int(input("ID du livre à supprimer: "))
    except ValueError:
        print("ID invalide.")
        return
    for livre in bibliotheque:
        if livre["ID"] == id_supprimer:
            confirmation = input(f"Supprimer {livre['Titre']} ? (o/n): ")
            if confirmation.lower() == "o":
                bibliotheque.remove(livre)
                print("Livre supprimé.")
            return
    print("Livre non trouvé.")


def rechercher_livre(bibliotheque):
    mot_cle = input("Mot-clé (titre ou auteur): ").lower()
    resultats = [l for l in bibliotheque if mot_cle in l["Titre"].lower() or mot_cle in l["Auteur"].lower()]
    if resultats:
        afficher_livres(resultats)
    else:
        print("Aucun résultat trouvé.")


def marquer_comme_lu(bibliotheque):
    try:
        id_livre = int(input("ID du livre lu: "))
    except ValueError:
        print("ID invalide.")
        return
    for livre in bibliotheque:
        if livre["ID"] == id_livre:
            livre["Lu"] = True
            try:
                livre["Note"] = float(input("Note sur 10: "))
            except ValueError:
                livre["Note"] = None
            livre["Commentaire"] = input("Commentaire: ")
            print("Livre marqué comme lu.")
            return
    print("Livre non trouvé.")


def afficher_filtre_lu(bibliotheque):
    choix = input("Afficher (1) lus ou (2) non lus ? ")
    if choix == "1":
        livres = [l for l in bibliotheque if l["Lu"]]
    elif choix == "2":
        livres = [l for l in bibliotheque if not l["Lu"]]
    else:
        print("Choix invalide.")
        return
    afficher_livres(livres)

def trier_livres(bibliotheque):
    print("Trier par : (1) Année, (2) Auteur, (3) Note")
    choix = input("Votre choix: ")
    if choix == "1":
        livres = sorted(bibliotheque, key=lambda l: l["Année"])
    elif choix == "2":
        livres = sorted(bibliotheque, key=lambda l: l["Auteur"].lower())
    elif choix == "3":
        livres = sorted(bibliotheque, key=lambda l: (l["Note"] is not None, l["Note"] or 0), reverse=True)
    else:
        print("Choix invalide.")
        return
    afficher_livres(livres)


def afficher_menu():
    print("""
==== MENU ====
1. Afficher tous les livres
2. Ajouter un livre
3. Supprimer un livre
4. Rechercher un livre
5. Marquer un livre comme lu
6. Afficher les livres lus ou non lus
7. Trier les livres
8. Quitter
""")


def main():
    bibliotheque = charger_bibliotheque()
    print("Bienvenue dans votre bibliothèque personnelle - Mohand Said Kemiche")

    while True:
        afficher_menu()
        choix = input("Choix: ")
        if choix == "1":
            afficher_livres(bibliotheque)
        elif choix == "2":
            ajouter_livre(bibliotheque)
        elif choix == "3":
            supprimer_livre(bibliotheque)
        elif choix == "4":
            rechercher_livre(bibliotheque)
        elif choix == "5":
            marquer_comme_lu(bibliotheque)
        elif choix == "6":
            afficher_filtre_lu(bibliotheque)
        elif choix == "7":
            trier_livres(bibliotheque)
        elif choix == "8":
            sauvegarder_bibliotheque(bibliotheque)
            print("Données sauvegardées. À bientôt !")
            break
        else:
            print("Choix invalide. Réessaie.")


if __name__ == "__main__" 
main()
