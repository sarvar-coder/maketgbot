#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:18:43 2025

@author: sarvarboltaboyev
"""

import logging
import asyncio
from aiogram import Bot, Dispatcher, types, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
import wikipedia

wikipedia.set_lang('uz')

API_TOKEN = ''

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()


# Create a router
router = Router()

@router.message(Command("start", "hello"))
async def send_welcome(message: Message):
    """
    This handler will be called when user sends '/start' or '/hello' command.
    """
    await message.answer("Hi!\nI'm EchoBot! \nPowered by aiogram 3.")

@router.message()
async def senWiki(message: Message):
    
        search = message.text
        respond = wikipedia.summary(search)

        await message.answer("Marhamat Dustim") 
        await message.answer(" {}".format(respond))
     

# Register the router
dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())  # ✅ Works in standard Python scripts
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.create_task(main())

    
