import telegram

telegram_token = "5829950008:AAF7s4iCEfjXTExRGK41PVkRg6hfrLVsLr4"
telegram_id = '1922469197'

def send_telegram_message(message):
    try:
        #텔레그램 메시지 발송
        bot = telegram.Bot(telegram_token)
        res = bot.sendMessage(chat_id=telegram_id, text=message)

        return res

    except Exception:
        raise

send_telegram_message("하이하이")

