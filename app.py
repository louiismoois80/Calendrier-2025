import streamlit as st
from datetime import datetime

# Configuration de la page
st.set_page_config(page_title="Calendrier de l'Avent Agreg", page_icon="🎄", layout="wide")

# --- FONCTION DE SÉCURITÉ ---
def verifier_acces():
    """Renvoie True si le mot de passe est bon, False sinon."""
    
    # Si l'utilisateur est déjà connecté dans sa session, on laisse passer
    if st.session_state.get('est_connecte'):
        return True

    # Sinon, on affiche le formulaire de connexion
    st.title("🔐 Accès Réservé - Agrégation")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Champ mot de passe
        pwd = st.text_input("Mot de passe :", type="password")
        
        if st.button("Entrer"):
            # --- DÉFINISSEZ VOTRE MOT DE PASSE ICI ---
            if pwd == "noel!!!":  
                st.session_state['est_connecte'] = True
                st.rerun()  # On recharge la page pour afficher le contenu
            else:
                st.error("Mot de passe incorrect.")
    
    return False

# --- DÉBUT DU PROGRAMME PRINCIPAL ---

# On lance la vérification. 
# Si c'est Faux, le script s'arrête là (return). 
# Si c'est Vrai, il continue et lit le code du calendrier.
if not verifier_acces():
    st.stop()

st.title("🎄 Calendrier de l'Avent 🎄 ")
st.markdown("### Un exercice préliminaire par jour pour garder le rythme !")

# --- CONFIGURATION DES EXERCICES ---
# C'est ici que vous remplirez vos exercices.
# Vous pouvez mettre du texte, du LaTeX, ou des noms de fichiers images.
exercices = {
    1: {"titre": "Analyse", "type": "image", "contenu": "ap_sujet_1999.png"},
    2: {"titre": "Algèbre", "type": "image", "contenu": "mg_ext_2025.png"},
    3: {"titre": "Analyse", "type": "image", "contenu": "ap_ext_2001.png"},
    4: {"titre": "Algèbre", "type": "image", "contenu": "mg_sujet_2022.png"},
    5: {"titre": "Algèbre", "type": "image", "contenu": "mg_ext_2003.png"},
    6: {"titre": "Analyse", "type": "image", "contenu": "ap_sujet_2020.png"},
    7: {"titre": "Analyse", "type": "image", "contenu": "ap_sujet_2018.png"},
    8: {"titre": "Algèbre", "type": "image", "contenu": "mg_sujet_2018.png"},
    9: {"titre": "Algèbre", "type": "image", "contenu": "mg_sujet_2020.png"},
    10: {"titre": "Algèbre", "type": "image", "contenu": "mg_sujet_2025.png"},
    11: {"titre": "Analyse", "type": "image", "contenu": "ap_ext_2025.png"},
    12: {"titre": "Analyse", "type": "image", "contenu": "ap_sujet_2005.png"},
    13: {"titre": "Algèbre", "type": "image", "contenu": "mg_sujet_2013.png"},
    14: {"titre": "Algèbre", "type": "image", "contenu": "mg_ext_2023.png"},
    15: {"titre": "Algèbre", "type": "image", "contenu": "mg_sujet_2023.png"},
    16: {"titre": "Analyse", "type": "image", "contenu": "ap_ext_2024.png"},
    17: {"titre": "Analyse", "type": "image", "contenu": "ap_sujet_2010.png"},
    18: {"titre": "Analyse", "type": "image", "contenu": "ap_sujet_2006.png"},
    19: {"titre": "Algèbre", "type": "image", "contenu": "mg_ext_2001.png"},
    20: {"titre": "Analyse", "type": "image", "contenu": "ap_sujet_2013.png"},
    21: {"titre": "Algèbre", "type": "image", "contenu": "mg_sujet_2021.png"},
    22: {"titre": "Analyse", "type": "image", "contenu": "ap_sujet_2025.png"},
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
        st.write("Bon courage 💩🎅🏻")
            
