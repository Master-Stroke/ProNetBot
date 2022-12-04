from dispatcher import bot
from dispatcher import dp
import requests
from config import open_weather_token
from config import ADMIN_ID
from aiogram import Bot, types,executor,Dispatcher
import datetime
import json
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
import psutil
from bs4 import BeautifulSoup as BS
import time
from main_news import check_news_update
from aiogram import types
from aiogram.dispatcher.filters import AdminFilter, IsReplyFilter
from random import randint
import string
import utils

Year = int(datetime.datetime.now().strftime("%Y"))
Mounth = datetime.datetime.now().strftime("%B")
Dey = int(datetime.datetime.now().strftime("%d"))
Hour = int(datetime.datetime.now().strftime("%H"))
Minute = datetime.datetime.now().strftime("%M")
Dates = [Dey, Hour, Minute, Mounth, Year]
date = f"{Dates[4]}y {Dates[3]} {Dates[0]} {Dates[1]}:{Dates[2]}"

CHAT_ID = -1001547735237

def cpu ():
  cpu_per = int (psutil.cpu_percent (1))
  return cpu_per

@dp.message_handler(commands=["start", "help"], commands_prefix="!/")
async def start(message: types.Message):
    if message.chat.id == CHAT_ID:
        await message.reply("Привет! Я модератор Чата Програмистов\nВ етом чате ти можеж общаться с программистами и проходить квести!\nПожалуста следуй правилам чата!\nПравила чата /rules\nВсе команди бота /commands\nЕсли Ви увидели что пользователь не следует правилам чата в ответ на його собщенния напишите /report чтоби админи чата обратили вниманния на його собщенния!")
    if not message.chat.id == CHAT_ID:
        await message.reply("Привет, Я ProNetBot точнее модератор для IT чатов.\nТакже ты можеж добавить меня в свой чат.\nМои команди /commands\n\nПоддержка по боту: @MasterStroke777")

@dp.message_handler(commands = ["reply"])
async def repl(message: types.Message):
    if message.chat.id == CHAT_ID:
        if message.from_user.id == ADMIN_ID:
            await bot.send_message(int(message.text.split()[1]), message.text.replace(message.text.split()[1], "").replace("/reply", ""))

@dp.message_handler(commands=["channel"], commands_prefix="!/")
async def start(message: types.Message):
    await message.reply("Заходьте на Канал Программистов\nhttps://t.me/official_programmerchannel")

@dp.message_handler(commands=["me"], commands_prefix="!/")
async def welcome(message: types.Message):
    if message.from_user.username is None:
        await message.reply(f"Name - {message.from_user.full_name}\nID - {message.from_user.id}\n")
    else:
        await message.reply(f"Name - {message.from_user.full_name}\n"
                            f"ID - <code>{message.from_user.id}</code>\n"
                            f"Username - @{message.from_user.username}\n")

@dp.message_handler(commands=["my_username"], commands_prefix="!/")
async def id(message: types.Message):
    if message.from_user.username is None:
        await message.reply("У вас нету username!")
    await message.reply(f"Ваш username: @{message.from_user.username}")

@dp.message_handler(commands=["my_name"], commands_prefix="!/")
async def id(message: types.Message):
    await message.reply(f"Ваше имя: {message.from_user.full_name}")

@dp.message_handler(commands=["my_number"], commands_prefix="!/")
async def id(message: types.Message):
    await message.reply(f"Ваш номер: {message.from_user.number}")

@dp.message_handler(commands=["my_id"], commands_prefix="!/")
async def id(message: types.Message):
    await message.reply(f"Ваш ID: <code>{message.from_user.id}</code>")

@dp.message_handler(commands=["chat_id"], commands_prefix="!/")
async def chat(message: types.Message):
    await message.reply(f"ID чата: <code>{message.chat.id}</code>")

@dp.message_handler(commands=["dice"], commands_prefix="!/")
async def start(message: types.Message):
    await message.reply("🎲")

@dp.message_handler(commands=["bot"], commands_prefix="!/")
async def start(message: types.Message):
    await message.reply(f"\nБот запущен!\nПоследнее обновленния было: {date}.\nНагрузка на процессор хостинга: {cpu()}%")

