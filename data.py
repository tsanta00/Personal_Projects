# data.py
# Tout le contenu du bot est ici. Facile à modifier sans toucher au code.

MENU_PRINCIPAL = {
    "titre": "🤖 Bienvenue ! En quoi puis-je aider ?",
    "options": {
        "1": ("📞 Contacts", "contacts"),
        "2": ("❓ Questions fréquentes", "faq"),
        "3": ("ℹ️ Informations", "infos"),
        "4": ("🚪 Quitter", "quit"),
    }
}

MENUS = {
    "contacts": {
        "titre": "📞 Contacts — Qui veux-tu joindre ?",
        "options": {
            "1": ("👤 Président", "contact_president"),
            "2": ("👤 Vice-Président", "contact_vice"),
            "3": ("👤 Secrétaire", "contact_secretaire"),
            "4": ("⬅️ Retour", "back"),
        }
    },
    "faq": {
        "titre": "❓ Questions fréquentes sur l'Ambassade",
        "options": {
            "1": ("📍 Adresse de l'Ambassade", "faq_adresse"),
            "2": ("🕒 Horaires d'ouverture", "faq_horaires"),
            "3": ("📞 Contacts de l'Ambassade", "faq_contacts"),
            "4": ("⬅️ Retour", "back"),
        }
    },
    "infos": {
        "titre": "ℹ️ Informations — De quel document as-tu besoin ?",
        "options": {
            "1": ("📄 Documents pour RVPO", "infos_rvpo"),
            "2": ("🛂 Documents pour nouveau passeport", "infos_passeport"),
            "3": ("📝 Documents pour registration", "infos_registration"),
            "4": ("⬅️ Retour", "back"),
        }
    },
}

# Réponses finales (feuilles de l'arbre)
REPONSES = {
    # Contacts
    "contact_president":   "👤 Président : +7 999 922 70 57",
    "contact_vice":        "👤 Vice-Président : +7 999 922 70 57",
    "contact_secretaire":  "👤 Secrétaire : +7 999 922 70 57",

    # FAQ Ambassade
    "faq_adresse":   "📍 Adresse de l'Ambassade :\n[à compléter avec l'adresse réelle]",
    "faq_horaires":  "🕒 Horaires d'ouverture :\nLundi–Vendredi, 9h00–17h00\n(fermé les jours fériés)",
    "faq_contacts":  "📞 Téléphone : +7 999 922 70 57\n📧 Email : ambassade@example.com",

    # Informations documents
    "infos_rvpo": (
        "📄 Documents pour le RVPO :\n"
        "  • Passeport original + copie\n"
        "  • Formulaire rempli\n"
        "  • Photo d'identité récente\n"
        "  • Preuve de résidence"
    ),
    "infos_passeport": (
        "🛂 Documents pour un nouveau passeport :\n"
        "  • Ancien passeport\n"
        "  • Acte de naissance\n"
        "  • 2 photos d'identité\n"
        "  • Formulaire de demande"
    ),
    "infos_registration": (
        "📝 Documents pour la registration :\n"
        "  • Passeport\n"
        "  • Formulaire de registration\n"
        "  • Preuve d'adresse"
    ),
}