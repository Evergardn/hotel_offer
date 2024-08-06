from aiogram import html
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class BookingStates(StatesGroup):
    destination = State()
    date = State()
    duration = State()

async def start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!\nКуда вы хотите полететь отдыхать?")
    await state.set_state(BookingStates.destination)

async def process_destination(message: Message, state: FSMContext) -> None:
    if await state.get_state() == BookingStates.destination:
        await state.update_data(destination=message.text)
        await message.answer("Введите дату (например, 2024-08-01):")
        await state.set_state(BookingStates.date)

async def process_date(message: Message, state: FSMContext) -> None:
    if await state.get_state() == BookingStates.date:
        await state.update_data(date=message.text)
        await message.answer("На сколько дней вы хотите поехать?")
        await state.set_state(BookingStates.duration)

async def process_duration(message: Message, state: FSMContext) -> None:
    if await state.get_state() == BookingStates.duration:
        await state.update_data(duration=message.text)
        user_data = await state.get_data()
        
        destination = user_data['destination']
        date = user_data['date']
        duration = user_data['duration']
        
        flight_link = f"https://www.skyscanner.net/transport/flights/{destination.lower()}?adults=1&children=0&infants=0&cabinclass=economy&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home"
        hotel_link = f"https://www.booking.com/searchresults.html?ss={destination}&checkin_monthday={date.split('-')[2]}&checkin_year_month={date.split('-')[0]}-{date.split('-')[1]}&checkout_monthday={int(date.split('-')[2]) + int(duration)}&checkout_year_month={date.split('-')[0]}-{date.split('-')[1]}"

        links = [
            f"Flights: {flight_link}",
            f"Hotels: {hotel_link}"
        ]
        
        await message.answer(f"Спасибо! Вот несколько ссылок для вас:\n" + "\n".join(links))
        await state.clear()