@dp.message_handler(content_types=["new_chat_members"])
async def new_chat(message: types.Message):
    if message.chat.id == CHAT_ID:
        await message.reply("Добро пожаловать в чат!\nМои команди /commands")
    if not message.chat.id == CHAT_ID:
        await message.reply("Добро пожаловать в чат!\nМои команди /commands\n\nПоддержка по боту: @MasterStroke777")

@dp.message_handler(content_types=["left_chat_member"])
async def left_chat(message: types.Message):
    if message.chat.id == CHAT_ID:
       await message.reply("Пока!")
    if not message.chat.id == CHAT_ID:
        await message.delete()

@dp.message_handler(commands=["commands"], commands_prefix="!/")
async def start(message: types.Message):
    if message.chat.id == CHAT_ID:
        await message.reply("Команди бота:\nКоманди можно писать с префиксом ! и /\n/commands чтоби посмотреть все команди бота\n/rules Правила чата\n/start и /help для помощи по чату\n/report чтоби пожаловаться на пользователя для етого ответе на его собщенния командой /report\n/fresh_news Свежие новости в мире IT\n/last_fave_news Последние 5 новостей в мире IT\n/all_news Все новости в мире IT\n/weather Посмотреть погоду\n/usd Курс Доллара\n/eur Курс Евро\n/uah Курс Гривни\n/rub Курс Рубля\n/gbp Курс Фунта\n/pln КУрс Злотих\n/well ведите сначала первую валюту а потом вторую типа вот так: /well_usd uah и оно отобразить стоимость первой валюти в второй\n\nКоманди бота для админов чата:\n/msg чтоби писать от имени бота\n/mute мут пользователя\n/ban бан пользователя\n/tmute времмений мут\n/reply Писать в личку пользователю\n/kick удалить пользователя с групи\n/unmute размутить пользователя в групе\n/unban разбан пользователя в групе\n/pin Закрепить сообщенния\n/unpin Открепить сообщенния\n/del Удалить сообщенния")
    if not message.chat.id == CHAT_ID:
        await message.reply("Команди бота:\nКоманди можно писать с префиксом ! и /\n/commands чтоби посмотреть все команди бота\n/start и /help для помощи по чату\n/report чтоби пожаловаться на пользователя для етого ответе на его собщенния командой /report\n/fresh_news Свежие новости в мире IT\n/last_fave_news Последние 5 новостей в мире IT\n/all_news Все новости в мире IT\n/weather Посмотреть погоду\n/usd Курс Доллара\n/eur Курс Евро\n/uah Курс Гривни\n/rub Курс Рубля\n/gbp Курс Фунта\n/pln КУрс Злотих\n/well ведите сначала первую валюту а потом вторую типа вот так: /well_usd uah и оно отобразить стоимость первой валюти в второй\n\nКоманди бота для админов чата:\n/mute мут пользователя\n/ban бан пользователя\n/tmute времмений мут\n/kick удалить пользователя с групи\n/unmute размутить пользователя в групе\n/unban разбан пользователя в групе\n/pin Закрепить сообщенния\n/unpin Открепить сообщенния\n/del Удалить сообщенния")

#@dp.message_handler(commands=["site"], commands_prefix="!/")
#async def start(message: types.Message):
#    await message.answer("Заходьте на наш сайт Клондайк Программистов\nhttps://klondikeprogrammers.ga")

@dp.message_handler(commands=["bots"], commands_prefix="!/")
async def start(message: types.Message):
    await message.reply("Боти нашей компании:\n@see_weather_city_bot посмотреть погоду в любом городе мира\n@pro_moder_bot Модератор\n@bot_accountant_bot бухгалер бот\n@bot_qr_code_bot Генератор QR Code\n@bot_join_bot Авто прием заявок на вступленния в чат\n@search_photo_cats_bot рандомный поиск фото котов\n@search_photo_dog_bot рандомный поиск фото собак\n@botcaptchabot Генератор капчи\n@programmerchat_bot Модератор для IT чатов")

#@dp.message_handler(commands=["say"], commands_prefix="!/")
#async def start(message: types.Message):
#    await message.answer("Пожалуста следуйте правилам чата!\nПравила чата /rules\nВсе команди бота /commands\nЕсли Ви увидели что пользователь не следует правилам чата в ответ на його собщенния напишите /report чтоби админи обратили внимания на його собщенния!")

#@dp.message_handler(commands=["say1"], commands_prefix="!/")
#async def start(message: types.Message):
#   await message.answer("Общаемся на тему программирования и всего что с ним связано 👊\n\n🚫Ненормативная лексика запрещена\n🚫Спам запрещен\n\nПриятного общения 😊")

