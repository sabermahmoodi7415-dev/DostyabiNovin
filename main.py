from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio

from config import TOKEN
from keyboards.main_menu import main_menu

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🌹 به ربات دوستیابی نوین خوش آمدید.\n\n"
        "برای شروع روی دکمه زیر کلیک کنید.",
        reply_markup=main_menu
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())