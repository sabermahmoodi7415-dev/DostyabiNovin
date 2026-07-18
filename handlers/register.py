from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.register import RegisterState

router = Router()


@router.message(Command("register"))
async def register(message: Message, state: FSMContext):
    await state.set_state(RegisterState.first_name)

    await message.answer(
        "🌹 به بخش ثبت نام خوش آمدید.\n\n"
        "لطفاً نام خود را وارد کنید:"
    )