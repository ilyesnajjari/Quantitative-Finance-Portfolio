import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import time
import csv
import os
import threading
import platform
from datetime import datetime

# Fonction pour récupérer les informations du joueur
def get_player_price_futwiz(player_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(player_url, headers=headers)
    
    if response.status_code != 200:
        print(f"Erreur lors de la récupération des données (Code HTTP : {response.status_code})")
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extraction du prix actuel
    price_num = soup.find("div", class_="price-num")
    current_price = price_num.text.strip() if price_num else "Prix actuel non disponible"
    
    # Extraction de la variation des prix
    price_compare = soup.find("div", class_="price-compare")
    price_change = price_compare.text.strip() if price_compare else "Variation non disponible"
    
    # Extraction de la gamme de prix
    price_range = soup.find("div", class_="pricerange")
    price_range_text = price_range.text.strip() if price_range else "Gamme de prix non disponible"
    
    # Extraction des prix supplémentaires
    extra_prices_section = soup.find("div", class_="extra-prices")
    extra_prices = []
    if extra_prices_section:
        extra_prices = [price.text.strip() for price in extra_prices_section.find_all("div")]
    
    return {
        "Prix actuel": current_price,
        "Variation des prix": price_change,
        "Gamme de prix": price_range_text,
        "Prix supplémentaires": extra_prices
    }

# Fonction pour envoyer une notification
def send_notification(message, title="Alerte Prix"):
    system = platform.system()

    if system == "Darwin":  # macOS
        os.environ["PATH"] += ":/usr/local/bin"
        os.system(f"terminal-notifier -message \"{message}\" -title \"{title}\"")
    elif system == "Windows":  # Windows
        os.system(f"msg * {message}")
    elif system == "Linux":  # Linux
        os.system(f'notify-send "{title}" "{message}"')
    else:
        print(f"[Notification] {title}: {message}")


# Fonction pour réinitialiser le fichier CSV si nécessaire
def reset_csv_if_needed():
    file_path = os.path.join("data", "price_history_player.csv")
    
    # Vérifier si le fichier existe
    if os.path.exists(file_path):
        # Lire la dernière date enregistrée
        with open(file_path, mode="r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)  # Lire toutes les lignes du fichier
            if len(rows) > 1:  # Si le fichier contient plus que l'entête
                last_row = rows[-1]  # Dernière ligne de données
                last_timestamp = last_row[-1]  # Dernière timestamp enregistrée
                last_date = datetime.strptime(last_timestamp, "%Y-%m-%d %H:%M:%S").date()
                current_date = datetime.today().date()
                
                # Si la date actuelle est différente de la dernière date enregistrée, réinitialiser le CSV
                if current_date != last_date:
                    print("Le fichier CSV sera réinitialisé.")
                    with open(file_path, mode="w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow(["Nom", "Prix actuel", "Variation des prix", "Gamme de prix", "Prix supplémentaires", "Timestamp"])
            else:
                # Si le fichier ne contient que l'entête, il est vide
                print("Le fichier CSV est vide, réinitialisation...")
                with open(file_path, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Nom", "Prix actuel", "Variation des prix", "Gamme de prix", "Prix supplémentaires", "Timestamp"])
    else:
        # Si le fichier n'existe pas, le créer et ajouter les entêtes
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Nom", "Prix actuel", "Variation des prix", "Gamme de prix", "Prix supplémentaires", "Timestamp"])

# Fonction pour suivre le prix et enregistrer dans le fichier CSV
def track_player_price(player_url, player_name, threshold_price):
    print(f"Essai d'accès à l'URL : {player_url}")
    
    player_info = get_player_price_futwiz(player_url)
    
    if player_info:
        current_price = player_info["Prix actuel"]
        print(f"Prix actuel : {current_price}")
        print(f"Variation des prix : {player_info['Variation des prix']}")
        print(f"Gamme de prix : {player_info['Gamme de prix']}")
        
        # Sauvegarder les données dans un CSV
        file_path = os.path.join("data", "price_history_player.csv")
        
        # Réinitialiser le CSV si nécessaire avant d'ajouter les nouvelles données
        reset_csv_if_needed()
        
        # Écriture des données dans le CSV
        with open(file_path, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([player_name, current_price, player_info["Variation des prix"], player_info["Gamme de prix"], ", ".join(player_info["Prix supplémentaires"]), time.strftime("%Y-%m-%d %H:%M:%S")])
        
        # Vérifier si le prix dépasse le seuil et envoyer une notification
        try:
            current_price_int = int(current_price.replace(",", "").replace("€", "").strip())
            if current_price_int > threshold_price:
                send_notification(f"Le prix du joueur {player_name} a dépassé le seuil ! Nouveau prix : {current_price}")
        except ValueError:
            print("Erreur : Le prix actuel n'est pas un nombre valide.")

# Fonction pour démarrer le suivi des prix dans un thread séparé
def start_tracking():
    # Récupérer les valeurs des champs d'entrée
    player_url = entry_url.get()
    player_name = entry_name.get()
    try:
        threshold_price = int(entry_threshold.get())
    except ValueError:
        messagebox.showerror("Erreur", "Le seuil de prix doit être un nombre valide.")
        return
    
    # Démarrer le suivi dans un thread séparé
    def update_price():
        while True:
            track_player_price(player_url, player_name, threshold_price)
            time.sleep(60)  # Attente de 2 secondes avant la prochaine mise à jour

    # Créer et démarrer le thread pour le suivi des prix
    tracking_thread = threading.Thread(target=update_price, daemon=True)
    tracking_thread.start()
    
    # Masquer la fenêtre principale après avoir lancé le suivi
    root.withdraw()

# Fonction pour gérer la fermeture de l'interface
def on_close():
    print("L'interface se ferme, mais le suivi continue en arrière-plan.")
    root.withdraw()  # Masque la fenêtre mais ne ferme pas le programme

# Création de l'interface graphique
root = tk.Tk()
root.title("Suivi des prix du joueur FUT")

# URL du joueur
label_url = tk.Label(root, text="URL du joueur:")
label_url.grid(row=0, column=0, padx=10, pady=10)
entry_url = tk.Entry(root, width=50)
entry_url.grid(row=0, column=1, padx=10, pady=10)

# Nom du joueur
label_name = tk.Label(root, text="Nom du joueur:")
label_name.grid(row=1, column=0, padx=10, pady=10)
entry_name = tk.Entry(root, width=50)
entry_name.grid(row=1, column=1, padx=10, pady=10)

# Seuil de prix
label_threshold = tk.Label(root, text="Seuil de prix (en EUR):")
label_threshold.grid(row=2, column=0, padx=10, pady=10)
entry_threshold = tk.Entry(root, width=50)
entry_threshold.grid(row=2, column=1, padx=10, pady=10)

# Bouton de soumission
submit_button = tk.Button(root, text="Lancer le suivi", command=start_tracking)
submit_button.grid(row=3, columnspan=2, pady=20)

# Lier la fermeture de la fenêtre à la fonction on_close
root.protocol("WM_DELETE_WINDOW", on_close)

# Affichage de l'interface
root.mainloop() 