#@dp.message_handler(commands=["sayrep"], commands_prefix="!/")
#async def start(message: types.Message):
#    await message.answer("Участники чата, не забывайте про команду /report с помощю которой Вы можете обратить внимание администрации на нарушителя в чате")

# ban user
@dp.message_handler(is_chat_admin=True, commands=['ban'], commands_prefix="!/")
async def cmd_ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение")
        return

    user = await message.bot.get_chat_member(message.chat.id,
                                             message.reply_to_message.from_user.id)

    if message.reply_to_message.from_user.id == message.from_user.id:
        await message.reply("Нельзя забанить самого себя =)")
        return

    if user.is_chat_admin():
        await message.reply("Нельзя изменять права администраторов!")
        return

    user = message.reply_to_message.from_user
    if user.last_name is not None:
        await message.reply(f"Пользователь {user.first_name} {user.last_name} (@{user.username}) забанен навсегда!")
    else:
        await message.reply(f"Пользователь {user.first_name} (@{user.username}) забанен навсегда!")
    await message.bot.delete_message(message.chat.id, message.message_id)  # remove admin message
    await message.bot.kick_chat_member(chat_id=message.chat.id,
                                       user_id=message.reply_to_message.from_user.id
                                       )


@dp.message_handler(is_chat_admin=True, commands=["unban"], commands_prefix="!/")
async def cmd_unban(message: types.Message):
    # Check if command is sent as reply to some message
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение")
        return

    user = await message.bot.get_chat_member(message.chat.id,
                                             message.reply_to_message.from_user.id
                                             )
    if user.is_chat_admin():
        await message.reply("Нельзя изменять права администраторов")
        return

    user = message.reply_to_message.from_user
    if user.last_name is not None:
        await message.reply(f"Пользователь {user.first_name} {user.last_name} (@{user.username}) разбанен")
    else:
        await message.reply(f"Пользователь {user.first_name} (@{user.username}) разбанен")
    await message.bot.delete_message(message.chat.id, message.message_id)  # remove admin message
    await message.bot.unban_chat_member(chat_id=message.chat.id,
                                        user_id=message.reply_to_message.from_user.id)

# random mute chat member
@dp.message_handler(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP], commands=['dont_click_me'],
commands_prefix='!/')
async def mute_random(message: types.Message):
    now_time = int(time.time())
    replied_user_id = message.from_user.id
    replied_user = message.from_user.full_name
    random_m = randint(1, 10)
    await bot.restrict_chat_member(chat_id=message.chat.id, user_id=replied_user_id, can_send_messages=False,
                                   can_send_media_messages=False, can_send_other_messages=False,
                                   until_date=now_time + 60 * random_m)
    if not message.from_user.username == None:
        await message.reply(f"Пользователю @{message.reply_to_message.from_user.username} видан мут на рандомное число, {random_m} минут.")
    if message.from_user.username == None:
        await message.reply(f"Пользователю [<code>{message.from_user.id}</code>] <code>{message.from_user.full_name}</code> видан мут на рандомное число, {random_m} минут.")

# unmute user in chat
@dp.message_handler(is_chat_admin=True, commands="mute", commands_prefix="!/")
async def cmd_readonly(message: types.Message):
    # Check if command is sent as reply to some message
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение")
        return

    # Admins cannot be restricted
    user = await message.bot.get_chat_member(message.chat.id,
                                             message.reply_to_message.from_user.id
                                             )
    if user.is_chat_admin():
        await message.reply("Нельзя изменять права администраторов")
        return

    words = message.text.split()
    if len(words) > 1:  # !mute with arg
        restriction_time = utils.get_restriction_time(words[1])
        if not restriction_time:
            await message.reply(
                "Неправильный формат времени!\nИспользуйте число + символ m, h или d.\nНапример: <code>!mute 7d</code>"
            )
            return
    else:
        restriction_time = 86400 * 367

    now_time = int(time.time())

    await message.bot.restrict_chat_member(message.chat.id,
                                           message.reply_to_message.from_user.id,
                                           types.ChatPermissions(),
                                           until_date=now_time + restriction_time
                                           )

    user = message.reply_to_message.from_user
    if len(words) > 1:
            await message.reply(f"Пользователю {user.full_name} (@{user.username}) выдан мут на " + (
                "{restriction_time}").format(restriction_time=words[1]))
    else:
            await message.reply(
                f"Пользователю {user.full_name} (@{user.username}) выдан мут навсегда")


