from aiogram import html
from aiogram.types import Message

async def start_handler(message: Message) -> None:
    """
    Обработчик команды `/start`
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")