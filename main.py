import os
import glob


# Menu principal
def menu():
    # Commandes possibles
    allowed_commands = ["cd", "scp", "sf", "rf", "exit"]
    user_input = ""

    # Boucle pour demander une commande valide
    while user_input not in allowed_commands:
        user_input = input("Command : ")
        if user_input not in allowed_commands:
            print("Unrecognized command :", user_input)

    # Actions pour chaque commande
    if user_input == "cd":
        # Changer de répertoire
        os.chdir(input("Go to : "))
        print("Directory changed to :", os.getcwd())

    elif user_input == "scp":
        # Afficher le répertoire courant
        print("You are in :", os.getcwd())

    elif user_input == "sf":
        # Lancer une recherche de fichiers
        search_file()

    elif user_input == "rf":
        # Lire un fichier
        file_path = input("Path to file: ")
        if check_file_readability(file_path):
            closed = False
            while not closed:
                closed = read_file(file_path)

    elif user_input == "exit":
        # Quitter le programme
        print("Goodbye ! o/\n")
        return True
    
    return False

def check_file_readability(file_path):
    # Vérifie si le fichier existe
    if not os.path.isfile(file_path):
        print(f"Le fichier {file_path} n'existe pas.")
        return False
    
    # Vérifie les permissions de lecture
    try:
        with open(file_path, 'r') as f:
            pass  # Ouvre et ferme immédiatement pour vérifier
        return True
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return False

def read_file(file_path):
    # Demander une commande à l'utilisateur (head, display, close)
    user_command = input("Enter command (head/display/close): ").strip().lower()

    if user_command == "head":
        # Afficher les 10 premières lignes
        with open(file_path, 'r') as f:
            for i in range(10):
                line = f.readline()
                if line == '':
                    break  # Fin du fichier atteinte
                print(line.strip())

    elif user_command == "display":
        try:
            # Demander le numéro de ligne de départ
            start_line = int(input("Enter the starting line number: "))
            with open(file_path, 'r') as f:
                for i, line in enumerate(f, 1):
                    if i >= start_line:
                        print(line.strip())
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    elif user_command == "close":
        print("Closing the file.")
        return True  # Indique que le fichier est fermé
    
    else:
        print("Commande non reconnue.")
    
    return False  # Continue tant que l'utilisateur ne ferme pas le fichier

def search_file(search_pattern):
    # chemin complet
    full_search_pattern = os.path.join(os.getcwd(),search_pattern) 
    
   
    files_found = glob.glob(full_search_pattern, recursive=True)
    """
    if files_found:
        print("Files found:")
        for file in files_found:
             print(file)
    else:
        print("No files found matching the pattern:", search_pattern)

    """
    
    return files_found