@dp.message_handler(is_chat_admin=True, commands="unmute", commands_prefix="!/")
async def cmd_unreadonly(message: types.Message):
    # Check if command is sent as reply to some message
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение")
        return

    user = await message.bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    if user.is_chat_admin():
        await message.reply("Нельзя изменять права администраторов!")
        return

    await message.bot.restrict_chat_member(message.chat.id,
                                           message.reply_to_message.from_user.id,
                                           types.ChatPermissions(
                                               can_send_messages=True,
                                               can_send_media_messages=True,
                                               can_send_polls=True,
                                               can_send_other_messages=True,
                                               can_add_web_page_previews=True,
                                               can_change_info=True,
                                               can_invite_users=True,
                                               can_pin_messages=True)
                                           )

    user = message.reply_to_message.from_user
    await message.reply(f"Пользователь {user.full_name} (@{user.username}) размучен")

# pin chat message
@dp.message_handler(AdminFilter(is_chat_admin=True), IsReplyFilter(is_reply=True),
                    chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP], commands=['pin'], commands_prefix='!/')
async def pin_message(message: types.Message):
    msg_id = message.reply_to_message.message_id
    await bot.pin_chat_message(message_id=msg_id, chat_id=message.chat.id)

@dp.message_handler(AdminFilter(is_chat_admin=True), IsReplyFilter(is_reply=False), commands=['pin'],
                    commands_prefix='!/', chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP])
async def ban(message: types.Message):
    await message.reply("Команда должна быть ответом на собщенния!")

# unpin chat message
@dp.message_handler(AdminFilter(is_chat_admin=True), IsReplyFilter(is_reply=True), commands_prefix='!/',
                    chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP], commands=['unpin'])
async def unpin_message(message: types.Message):
    msg_id = message.reply_to_message.message_id
    await bot.unpin_chat_message(message_id=msg_id, chat_id=message.chat.id)

@dp.message_handler(AdminFilter(is_chat_admin=True), IsReplyFilter(is_reply=False), commands=['unpin'],
                    commands_prefix='!/', chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP])
async def ban(message: types.Message):
    await message.reply("Команда должна бить ответом на собщенния!")

# delete user message
@dp.message_handler(AdminFilter(is_chat_admin=True), IsReplyFilter(is_reply=True), commands_prefix='!/',
                    chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP], commands=['del'])
async def delete_message(message: types.Message):
    msg_id = message.reply_to_message.message_id
    await bot.delete_message(chat_id=message.chat.id, message_id=msg_id)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

@dp.message_handler(AdminFilter(is_chat_admin=True), IsReplyFilter(is_reply=False), commands=['del'],
                    commands_prefix='!/', chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP])
async def ban(message: types.Message):
    await message.reply("Команда должна быть ответом на собщенния!")
# get chat admins list
@dp.message_handler(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP], commands=['admins'],
                    commands_prefix='!/')
async def get_admin_list(message: types.Message):
    admins_id = [(admin.user.id, admin.user.full_name) for admin in await bot.get_chat_administrators(
        chat_id=message.chat.id)]
    admins_list = []
    for ids, name in admins_id:
        admins_list.append("".join(f"[{name}]"))
    result_list = ""
    for admins in admins_list:
        result_list += "".join(admins) + '\n'
    await message.reply("Админи чата:\n" + result_list, parse_mode=types.ParseMode.MARKDOWN)

# report about spam or something else
@dp.message_handler(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP], commands=['report'],
                      commands_prefix='!/')
