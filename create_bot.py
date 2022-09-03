from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token = "5412770175:AAERUo8-l44-Lhb6EYNdM_agXShHPvOzS4o")
dp = Dispatcher(bot, storage=storage)