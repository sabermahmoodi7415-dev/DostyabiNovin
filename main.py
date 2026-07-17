from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("سلام 🌹\nبه ربات دوستیابی نوین خوش آمدید.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())