import time
import requests
import telegram

# Seu token e ID do Telegram
TELEGRAM_BOT_TOKEN = '7886005192:AAExBYx3YaXsXH4I71rePSdGThS7asmO93s'
TELEGRAM_CHAT_ID = '855971772'

# Inicializa o bot
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

# Guardar contratos já enviados
sent_tokens = set()

def fetch_new_tokens():
    url = 'https://client-api-2-phi.vercel.app/api/trending'
    response = requests.get(url)
    data = response.json()

    for token in data:
        address = token.get('address')
        name = token.get('name')
        twitter = token.get('twitter')
        telegram_link = token.get('telegram')

        if not address or not name:
            continue

        # Filtra os que só têm Twitter e Telegram
        if twitter and telegram_link and address not in sent_tokens:
            message = (
                f"🚀 Novo token lançado no Pump.fun!\n\n"
                f"🪙 Nome: {name}\n"
                f"📄 Contrato: {address}\n"
                f"🐦 Twitter: {twitter}\n"
                f"📢 Telegram: {telegram_link}"
            )
            bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
            sent_tokens.add(address)

if __name__ == "__main__":
    while True:
        try:
            fetch_new_tokens()
        except Exception as e:
            print(f"Erro ao buscar tokens: {e}")
        time.sleep(30)
