from dispatcher import dp
from config import open_weather_token
from aiogram import Bot, types,executor,Dispatcher
from db import BotDB
from dbx import Database
from main_news import check_news_update
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink

if __name__ == "__main__":
    print("<<<START>>>")
    executor.start_polling(dp, skip_updates=False)