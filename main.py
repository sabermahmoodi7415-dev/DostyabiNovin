from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio
from handlers.register import router as register_router
from config import TOKEN
from keyboards.main_menu import main_menu
print("TOKEN =", TOKEN)
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
    dp.include_router(register_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())