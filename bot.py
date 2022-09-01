from aiogram.utils import executor

import admins
from create_bot import dp, bot
from aiogram import types
import keyboard_main
from data_base import sql_db
from client import *
from admins import *

async def on_startup(_):
    print("Папа в здании")
    sql_db.db_start()

@dp.callback_query_handler(text="в начало")
@dp.message_handler(lambda message: "в начало" in message.text.lower())
async def salam(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIHRGMLJhCchUeJOxUi85ASQ0wy1pXOAAKNqjEbh4xZRN1YiXXKQzlcAQADAgADcwADKQQ")
    if message.from_user.id in admins.amdins:
        await bot.send_message(message.from_user.id, "Салам, родной",
                               reply_markup=keyboard_main.kb_mainwindow_admin)
    else:
        await bot.send_message(message.from_user.id, "Выбери категорию",
                               reply_markup=keyboard_main.kb_mainwindow)

@dp.message_handler(lambda message: "start" in message.text.lower())
async def start(message: types.Message):
    await bot.send_video(message.from_user.id, "BAACAgIAAxkBAAIKJmMLfIUGuimxS-DTlsb5cqSr1WsdAAL0IwAC5RZQSC7-V5eS635sKQQ")
    if message.from_user.id in admins.amdins:
        await bot.send_message(message.from_user.id, "Салам, родной",
                               reply_markup=keyboard_main.kb_mainwindow_admin)
    else:
        await bot.send_message(message.from_user.id, "Здравствуй, дорогой друг!\nВыбери категорию, нажав на соответствующую кнопку",
                               reply_markup=keyboard_main.kb_mainwindow)
        await sql_db.user_add(message)

@dp.message_handler(lambda message: "контакты" in message.text.lower())
async def kontakts(message: types.Message):
    await bot.send_message(message.from_user.id, "Телефон нашего кальян бара - 979-474\nInstagramm - https://instagramm.com/"
                                                 "hookah.boss.tsk", reply_markup=keyboard_main.ikb_main)

@dp.message_handler(lambda message: "адрес" in message.text.lower())
async def adress(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         "AgACAgIAAxkBAAMpYwM4FFUdRYIKwVXAvd2mB-FUIA4AAnO8MRsjbiFIqwxy4U3H17YBAAMCAANzAAMpBA")
    await bot.send_photo(message.from_user.id,
                         "AgACAgIAAxkBAAOBYwNG9ND71xaAYMnyGqejFPWq0WoAApm8MRsjbiFITn9RsxPszhUBAAMCAANzAAMpBA")
    await bot.send_message(message.from_user.id, "Наш уютный кальянный бар расположен по адресу: г. Томск, \nул. "
                                                 "19й Гвардейской дивизии, д. 11/1 (со стороно общежития ТУСУР)", reply_markup=keyboard_main.ikb_main)

@dp.message_handler(lambda message: "режим работы" in message.text.lower())
async def time(message: types.Message):
    await bot.send_message(message.from_user.id, "Кальянный бар Hookah Boss открыт для гостей ежедневно с 15.00 до 02.00", reply_markup=keyboard_main.ikb_main)

@dp.callback_query_handler(text="О нашем баре")
@dp.message_handler(lambda message: "о нашем баре" in message.text.lower())
async def about(message: types.Message):
    await bot.send_message(message.from_user.id, "Наш бар расположен в Кировском районе города Томска в пешей доступности от студенческих общежитий"
                                                 " ТГУ и ТУСУР. В баре царит дружеская атмосфера, уютный лаунж исполнен в теплых тонах.\n Ты можешь ознакомиться с нашими "
                                                 "мастерами и интерьером зала.", reply_markup=keyboard_main.kb_ourbar)
    await bot.send_message(message.from_user.id,
                           text="Выбери категорию", reply_markup=keyboard_main.ikb_main)


@dp.message_handler(lambda message: "интерьер" in message.text.lower())
async def interier(message: types.Message):
    await bot.send_message(message.from_user.id, "Фото зала нашего уютного заведения")
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIHSmMLJxX4K5pgk7TJLpZAK5Yetm-7AAKQqjEbh4xZRFMcFaT8BeoxAQADAgADcwADKQQ")
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIHSGMLJxBmZ2pp3k9ObsCGHLuEjfleAAKPqjEbh4xZROqILbVYUFa9AQADAgADcwADKQQ")
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIHRmMLJwt7RDzbeWNioQNWwTmVQkRYAAKOqjEbh4xZRCKUQdbniC-6AQADAgADcwADKQQ", reply_markup=
                           keyboard_main.ikb_main)

