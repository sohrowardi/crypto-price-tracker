import requests
import tkinter as tk
from PIL import Image, ImageTk
import io

def get_top_10_crypto():
    url = 'https://min-api.cryptocompare.com/data/top/mktcapfull'
    parameters = {
        'limit': 10,
        'tsym': 'USD'
    }

    response = requests.get(url, params=parameters)
    data = response.json()

    top_10_crypto = []
    for crypto in data['Data']:
        crypto_info = {
            'name': crypto['CoinInfo']['FullName'],
            'symbol': crypto['CoinInfo']['Name'].upper(),
            'current_price': crypto['RAW']['USD']['PRICE'],
            'logo_url': f"https://www.cryptocompare.com{crypto['CoinInfo']['ImageUrl']}",
        }
        top_10_crypto.append(crypto_info)

    return top_10_crypto

def display_top_10_crypto_gui(top_10_crypto):
    root = tk.Tk()
    root.title("Top 10 Cryptocurrencies")

    for idx, crypto in enumerate(top_10_crypto):
        label_name = tk.Label(root, text=f"{crypto['name']} ({crypto['symbol']}) - ${crypto['current_price']} USD")
        label_name.grid(row=idx, column=0, padx=10, pady=5, sticky="w")

        response = requests.get(crypto['logo_url'])
        img_data = response.content
        img = Image.open(io.BytesIO(img_data))
        img.thumbnail((50, 50))
        photo = ImageTk.PhotoImage(img)
        label_logo = tk.Label(root, image=photo)
        label_logo.image = photo
        label_logo.grid(row=idx, column=1, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    top_10_crypto = get_top_10_crypto()
    display_top_10_crypto_gui(top_10_crypto)
