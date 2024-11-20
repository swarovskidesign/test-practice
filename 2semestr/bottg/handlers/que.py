import json
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from utils.states import Form

router = Router()

def save_to_json(data, filename='data.json'):
    try:
        with open(filename, 'r+', encoding='utf-8') as file:
            file_data = json.load(file)
            file_data.append(data)
            file.seek(0)
            json.dump(file_data, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([data], file, ensure_ascii=False, indent=4)

@router.message(Command("регистрация"))
async def fill_profile(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer("name")

@router.message(Form.name)
async def form_name(message: Message, state: FSMContext):
    name = message.text.strip()
    if name:
        await state.update_data(name = name)
        await state.set_state(Form.mail)
        await message.answer("mail")
    else:
        await message.answer("eshe raz name")

@router.message(Form.mail)
async def form_mail(message: Message, state: FSMContext):
    email = message.text.strip()
    await state.update_data(mail = email)
    await state.set_state(Form.id)
    await message.answer("id")

@router.message(Form.id)
async def form_id(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await state.update_data(id = user_id)
    await state.set_state(Form.phone)
    await message.answer("phone")

@router.message(Form.phone)
async def form_phone(message: Message, state: FSMContext):
    phone = message.text.strip()
    await state.update_data(phone = phone)
    user_data = await state.get_data()
    save_to_json(user_data)
    await message.answer("norm")
