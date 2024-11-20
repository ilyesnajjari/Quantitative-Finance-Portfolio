import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Télécharger les données boursières
ticker = "AAPL"  # Symbole de l'action (Apple Inc.)
start_date = "2023-01-01"
end_date = "2023-06-01"

# Télécharger les données boursières de Yahoo Finance
stock_data = yf.download(ticker, start=start_date, end=end_date)

print(f"Downloading data for {ticker} from {start_date} to {end_date}...")
data = yf.download(ticker, start=start_date, end=end_date)

# Afficher les premières lignes des données
print("\nFirst rows of the data:")
print(data.head())

# Sauvegarder les données dans un fichier CSV
stock_data.to_csv('data/stock_data.csv')

# Calculer la moyenne mobile sur 20 jours
data['SMA_20'] = data['Close'].rolling(window=20).mean()

# Visualiser les cours de clôture et la moyenne mobile
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label="Closing Price")
plt.plot(data['SMA_20'], label="20-Day SMA", linestyle="--")
plt.title(f"{ticker} Stock Price and 20-Day SMA")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid()
plt.show()
