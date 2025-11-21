import streamlit as st
from datetime import datetime

# Configuration de la page
st.set_page_config(page_title="Calendrier de l'Avent Agreg", page_icon="🎄", layout="wide")

st.title("🎄 Calendrier de l'Avent - Agrégation Externe 🎄")
st.markdown("### Un exercice préliminaire par jour pour garder le rythme !")

# --- CONFIGURATION DES EXERCICES ---
# C'est ici que vous remplirez vos exercices.
# Vous pouvez mettre du texte, du LaTeX, ou des noms de fichiers images.
exercices = {
    1: {"titre": "Sujet 2018 - Analyse", "type": "image", "contenu": "exo_jour_1.png"},
    2: {"titre": "Sujet 2021 - Algèbre", "type": "latex", "contenu": r"Soit $G$ un groupe fini d'ordre $p^k$..."},
    # Ajoutez les autres jours ici...
}

# --- LOGIQUE DE DATE ---
# Pour tester avant décembre, changez cette variable en une date fictive (ex: datetime(2025, 12, 10))
# Pour la version finale, utilisez : main_tenant = datetime.now()
main_tenant = datetime.now()

# --- AFFICHAGE DE LA GRILLE ---
cols = st.columns(4) # 4 colonnes pour faire un joli calendrier

for jour in range(1, 25):
    col = cols[(jour - 1) % 4] # Distribution dans les colonnes

    with col:
        # Création d'un container visuel pour chaque jour
        with st.container(border=True):
            st.subheader(f"Jour {jour}")

            # Vérification de la date
            # Note: On vérifie si on est en décembre ET si le jour est atteint
            # (Simplifié ici : on suppose qu'on lance le site en décembre)
            date_acces = datetime(main_tenant.year, 12, jour)

            if main_tenant >= date_acces:
                # Le jour est accessible
                if st.button(f"Ouvrir la case {jour}", key=f"btn_{jour}"):
                    # On utilise une variable de session pour retenir quel jour est ouvert
                    st.session_state['jour_ouvert'] = jour
            else:
                # Le jour n'est pas encore accessible
                st.button(f"🔒 {jour} Décembre", disabled=True, key=f"lock_{jour}")

# --- AFFICHAGE DE L'EXERCICE SÉLECTIONNÉ ---
st.divider()

if 'jour_ouvert' in st.session_state:
    jour = st.session_state['jour_ouvert']
    data = exercices.get(jour)

    if data:
        st.header(f"🎁 Exercice du Jour {jour} : {data['titre']}")

        if data['type'] == 'latex':
            st.info("À vos stylos !")
            st.latex(data['contenu'])

        elif data['type'] == 'image':
            # Assurez-vous d'avoir le fichier image dans le même dossier ou un sous-dossier
            try:
                st.image(data['contenu'], caption="Extrait du sujet")
            except:
                st.error(f"L'image '{data['contenu']}' est introuvable. Vérifiez le dossier.")

        st.markdown("---")
        with st.expander("Voir un indice ou le corrigé (Spoiler)"):
            st.write("Ici vous pouvez mettre une indication pour démarrer...")