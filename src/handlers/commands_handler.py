import logging
from aiogram import html
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class BookingStates(StatesGroup):
    destination = State()
    date = State()
    duration = State()

async def start_handler(message: Message, state: FSMContext) -> None:
    logging.info("Handling /start command")
    await message.answer(f"Hello, {message.from_user.full_name}!\nКуда вы хотите полететь отдыхать?")

    try:
        await state.set_state(BookingStates.destination)
        logging.info(f"Set state to {BookingStates.destination}")

    except Exception as e:
        logging.info(e)

async def process_destination(message: Message, state: FSMContext) -> None:
    logging.info(f"Processing date: {message.text}")
    current_state = await state.get_state()
    logging.info(f"Current state: {current_state}")

    if current_state == BookingStates.destination.state:
        # await state.update_data(destination=message.text)
        await message.answer("Введите дату (например, 2024-08-01):")
        await state.set_state(BookingStates.date)
        logging.info(f"Set state to {BookingStates.date}")
    else:
        logging.warning(f"Unexpected state: {current_state}")

async def process_date(message: Message, state: FSMContext) -> None:
    logging.info(f"Processing date: {message.text}")
    current_state = await state.get_state()
    logging.info(f"Current state: {current_state}")

    if current_state == BookingStates.date.state:
        await state.update_data(date=message.text)
        await message.answer("На сколько дней вы хотите поехать?")
        await state.set_state(BookingStates.duration)
        logging.info(f"Set state to {BookingStates.duration}")
    else:
        logging.warning(f"Unexpected state: {current_state}")