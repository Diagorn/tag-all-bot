import configure as conf
import utils.telegram_utils as utils

bot = conf.bot


@bot.message_handler(commands=['start'])
def start(message):
    utils.send_start(bot, message.chat.id)


@bot.message_handler(commands=['faq'])
def faq(message):
    utils.send_processing(bot, message.chat.id)
    # todo send kafka event
    bot.register_next_step_handler(message, faq_category_handler)


def faq_category_handler(message):
    if not message.text.is_numeric():
        bot.send_message(message.chat.id, 'Пожалуйста, выберите номер категории вопроса')
        bot.register_next_step_handler(message, faq_category_handler)
        return

    utils.send_processing(bot, message.chat.id)
    # todo send kafka event
    bot.register_next_step_handler(message, faq_question_handler)


def faq_question_handler(message):
    if not message.text.is_numeric():
        bot.send_message(message.chat.id, 'Пожалуйста, выберите номер категории вопроса')
        bot.register_next_step_handler(message, faq_category_handler)
        return

    utils.send_processing(bot, message.chat.id)
    # todo send kafka event
