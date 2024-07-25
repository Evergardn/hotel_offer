from aiogram.types import Message

async def help_handler(message: Message) -> None:
    """
    Обработчик команды `/help`
    """
    await message.answer("This is the help message.")