async def report_by_user(message: types.Message):
    msg_id = message.reply_to_message.message_id
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    username = message.from_user.username
    from_username = message.reply_to_message.from_user.username
    from_user_id = message.reply_to_message.from_user.id
    from_name = message.reply_to_message.from_user.full_name
    admins_list = [admin.user.id for admin in await bot.get_chat_administrators(chat_id=message.chat.id)]
    for adm_id in admins_list:
        try:
            await bot.send_message(text=f"🆘Жалоба в чате\nПользователь <code>{user_name}</code> [<code>{user_id}</code>] @{username}\nотправил жалобу на\n <code>{from_username}</code> [<code>{from_user_id}</code>] <code>{from_name}</code>\nПричина жалоби: {message.text[8:]}",
                                   chat_id=adm_id, disable_web_page_preview=True)
            await message.reply(f"Жалоба на пользователя @{message.reply_to_message.from_user.username}\nПричина: {message.text[8:]}\n\nОтправлено админам!")                       
        except:
            await bot.send_message(text=f"🆘Жалоба в чате\nПользователь <code>{user_name}</code> [<code>{user_id}</code>] @{username} отправил жалобу на <code>{from_username}</code> [<code>{from_user_id}</code>] <code>{from_name}</code>\nПричина жалоби: {message.text[8:]}",
                                   chat_id=adm_id, disable_web_page_preview=True)
            await message.reply(f"Жалоба на пользователя @{message.reply_to_message.from_user.username}\nПричина: {message.text[8:]}\nОтправлено админам!")                       

@dp.message_handler(commands=["rules"], commands_prefix="!/", chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP])
async def start(message: types.Message):
    if message.chat.id == CHAT_ID:
        await message.reply("Правила чата:\n🚫 Ненормативная лексика запрещена\n🚫Спам запрещен\n\nНе следуванния правил чата караеться баном или мутом!\nНезнание правил не освобождает вас от ответственности!\nЕсли Ви увидели что пользователь не следует правилам чата в ответ на його собщенния напишите /report чтоби админи обратили вниманния на його собщенния в чате!")

@dp.message_handler(commands=["msg"], commands_prefix="!/")
async def echo(message: types.Message):
 if message.chat.id == CHAT_ID:
  if not message.reply_to_message:  
       if '!msg' in message.text:
          await message.delete()
       if '/msg' in message.text:
          await message.delete()
       await message.answer(message.text[5:])
       await message.reply_to_message.from_user.id(message.text[5:])
  if message.reply_to_message:
    if '!msg' in message.text:
        await message.delete()
    if '/msg' in message.text:
        await message.delete()  
    await message.reply_to_message.reply(message.text[5:])

@dp.message_handler(commands=["well_usd"], commands_prefix="!/")
async def start(message: types.Message):
    first = f'{message.text[6:]}'
    second = f'{message.text[10:]}'
    url = f'https://www.currency.me.uk/convert/usd/{second}'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    well = soup.find("span", { "class" : "mini ccyrate" }).text
    res = f"{well}"
    await message.reply(res) 

@dp.message_handler(commands=["well_eur"], commands_prefix="!/")
async def start(message: types.Message):
    second = f'{message.text[10:]}'
    url = f'https://www.currency.me.uk/convert/eur/{second}'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    well = soup.find("span", { "class" : "mini ccyrate" }).text
    res = f"{well}"
    await message.reply(res) 

@dp.message_handler(commands=["well_uah"], commands_prefix="!/")
async def start(message: types.Message):
    second = f'{message.text[10:]}'
    url = f'https://www.currency.me.uk/convert/uah/{second}'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    well = soup.find("span", { "class" : "mini ccyrate" }).text
    res = f"{well}"
    await message.reply(res) 

@dp.message_handler(commands=["well_rub"], commands_prefix="!/")
async def start(message: types.Message):
    second = f'{message.text[10:]}'
    url = f'https://www.currency.me.uk/convert/rub/{second}'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    well = soup.find("span", { "class" : "mini ccyrate" }).text
    res = f"{well}"
    await message.reply(res)            

@dp.message_handler(commands=["well_gbp"], commands_prefix="!/")
async def start(message: types.Message):
    second = f'{message.text[10:]}'
    url = f'https://www.currency.me.uk/convert/gbp/{second}'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    well = soup.find("span", { "class" : "mini ccyrate" }).text
    res = f"{well}"
    await message.reply(res)    

@dp.message_handler(commands=["well_pln"], commands_prefix="!/")
async def start(message: types.Message):
    second = f'{message.text[10:]}'
    url = f'https://www.currency.me.uk/convert/pln/{second}'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    well = soup.find("span", { "class" : "mini ccyrate" }).text
    res = f"{well}"
    await message.reply(res)                            

