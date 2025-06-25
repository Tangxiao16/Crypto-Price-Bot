import requests
import time

# === KONFIGURASI ===
TOKEN = '7456032535:AAGDNqDzYr-RDZ7Jef4c-nngobLtrsY3K7A'
CHAT_ID = '1260384319'
COINS = {
    'BTC': {'symbol': 'bitcoin', 'target': 1700000000},
    'INJ': {'symbol': 'injective-protocol', 'target': 200000},
    'RNDR': {'symbol': 'render-token', 'target': 70000},
    'FET': {'symbol': 'fetch-ai', 'target': 30000},
    'WLD': {'symbol': 'worldcoin-wld', 'target': 40000}
}

def get_price(symbol):
    try:
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=idr'
        r = requests.get(url)
        r.raise_for_status()
        return r.json()[symbol]['idr']
    except Exception as e:
        print(f'❌ Error ambil harga {symbol}: {e}')
        return 0

def send_telegram(message):
    try:
        url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
        payload = {'chat_id': CHAT_ID, 'text': message}
        r = requests.post(url, data=payload)
        print(f'📩 Telegram: {r.text}')
    except Exception as e:
        print(f'❌ Gagal kirim Telegram: {e}')

# Coba 1x dulu (bukan loop)
for name, info in COINS.items():
    current = get_price(info['symbol'])
    print(f'{name} sekarang: Rp{current:,}')
    if current >= info['target']:
        send_telegram(f'📈 {name} sudah mencapai target! Rp{current:,}')
    else:
        print(f'{name} belum mencapai target.')
