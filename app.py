import streamlit as st
from data import MENU_PRINCIPAL, MENUS, REPONSES

st.set_page_config(page_title="Assistant RM", page_icon="🤖")
st.title("🤖 Assistant virtuel RM")

# Initialisation de la session
if "menu" not in st.session_state:
    st.session_state.menu = "principal"

def afficher_menu(nom_menu):
    menu = MENU_PRINCIPAL if nom_menu == "principal" else MENUS[nom_menu]
    st.subheader(menu["titre"])

    for touche, (label, action) in menu["options"].items():
        if st.button(label, key=f"{nom_menu}_{touche}", use_container_width=True):
            gerer_action(action)

def gerer_action(action):
    if action == "quit":
        st.session_state.menu = "fin"
    elif action == "back":
        st.session_state.menu = "principal"
    elif action in MENUS:
        st.session_state.menu = action
    elif action in REPONSES:
        st.session_state.menu = "reponse"
        st.session_state.reponse_actuelle = action

# Affichage
if st.session_state.menu == "fin":
    st.success("👋 Merci, à bientôt !")
elif st.session_state.menu == "reponse":
    st.info(REPONSES[st.session_state.reponse_actuelle])
    if st.button("⬅️ Retour"):
        st.session_state.menu = "principal"
        st.rerun()
else:
    afficher_menu(st.session_state.menu)