@dp.message_handler(commands=["uah"], commands_prefix="!/")
async def start(message: types.Message):
    url = 'https://www.currency.me.uk/convert/uah/usd'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    usd = soup.find("span", { "class" : "mini ccyrate" }).text

    url = 'https://www.currency.me.uk/convert/uah/rub'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    rub = soup.find("span", { "class" : "mini ccyrate" }).text 

    url = 'https://www.currency.me.uk/convert/uah/eur'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    eur = soup.find("span", { "class" : "mini ccyrate" }).text 

    url = 'https://www.currency.me.uk/convert/uah/gbp'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    gbp = soup.find("span", { "class" : "mini ccyrate" }).text 

    url = 'https://www.currency.me.uk/convert/uah/pln'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    pln = soup.find("span", { "class" : "mini ccyrate" }).text    

    res = f"UAH🇺🇦\n🇺🇸{usd}\n🇷🇺{rub}\n🇪🇺{eur}\n🇬🇧{gbp}\n🇵🇱{pln}"
    await message.reply(res)

@dp.message_handler(commands=["rub"], commands_prefix="!/")
async def start(message: types.Message):
    url = 'https://www.currency.me.uk/convert/rub/usd'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    usd = soup.find("span", { "class" : "mini ccyrate" }).text

    url = 'https://www.currency.me.uk/convert/rub/uah'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    uah = soup.find("span", { "class" : "mini ccyrate" }).text 

    url = 'https://www.currency.me.uk/convert/rub/eur'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    eur = soup.find("span", { "class" : "mini ccyrate" }).text 

    url = 'https://www.currency.me.uk/convert/rub/gbp'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    gbp = soup.find("span", { "class" : "mini ccyrate" }).text 

    url = 'https://www.currency.me.uk/convert/rub/pln'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    pln = soup.find("span", { "class" : "mini ccyrate" }).text    

    res = f"RUB🇷🇺\n🇺🇸{usd}\n🇺🇦{uah}\n🇪🇺{eur}\n🇬🇧{gbp}\n🇵🇱{pln}"
    await message.reply(res) 

@dp.message_handler(commands=["gbp"], commands_prefix="!/")
async def start(message: types.Message):
    url = 'https://www.currency.me.uk/convert/gbp/usd'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    usd = soup.find("span", { "class" : "mini ccyrate" }).text

    url = 'https://www.currency.me.uk/convert/gbp/rub'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    rub = soup.find("span", { "class" : "mini ccyrate" }).text 

    url = 'https://www.currency.me.uk/convert/gbp/eur'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    eur = soup.find("span", { "class" : "mini ccyrate" }).text 

    url = 'https://www.currency.me.uk/convert/gbp/uah'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    uah = soup.find("span", { "class" : "mini ccyrate" }).text 

    url = 'https://www.currency.me.uk/convert/gbp/pln'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    pln = soup.find("span", { "class" : "mini ccyrate" }).text    

    res = f"GBP💷\n🇺🇸{usd}\n🇷🇺{rub}\n🇪🇺{eur}\n🇺🇦{uah}\n🇵🇱{pln}"
    await message.reply(res)

@dp.message_handler(commands=["pln"], commands_prefix="!/")
async def start(message: types.Message):
    url = 'https://www.currency.me.uk/convert/pln/usd'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    usd = soup.find("span", { "class" : "mini ccyrate" }).text

    url = 'https://www.currency.me.uk/convert/pln/rub'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    rub = soup.find("span", { "class" : "mini ccyrate" }).text 

    url = 'https://www.currency.me.uk/convert/pln/eur'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    eur = soup.find("span", { "class" : "mini ccyrate" }).text 

    url = 'https://www.currency.me.uk/convert/pln/uah'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    uah = soup.find("span", { "class" : "mini ccyrate" }).text 

    url = 'https://www.currency.me.uk/convert/pln/gbp'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    gbp = soup.find("span", { "class" : "mini ccyrate" }).text    

    res = f"PLN🇵🇱\n🇺🇸{usd}\n🇷🇺{rub}\n🇪🇺{eur}\n🇺🇦{uah}\n🇬🇧{gbp}"
    await message.reply(res)

