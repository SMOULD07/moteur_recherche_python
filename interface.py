import streamlit as st
import os
from main import search_file, check_file_readability, read_file

# Interface principale
def main():
    st.title("Moteur de recherche de fichiers")

    # Section pour changer de répertoire
    if st.button('Changer de dossier'):
        change_directory()

    # Afficher le chemin actuel
    if st.button('Voir le chemin actuel'):
        see_current_path()

    # Rechercher un fichier dans le répertoire
    search_file_ui()

    # Lire un fichier
    read_file_ui()

# Fonction pour changer de répertoire
def change_directory():
    new_dir = st.text_input("Entrez le chemin du nouveau répertoire :")
    if st.button("Changer"):
        if new_dir :
            if os.path.exists(new_dir): 
                try:
                    os.chdir(new_dir)
                    st.success(f"Dossier changé à : {os.getcwd()}")
                except Exception as e:
                    st.error(f"Erreur : {e}")
            else:
                st.error("Le chemin spécifié n'existe pas.")
        else :
            st.error("Veuillez entrer un chemain valide.")


# Fonction pour afficher le répertoire actuel
def see_current_path():
    st.write(f"Vous êtes dans : {os.getcwd()}")

# Interface pour rechercher un fichier
def search_file_ui():
    search_pattern = st.text_input('Motif de fichier à rechercher (ex: *.txt):')
    if st.button("Rechercher"):
        # repertoire courant 
        st.write(f"repertoire courant : {os.getcwd()}")
        
        files_found = search_file(search_pattern)
        if files_found:
            st.write("Fichiers trouvés :")
            for file in files_found:
                st.write(file)
        else:
            st.warning("Aucun fichier trouvé.")

# Interface pour lire un fichier
def read_file_ui():
    file_path = st.text_input("Entrez le chemin du fichier à lire :")
    
    if st.button("Vérifier si le fichier est lisible"):
        if check_file_readability(file_path):
            st.success("Le fichier est lisible.")
        else:
            st.error("Le fichier ne peut pas être lu.")
    
    if st.button("Afficher les premières lignes"):
        if check_file_readability(file_path):
            with open(file_path, 'r') as f:
                lines = [f.readline().strip() for _ in range(10)]
                st.text("\n".join(lines))

    start_line = st.number_input("Afficher à partir de la ligne :", min_value=1)
    if st.button("Afficher le contenu du fichier à partir d'une ligne donnée"):
        if check_file_readability(file_path):
            with open(file_path, 'r') as f:
                for i, line in enumerate(f, 1):
                     if i >= start_line:
                        st.write(line.strip())

if __name__ == "__main__":
    main()