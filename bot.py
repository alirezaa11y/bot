from robka import Robot
from robka.context import Message
import requests

bot = Robot("توکن ربات خود را بزارید اینجا") 

@bot.on_message()
def handle(bot, message: Message):
    text = message.text.strip()
    
    if text == "/start":
        message.reply("✨ به ربات هوش مصنوعی خوش آمدید!\n💭 لطفاً پیام خود را ارسال کنید:")
        return
    
    sent = message.reply("🔍 در حال پردازش...")
    
    try:
        response = requests.get(f"https://hoshi-app.ir/api/chat-gpt.php?text={text}")
        if response.status_code == 200:
            result = response.json().get("result") or response.json().get("Result")
            reply_text = result if result else "پاسخی دریافت نشد"
        else:
            reply_text = "⚠️ خطا در ارتباط با سرور"
    except:
        reply_text = "⚠️ خطا در ارتباط با سرور"
    
    bot.edit_message_text(message.chat_id, sent["data"]["message_id"], reply_text)

print('فعال شدم')
bot.run()
