import os
import telebot


bot = telebot.TeleBot("1969051592:AAFtyw2lD0u8K9EA5Pm3qp4_pOXiJ9MAoJg")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm VndGroup Chat Bot ๐Made by VndGroup")


@bot.message_handler(commands=["help"])
def send_message(message):
    bot.send_message(message.chat.id, "https://www.youtube.com/channel/UCL8PI42TZ_uaQWVVKUJx9Eg")

PM_START_TEXT = """
๐๐๐ก๐ก๐ค ๐ฉ๐๐๐ง๐, ๐'๐ข VndGroup Bot โจ
๐'๐ข ๐ ๐๐ค๐ฌ๐๐ง๐๐ช๐ก gr๏ฟฝ๐ค๐ช๐ฅ ๐ข๐๐ฃ๐๐๐๐ง ๐๐ค๐ฉ ๐๐๐ฉ๐ ๐พ๐ค๐ค๐ก ๐๐ค๐๐ช๐ก๐๐จ. ๐๐๐๐ ๐๐ฎ TEแฉแฐ Vnd Group
๐๐๐ฉ /help ๐ฉ๐ค ๐๐๐ฃ๐ ๐ข๐ฎ ๐ก๐๐จ๐ฉ ๐ค๐ ๐๐ซ๐๐๐ก๐๐๐ก๐ ๐๐ค๐ข๐ข๐๐ฃ๐๐จ ๐น
 
"""
buttons = [
    [
        InlineKeyboardButton(text="๐Owner", url="https://t.me/venuja_sadew"),
        InlineKeyboardButton(text="๐ฒ Simple", url="https://t.me/venuja_sadew"),
    ],
    [
        InlineKeyboardButton(text="๐ By", url="https://t.me/venuja_sadew"),
        InlineKeyboardButton(text="โ สแดสแด", url="https://t.me/venuja_sadew"),
    ],
    [
        InlineKeyboardButton(
            text="โ แดแดแด แดษดแดษช แด แดแดแดแดส แดแด สแดแดส ษขสแดแดแด โ", url="https://t.me/venuja_sadew"
        ),
    ],
]


ANKIVECTOR_IMG = "https://telegra.ph/file/75579c20520fc79f5b68d.jpg"


bot.polling()
