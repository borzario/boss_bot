from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

ib_main = InlineKeyboardButton(text="В начало", callback_data="в начало")

b_time = KeyboardButton("Режим работы")
b_adress = KeyboardButton("Адрес")
b_contacts = KeyboardButton("Контакты")
b_first = KeyboardButton("В начало")
b_usligi = KeyboardButton("Услуги нашего заведения")
b_about = KeyboardButton("О нашем баре")
kb_mainwindow = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mainwindow.row(b_usligi).row(b_about)

b_masters = KeyboardButton("Наши мастера")
b_interier = KeyboardButton("Интерьер")
ib_about = InlineKeyboardButton(text="Назад", callback_data="О нашем баре")
kb_ourbar = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ourbar.row(b_masters).row(b_interier).row(b_time, b_adress, b_contacts)
ikb_main = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).row(ib_main)
ikb_about = InlineKeyboardMarkup(row_width=1).row(ib_about)

b_hooka = KeyboardButton("Кальянные радости")
b_bar = KeyboardButton("Напитки и чаи")
b_razvlekuha = KeyboardButton("Развлечения в нашем баре")
b_stol = KeyboardButton("Забронировать стол")
kb_uslugi = ReplyKeyboardMarkup(resize_keyboard=True)
kb_uslugi.row(b_hooka, b_bar).row(b_razvlekuha).row(b_stol)

ib_uslugi = InlineKeyboardButton(text="Назад", callback_data="Услуги нашего заведения")
b_tea = KeyboardButton("Чаи")
b_cold = KeyboardButton("Прохладительные напитки")
b_alkfood = KeyboardButton("Алкоголь и еда")
kb_bar = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bar.row(b_tea, b_alkfood).row(b_cold).row(b_stol)
ikb_uslugi = InlineKeyboardMarkup(row_width=1).row(ib_uslugi, ib_main)

b_pl = KeyboardButton("Play Station")
b_trans = KeyboardButton("Спортивные трансляции и фильмы")
b_games = KeyboardButton("Настольные игры")
kb_razv = ReplyKeyboardMarkup(resize_keyboard=True)
kb_razv.row(b_pl, b_games).row(b_trans).row(b_stol)

b_nasmene = KeyboardButton("Я на смене")
b_bron_accapt = KeyboardButton("Подтвердить бронь")
kb_mainwindow_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mainwindow_admin.row(b_nasmene).row(b_bron_accapt)

b_cancel = KeyboardButton("Отмена")

kb_zakaz = ReplyKeyboardMarkup(resize_keyboard=True)
kb_zakaz.row(b_cancel).row(b_usligi)

b_who_at_work = KeyboardButton("Кто на смене?")
kb_who_at_work = ReplyKeyboardMarkup(resize_keyboard=True).row(b_who_at_work)

