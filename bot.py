import random
import os

from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = os.environ.get("STRELTSY_BOT_TOKEN")
print(TOKEN)

voice_reactions = [
    "Нахуй свои войсы, пиши текстом, дебилоид.",
    "Я не слушаю аудио короче твоего IQ. Пиши.",
    "Если войс меньше 15 сек — ты еблан. Понял? Отстань.",
    "Ещё один войс — и я тебя в чс брошу, как прошлого долбоёба.",
    "Мне насрать на твой голос. Текст. Или молчи.",
    "Я не твой секретарь, чтобы расшифровывать твоё мычание. Пиши.",
    "Войсы для ленивых мудаков. Не будь мудаком.",
    "Если ты не слепой — печатай. Если слепой — нахуй мне твой войс?",
    "Последний раз говорю: войсы = игнор. Выбери: текст или забвение.",
    "Скинул войс? Поздравляю, ты — говно. Исправляйся."
]


# Обработчик голосовых сообщений
async def handle_voice(update: Update, context):
    # Проверяем, что сообщение пришло из чата (не из лички)
    if update.message.chat.type in ('group', 'supergroup'):
        voice = update.message.voice
        user = update.effective_user

        print(f"Голосовое в чате {update.message.chat.title} (ID: {update.message.chat.id})")
        print(f"От: @{user.username} (ID: {user.id})")
        print(f"Длительность: {voice.duration} сек")

        if voice.duration < 15:
            await update.message.reply_text(random.choice(voice_reactions))
            await update.message.delete()


# Функция для команды /start
async def tag_all(update: Update, context):
    chat_id = update.effective_chat.id
    bot: Bot = context.bot

    # Получаем список участников чата
    members = bot.get_chat_member_count(chat_id)  # Это только количество, но не имена

    # Альтернативный способ (если бот админ и может получать список участников)
    try:
        # Получаем список участников (если бот админ)
        members_list = await bot.get_chat_administrators(chat_id)
        mentions = []

        for member in members_list:
            user = member.user
            if not user.is_bot:  # Исключаем ботов
                mentions.append(f"@{user.username}" if user.username else user.full_name)

        if mentions:
            await update.message.reply_text(" ".join(mentions))
        else:
            await update.message.reply_text("Не удалось собрать участников.")
    except Exception as e:
        print(f"Ошибка: {e}")
        await update.message.reply_text("У меня нет прав администратора для этого действия.")

# Создаем бота и добавляем обработчики
def main():
    app = Application.builder().token(TOKEN).build()

    # Хендлер для команды /start
    app.add_handler(CommandHandler("all", tag_all))

    # Хендлер для голосовых сообщений
    app.add_handler(MessageHandler(
        filters.VOICE, handle_voice
    ))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
