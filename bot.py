from dispatcher import dp
import handlers
import requests
from aiogram import Bot, types,executor,Dispatcher
import asyncio
import datetime
import time
from main_news import check_news_update
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text

if __name__ == "__main__":
    print("<<<START>>>")
    executor.start_polling(dp)
