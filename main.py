from bs4 import BeautifulSoup
import requests

# Bitcoin
bitcoin_url = 'https://markets.businessinsider.com/currencies/btc-usd'
bitcoin_page = requests.get(bitcoin_url)
bitcoin_soup = BeautifulSoup(bitcoin_page.content, "html.parser")

# Etherium
ether_url = 'https://markets.businessinsider.com/currencies/eth-usd'
ether_page = requests.get(ether_url)
ether_soup = BeautifulSoup(ether_page.content, "html.parser")

# Tether
tether_url = 'https://markets.businessinsider.com/currencies/usdt-usd'
tether_page = requests.get(tether_url)
tether_soup = BeautifulSoup(tether_page.content, "html.parser")

# Binance Coin
binancec_url = 'https://markets.businessinsider.com/currencies/bnb-usd'
binancec_page = requests.get(binancec_url)
binancec_soup = BeautifulSoup(binancec_page.content, "html.parser")

# Solana
solana_url = 'https://markets.businessinsider.com/currencies/sol-usd'
solana_page = requests.get(solana_url)
solana_soup = BeautifulSoup(solana_page.content, "html.parser")

# variables 
bitcoin = bitcoin_soup.find('span', class_="price-section__current-value")
bitcoin = str(bitcoin)
bitcoin = bitcoin.replace('<span class="price-section__current-value">', "")
bitcoin = bitcoin.replace("</span>", "")
ether = ether_soup.find('span', class_="price-section__current-value")
ether = str(ether)
ether = ether.replace('<span class="price-section__current-value">', "")
ether = ether.replace("</span>", "")
tether = tether_soup.find('span', class_="price-section__current-value")
tether = str(tether)
tether = tether.replace('<span class="price-section__current-value">', "")
tether = tether.replace("</span>", "")
binancec = binancec_soup.find('span', class_="price-section__current-value")
binancec = str(binancec)
binancec = binancec.replace('<span class="price-section__current-value">', "")
binancec = binancec.replace("</span>", "")
solana = solana_soup.find('span', class_="price-section__current-value")
solana = str(solana)
solana = solana.replace('<span class="price-section__current-value">', "")
solana = solana.replace('</span>', "")


print("\n")
print("Prices of Crypto in Real Time (USD)\n", "\n")

print(f"Bitcoin: ${bitcoin}")
print(f"Ethereum: ${ether}")
print(f"Tether: ${tether}")
print(f"BinanceCoin: ${binancec}")
print(f"Solana: ${solana}")
print("\n")