@dp.message_handler(lambda message: "наши мастера" in message.text.lower())
async def masters(message: types.Message):
    await bot.send_message(message.from_user.id, "Наши доблестные мастера кальянного дела", reply_markup=
                           keyboard_main.kb_who_at_work)
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIH82MLNtpvLh0qdVsz8OgqwX5YYSRXAAKfqjEbh4xZRGhiN7Q_NpHPAQADAgADcwADKQQ")
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIH9WMLNt2WU_Pb3ZfSRwFL16qYnaQcAAKgqjEbh4xZRJadfWrFRo6dAQADAgADcwADKQQ")
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIH92MLNuKURP5h6HRjXCtkr2Q3jNnoAAKhqjEbh4xZRIGh1HIpaqQDAQADAgADcwADKQQ")
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIH-WMLNuWNKJfcLbikQMIk_a5EWUcoAAKiqjEbh4xZRGU6SXr5esh2AQADAgADcwADKQQ", reply_markup=
                           keyboard_main.ikb_main)


@dp.callback_query_handler(text="Услуги нашего заведения")
@dp.message_handler(lambda message: "услуги нашего заведения" in message.text.lower())
async def positions(message: types.Message):
    await bot.send_message(message.from_user.id, "Развлечения на любой вкус", reply_markup=keyboard_main.kb_uslugi)
    await bot.send_message(message.from_user.id,
                           text="Выбери категорию", reply_markup=keyboard_main.ikb_main)
"""@dp.message_handler(lambda message: "забронировать стол" in message.text.lower())
async def stol(message: types.Message):
    await bot.send_message(message.from_user.id, "тут будет раздел с бронью стола")"""

@dp.message_handler(lambda message: "кальянные радости" in message.text.lower())
async def hookah(message: types.Message):
    await bot.send_message(message.from_user.id, "Дымное удовольствие на любой вкус")
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIHq2MLKtej1O1nlx_44ZISLr7N09dPAAKVqjEbh4xZRE9vjjXSlpZmAQADAgADcwADKQQ")
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIH3mMLL6uxfy05VAsixmbOoE7P9wGVAAKZqjEbh4xZRAvHqkeu-ls2AQADAgADcwADKQQ",
                         "DarkSide - 500 рублей")
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIHp2MLKsNyDFcwlCiCk5H8WqUihBjOAAKTqjEbh4xZRCbl4_kVeY8QAQADAgADcwADKQQ",
                         "MustHave - 500 рублей")
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIHzGMLLn347bf3jm8zKIJL2pTLTCacAAKWqjEbh4xZRHG8niV1CwLKAQADAgADcwADKQQ",
                         "BlackBurn - 500 рублей")
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIHzmMLLn90_1q45AUXT50fBx1i_wjfAAKXqjEbh4xZRG5tSXb5o_8yAQADAgADcwADKQQ",
                         "Daily Hookah - 500 рублей")
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIH0GMLLoP07dKtevLqjhXUUTo5NdfhAAKYqjEbh4xZRMOiXqaRCFkhAQADAgADcwADKQQ",
                         "Duft - 500 рублей")
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIHpWMLKr5M2XRRyzszuqaB4VUL31IOAAKSqjEbh4xZRLNDA-9lCZGEAQADAgADcwADKQQ",
                         "Brusko - 500 рублей")
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIHo2MLKrlUx5BAn3VSVjQPYM1CCWtBAAKRqjEbh4xZRL407FUTe65cAQADAgADcwADKQQ",
                         "Tangiers - 600 рублей", reply_markup=keyboard_main.ikb_main)

@dp.message_handler(lambda message: "напитки и чаи" in message.text.lower())
async def drinks(message: types.Message):
    await bot.send_message(message.from_user.id, "В нашем баре имеются  прохладительные напитки в широком ассортименте,"
                                                 " а также вкуснейшие чаи", reply_markup=keyboard_main.kb_bar)
    await bot.send_message(message.from_user.id, "Выбери категорию", reply_markup=keyboard_main.ikb_uslugi)