@dp.message_handler(commands=["usd"], commands_prefix="!/")
async def start(message: types.Message):
    url = 'https://www.currency.me.uk/convert/usd/uah'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    uah = soup.find("span", { "class" : "mini ccyrate" }).text

    url = 'https://www.currency.me.uk/convert/usd/rub'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    rub = soup.find("span", { "class" : "mini ccyrate" }).text 

    url = 'https://www.currency.me.uk/convert/usd/eur'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    eur = soup.find("span", { "class" : "mini ccyrate" }).text 

    url = 'https://www.currency.me.uk/convert/usd/gbp'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    gbp = soup.find("span", { "class" : "mini ccyrate" }).text 

    url = 'https://www.currency.me.uk/convert/usd/pln'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    pln = soup.find("span", { "class" : "mini ccyrate" }).text    

    res = f"USD💵\n🇺🇦{uah}\n🇷🇺{rub}\n🇪🇺{eur}\n🇬🇧{gbp}\n🇵🇱{pln}"
    await message.reply(res)

@dp.message_handler(commands=["eur"], commands_prefix="!/")
async def start(message: types.Message):
    url = 'https://www.currency.me.uk/convert/eur/uah'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    uah = soup.find("span", { "class" : "mini ccyrate" }).text

    url = 'https://www.currency.me.uk/convert/eur/rub'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    rub = soup.find("span", { "class" : "mini ccyrate" }).text 

    url = 'https://www.currency.me.uk/convert/eur/usd'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    usd = soup.find("span", { "class" : "mini ccyrate" }).text 

    url = 'https://www.currency.me.uk/convert/eur/gbp'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    gbp = soup.find("span", { "class" : "mini ccyrate" }).text 

    url = 'https://www.currency.me.uk/convert/eur/pln'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    pln = soup.find("span", { "class" : "mini ccyrate" }).text 

    res = f"EUR💶\n🇺🇦{uah}\n🇷🇺{rub}\n🇺🇸{usd}\n🇬🇧{gbp}\n🇵🇱{pln}"
    await message.reply(res)

@dp.message_handler(commands=["all_news"], commands_prefix="!/")
async def get_all_news(message: types.Message):
    with open("news.json") as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items()):
        news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
            f"{hlink(v['article_title'], v['article_url'])}"
        await message.answer(news)

@dp.message_handler(commands="last_fave_news")
async def get_last_five_news(message: types.Message):
    with open("news.json") as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items())[-5:]:
        news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
            f"{hlink(v['article_title'], v['article_url'])}"

        await message.answer(news)

@dp.message_handler(commands=["fresh_news"], commands_prefix="!/")
async def get_fresh_news(message: types.Message):
    fresh_news = check_news_update()

    if len(fresh_news) >= 1:
        for k, v in sorted(fresh_news.items()):
            news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
                f"{hlink(v['article_title'], v['article_url'])}"

            await message.answer(news)
    else:
        await message.answer("Пока нет свежих новостей...")

@dp.message_handler(commands=["weather"], commands_prefix="!/")
async def get_fresh_news(message: types.Message): 
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }
    r = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={message.text[9:]}&appid={open_weather_token}&units=metric"
    )
    data = r.json()

    city = data["name"]
    cur_weather = data["main"]["temp"]

    weather_description = data["weather"][0]["main"]
    if weather_description in code_to_smile:
        wd = code_to_smile[weather_description]
    else:
        wd = "Посмотри в окно, не пойму что там за погода!"

    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind = data["wind"]["speed"]
    sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
    length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

    msgw = await message.reply(
            f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
            f"Хорошего дня!"
            )       

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def filter_mes(message: types.Message):
    await bot.send_message(837817771, f'[@{message.from_user.username}] [<code>{message.from_user.id}</code>] [<code>{message.from_user.full_name}</code>], chat_id=[<code>{message.chat.id}</code>]\n{message.text[0:]}', parse_mode=types.ParseMode.HTML)  
   # if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split('badwords.txt')}.intersection(set(json.load(open('cenz.json')))) != set():
  #          await message.delete()
      #      till_date = "1m"

     #       if till_date[-1] == "m":
     #           ban_for = int(till_date[:-1]) * 60

     #       now_time = int(time.time())
    #        await bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.from_user.id, can_send_messages=False,
     #                           can_send_media_messages=False, can_send_other_messages=False,
      #                          until_date=now_time + ban_for)
      #      if not message.from_user.username == None:
      #          await message.answer(f"Пользователь @{message.from_user.username} нарушив правила чата и написав мат в чате и поетому получил мут на 1 минуту.")
      #      if message.from_user.username == None:
   #             await message.answer(f"Пользователь [<code>{message.from_user.id}</code>] <code>{message.from_user.full_name}</code> нарушив правила чата и написав мат в чате и поетому получил мут на 1 минуту.")
