# bot.py
from data import MENU_PRINCIPAL, MENUS, REPONSES


def afficher_menu(menu):
    """Affiche un menu (titre + options)."""
    print("\n" + "=" * 50)
    print(menu["titre"])
    print("=" * 50)
    for touche, (label, _) in menu["options"].items():
        print(f"  {touche}. {label}")
    print("-" * 50)


def demander_choix(menu):
    """Demande un choix jusqu'à ce qu'il soit valide."""
    options_valides = list(menu["options"].keys())
    while True:
        choix = input("Ton choix : ").strip()
        if choix in options_valides:
            return choix
        print(f"⚠️  Choix invalide. Tape un chiffre parmi {options_valides}.")


def lancer_bot():
    """Boucle principale du chatbot."""
    print("\n🤖 Bonjour ! Je suis l'assistant virtuel de RM.")
    menu_actuel = MENU_PRINCIPAL

    while True:
        afficher_menu(menu_actuel)
        choix = demander_choix(menu_actuel)
        _, action = menu_actuel["options"][choix]

        if action == "quit":
            print("\n👋 Merci d'avoir utilisé l'assistant. À bientôt !\n")
            break

        elif action == "back":
            menu_actuel = MENU_PRINCIPAL

        elif action in MENUS:
            menu_actuel = MENUS[action]

        elif action in REPONSES:
            print("\n" + "─" * 50)
            print(REPONSES[action])
            print("─" * 50)
            input("\n(Appuie sur Entrée pour revenir au menu...)")
            menu_actuel = MENU_PRINCIPAL

        else:
            print("⚠️  Action inconnue.")