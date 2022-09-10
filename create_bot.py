from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import token

storage = MemoryStorage()
bot = Bot(token = token.token)
dp = Dispatcher(bot, storage=storage)