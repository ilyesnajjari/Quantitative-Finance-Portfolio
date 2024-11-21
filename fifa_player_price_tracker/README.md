# FUT Player Price Tracker

This project allows you to track the prices of players on the FUT (FIFA Ultimate Team) market by retrieving data from the Futwiz website. It records the prices in a CSV file and sends a notification if the price exceeds a defined threshold.

## Prerequisites

- Python 3.x
- The following Python libraries:
 - tkinter
 - requests
 - beautifulsoup4
 - csv
 - os
 - threading
 - platform
 - datetime

You can install the necessary dependencies using the requirements.txt file:
```bash
pip install -r requirements.txt
```

## Usage

1. Clone this repository to your local machine.
2. Navigate to the project directory:
```bash
    cd fifa_player_price_tracker
```
3. Run the track_prices.py script:
```bash
    python3 track_prices.py
```
```bash
    python track_prices.py
```
4. A graphical interface will open. Enter the player's URL, player name, and price threshold in credits. 
    Example URL: [URL](https://www.futwiz.com/en/fc25/player/sandro-tonali/19121)
5. Click "Start Tracking" to begin monitoring the player's price.

## Features

- Price Retrieval: The script retrieves current prices, price variation, price range, and additional prices from the player's Futwiz page.
- Data Logging: The data is saved in a CSV file (data/price_history_player.csv).
- Notifications: If the current price exceeds the defined threshold, a notification is sent.
Graphical Interface: A simple user interface to input the necessary information and start tracking.

## Project Structure
```
fifa_player_price_tracker/
├── data/
│   └── price_history_player.csv   # CSV file containing player price history
├── scripts/
│   └── track_prices.py            # Main script for the project
├── README.md                      # Project documentation
├── .gitignore                     # List of files to be ignored by Git
├── requirements.txt               # List of required dependencies
└── venv/                          # Python virtual environment
```

## Main Code

The main file of the project is track_prices.py, which contains the following functions:

- get_player_price_futwiz(player_url): Retrieves price information from the Futwiz page.
- send_notification(message, title="Price Alert"): Sends a notification based on the operating system.
- reset_csv_if_needed(): Resets the CSV file if necessary (e.g., if the date changes).
- track_player_price(player_url, player_name, threshold_price): Tracks the player's price and logs the data in the CSV file.
- start_tracking(): Starts tracking the prices in a separate thread.
- on_close(): Handles the closing of the graphical interface.

## Authors

Ilyes NAJJARI

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it as you wish.
