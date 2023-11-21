from loader import dp,bot
from aiogram import types
import requests
from handlers.users.insta3 import download_video3
from aiogram.dispatcher.filters import Text
from data.config import  Botusername


caption = f"""
📥 {Botusername} yordamida yuklangan
-----------------------------------------
📥 загружено с помощью {Botusername}
"""



@dp.message_handler(Text(startswith="https://instagram.com"))
async def dw(message: types.Message):
    link = message.text
    first = download_video3(url=link)
    print('*'*15, first)
    videos = first['videos']
    images = first['images']
    for video in videos:
        await message.answer_chat_action(action=types.ChatActions.UPLOAD_VIDEO)
        video = types.InputFile.from_url(url=video)
        await message.answer_sticker()
        try:

            await message.answer_video(video=video,caption=caption)
        except:
            await message.answer("Видео или изображение не найдено. Вероятно, это частный аккаунт..")
    for image in images:
        await message.answer_chat_action(action=types.ChatActions.UPLOAD_PHOTO)
        image = types.InputFile.from_url(url=image)
        try:

            await message.answer_photo(photo=image,caption=caption)
        except:
                await message.answer("Видео или изображение не найдено. Вероятно, это частный аккаунт..")


@dp.message_handler(Text(startswith="https://www.instagram.com"))
async def dw(message: types.Message):
    link = message.text
    first = download_video3(url=link)
    
    videos = first['videos']
    images = first['images']
    for video in videos:
        await message.answer_chat_action(action=types.ChatActions.UPLOAD_VIDEO)
        video = types.InputFile.from_url(url=video)
        try:

            await message.answer_video(video=video,caption=caption)
        except:
            await message.answer("Видео или изображение не найдено. Вероятно, это частный аккаунт..")
    for image in images:
        await message.answer_chat_action(action=types.ChatActions.UPLOAD_PHOTO)
        image = types.InputFile.from_url(url=image)
        try:

            await message.answer_photo(photo=image,caption=caption)
        except:
                await message.answer("Видео или изображение не найдено. Вероятно, это частный аккаунт..")