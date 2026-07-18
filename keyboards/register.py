from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

gender_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👨 مرد"),
            KeyboardButton(text="👩 زن")
        ],
        [
            KeyboardButton(text="❌ لغو ثبت نام")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)