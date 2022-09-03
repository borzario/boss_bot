from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sql_db
import keyboard_main

amdins = [5097527515, 5483128301, 928163560, 968758461]

@dp.message_handler(lambda message: "я на смене" in message.text.lower())
async def smena(message: types.Message):
    await bot.send_message(message.from_user.id, "Красава, братка! Ебашим!")
    await sql_db.set_master(message)


class Brona(StatesGroup):
    sosta = State()

async def brona(message: types.Message):
    await bot.send_message(message.from_user.id, "Братан, введи номер брони")
    await Brona.sosta.set()


async def bronb(message: types.Message, state=FSMContext):
    user = await sql_db.bronselect(message)
    await bot.send_message(message.from_user.id, "Клиент уведомлен о подтверждении брони")
    await state.finish()
    await bot.send_message(user[0][0], "Столик забронирован, ждем вас на порцию дымной радости")


#запиливаем функцию отмены загрузки
#@dp.message_hendler(state = "*", commands = 'отмена')
#@dp.message_hendler(Text(equals = 'отмена', ignore_case = True), state = "*")
async def cancel(message : types.Message, state = FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK")


def registr_admin(dp: Dispatcher):
    dp.register_message_handler(brona, lambda message: "Подтвердить бронь" in message.text, state=None)
    dp.register_message_handler(cancel, state="*", commands='отмена')
    dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(bronb, state=Brona.sosta)