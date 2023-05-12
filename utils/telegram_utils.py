import str_const as c


def send_start(bot, chat_id):
    bot.send_message(chat_id, c.start_msg)


def send_processing(bot, chat_id):
    bot.send_message(chat_id, c.processing_msg)
