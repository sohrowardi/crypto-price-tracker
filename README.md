# Top 10 Cryptocurrencies Viewer

## Overview
This Python application fetches and displays the current top 10 cryptocurrencies by market cap in a simple GUI. It uses the CryptoCompare API to retrieve cryptocurrency data and Tkinter for the graphical interface.

## Features
- Fetches the top 10 cryptocurrencies by market cap.
- Displays each cryptocurrency's name, symbol, and current price in USD.
- Shows the logo for each cryptocurrency next to its details.

## Requirements
- Python 3.x
- `requests` library
- `tkinter` library
- `PIL` library

## Installation
To run this application, you will need to install the required libraries if you haven't already. You can install them using pip:

```bash
pip install requests
pip install Pillow
```

### Usage
To start the application, run the following command in your terminal:

```bash
python top_10_crypto_viewer.py
```

The GUI will display the top 10 cryptocurrencies with their logos, names, symbols, and current prices in USD.

## API Reference
This application uses the CryptoCompare API to fetch the latest cryptocurrency data. For more information about the API, visit: https://min-api.cryptocompare.com/documentation