# Stock Data Analysis

## Project Overview
This project focuses on downloading stock market data from Yahoo Finance using the `yfinance` library and performing basic data analysis with Python. The goal is to implement simple algorithms like moving averages and ARIMA models to analyze stock price trends. This repository is part of a broader portfolio showcasing skills in quantitative finance and Python programming.

## Features
- Download stock data from Yahoo Finance using the `yfinance` library.
- Perform basic data analysis, including calculating moving averages and implementing ARIMA models.
- Visualize stock data and analysis results with `matplotlib` and `seaborn`.
- Explore time-series forecasting for stock price predictions.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/ilyesnajjari/Quantitative-Finance-Portfolio.git
    ```

2. Navigate to the project folder:
    ```bash
    cd stock-data-analysis
    ```

3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:
    - **On macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```
    - **On Windows**:
      ```bash
      venv\Scripts\activate
      ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. To run the main script and start analyzing stock data, use:
    ```bash
    python scripts/stock_data_analysis.py
    ```

2. You can modify the script to download data for different stock symbols by updating the `symbol` variable.

## Dependencies

- `yfinance` for downloading stock market data.
- `pandas` for data manipulation and analysis.
- `matplotlib` for plotting graphs and visualizing data.
- `statsmodels` for statistical modeling, including ARIMA.
- `seaborn` for enhanced data visualization.

You can install all dependencies using the following command:
```bash
pip install -r requirements.txt


File Structure

stock-data-analysis/
│
├── data/                    # Dossier pour stocker les fichiers de données
│   └── stock_data.csv       # Exemple de fichier de données téléchargées (si nécessaire)
│
├── scripts/                 # Dossier contenant les scripts Python
│   └── stock_data_analysis.py  # Script principal d’analyse des données
│
├── requirements.txt         # Liste des dépendances
│
├── README.md                # Fichier de documentation pour décrire le projet
│
├── .gitignore               # Fichier pour ignorer certains fichiers ou dossiers dans Git
│
└── venv/                    # Dossier de l'environnement virtuel (exclu de Git)


License

This project is open-source and available under the MIT License.

License

This project is open-source and available under the MIT License.

