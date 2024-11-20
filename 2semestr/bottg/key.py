from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardRemove
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

kb = ReplyKeyboardMarkup (
    keyboard = [
        [
            KeyboardButton(text = "Регистрация"),
            KeyboardButton(text = "Эфиры")
        ],
        [
            KeyboardButton(text = "Мероприятия"),
            KeyboardButton(text = "Подарки")
        ]
    ],
    resize_keyboard = True
)

links = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = "danger tw", url = "https://www.twitch.tv/dangerlyoha"),
            InlineKeyboardButton(text = "danger tg", url = "tg://resolve?domain=dangerlyoha")
        ]
    ]
)

mero = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = "Городские", url = "https://afisha.yandex.ru/novosibirsk"),
            InlineKeyboardButton(text = "Репчик", url = "https://randomfest.ru/")
        ]
    ]
)

def profile(text: str | list):
    builder = ReplyKeyboardBuilder()

    if isinstance(text, str):
        text = [text]
    
    [builder.button(text=txt) for txt in text]
    return builder.as_markup()

rmk = ReplyKeyboardRemove()