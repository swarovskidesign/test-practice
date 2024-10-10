# у меня нету как таковой пагинации, потому что не разобрался куда ее тут пихнуть, ведь у меня, по сути, 4 кнопки
# также я не могу сделать так, чтобы код из que.py шел дальше, а не стопался на vvedi name
# из-за того, что код не идет дальше vvedi name, не записываются в джсон
# не смог понять, как разделить файлы, я пробовал, но не получилось
# если сможете помочь с этим беспорядком, помогите!

import asyncio
import random
import key

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from handlers import que

bot = Bot("7175306880:AAFKKIVKDSzgh6S-Pz4AkpZITJXCFA1IeQw")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"sup, {message.from_user.first_name}", reply_markup = key.kb)

@dp.message(Command("end"))
async def end(message: Message):
    await message.answer(f"bb, {message.from_user.first_name}")

@dp.message()
async def echo(message: Message):
    msg = message.text.lower()
    if msg == "регистрация":
        await que.fill_profile(message, dp.storage)
      
    elif msg == "эфиры":
        await message.answer("Трансляции", reply_markup = key.links)
    
    elif msg == "мероприятия":
        await message.answer("Концерты, мероприятия", reply_markup = key.mero)

    elif msg == "подарки":
        a = ["spacevk3783516372", "vkspace7179450381"]
        random_element = random.choice(a)
        await message.answer("ты пока не заслужил, но...")
        await asyncio.sleep(2)
        await message.answer(f"есть промокод в яндекс еду - {random_element}")


async def main():
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot)
    dp.include_router(
    que.router
)

if __name__ == "__main__":
    asyncio.run(main())