@dp.message_handler(lambda message: "чаи" in message.text.lower())
async def teas(message: types.Message):
    await bot.send_video(message.from_user.id,
                         "BAACAgIAAxkBAAIJ32MLea7bLS4YcK_iCoU8c4m6h3YbAAIOIQACzXRZSBmT61xwKIG4KQQ")
    await bot.send_message(message.from_user.id, "Вкуснейшие чаи: Сладкий апельсин, Клубника со сливками, Ягодный калейдоско, "
                                                 "Малина со сливками, Молочный улун, Классический черный - 200 рублей за чайник",
                           reply_markup=keyboard_main.ikb_main)

@dp.message_handler(lambda message: "алкоголь и еда" in message.text.lower())
async def alkohol(message: types.Message):
    await bot.send_message(message.from_user.id, "В нашем заведении действует пробковый сбор 100 рублей с каждой бутылки.\n"
                                                 "Также Ты можешь принести с собой любую еду", reply_markup=keyboard_main.ikb_uslugi)

@dp.message_handler(lambda message: "прохладительные напитки" in message.text.lower())
async def colla(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIH6WMLMPE2pXkNqIYMEYV-Gl2AS0g0AAKbqjEbh4xZRGBA0Qc7obgiAQADAgADcwADKQQ",
                         "В нашем баре представлен широкий выбор прохладительных напитков:\n"
                         "Баночки и гранатовый сок - 100 рублей\n"
                         "Напитки в стеклянных бутылках - 150 рублей\n"
                         "Энергетики - 200 рублей",
                         reply_markup=keyboard_main.ikb_main)

@dp.message_handler(lambda message: "развлечения в нашем баре" in message.text.lower())
async def enterteiment(message: types.Message):
    await bot.send_message(message.from_user.id, "В нашем баре вы можете провести свое свободное время,"
                                                 " совмещая порцию дымной радости с увлекательными играми "
                                                 "или с просмотром фильма/спортивной трансляции", reply_markup=keyboard_main.kb_razv)
    await bot.send_message(message.from_user.id, "Выбери категорию", reply_markup=keyboard_main.ikb_uslugi)

@dp.message_handler(lambda message: "Play Station" in message.text)
async def sp5(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIH62MLMbSKR4feiA8Tn29DzljOxULXAAKcqjEbh4xZRGuyfschXGcLAQADAgADcwADKQQ",
                         "В нашем баре ты можешь поиграть в UFC3, Mortal Kombat XI, FIFA 2019, FIFA 2020, GTA 5, God Of War",
                         reply_markup=keyboard_main.ikb_uslugi)

@dp.message_handler(lambda message: "спортивные трансляции и фильмы" in message.text.lower())
async def tranlations(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIH72MLMnJv3wbnhCUx7cv2j-lqnyk2AAKdqjEbh4xZRIrGYgABjCjmgQEAAwIAA3MAAykE")
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIH7WMLMm72NII0SqEhckhwATsGlIR0AAKOqjEbh4xZRCKUQdbniC-6AQADAgADcwADKQQ",
                         "Просмотр фильмов и спортивных трансляций на большом экране 75 дюймов",
                         reply_markup=keyboard_main.ikb_uslugi)

@dp.message_handler(lambda message: "настольные игры" in message.text.lower())
async def games(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIH8WMLMyu-cq0f2Hn0f-yhqqlJYiVNAAKeqjEbh4xZRBh1rUCCZMHxAQADAgADcwADKQQ",
                         "Карты, нарды, домино",
                         reply_markup=keyboard_main.ikb_uslugi)



@dp.message_handler(content_types = ['photo'])
async def any_shit(message : types.Message, a="nnn"):
    await bot.send_message(message.from_user.id, message.from_user.id)

@dp.message_handler(content_types = ['video'])
async def any_shit2(message : types.Message, a="nnn"):
    await bot.send_message(message.from_user.id, message.video.file_id)

registr_admin(dp)
registr_client(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True, on_startup = on_startup)
