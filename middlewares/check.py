


from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler
from data.config import  CHANNELS
from utils.misc import subscription
from loader import bot, db

text = '''
👋 Assalomu alaykum. Men Instagram Video Yuklovchi Telegram Botman!\n
- Men sizga videolarni yuklashga yordam beraman.\n
📤 Shunchaki kerakli videoni havola(linkini yuboring) menga yuboring.
-----------------------------------------
👋 Здравствуйте. Я Telegram-бот для загрузки видео из Instagram!\n
- Я помогу вам загрузить видео.\n
📤 Просто пришлите мне ссылку на желаемое видео
'''
class WorkingHoursMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: types.Message, data: dict):
        
        user = message.from_user.id
        db.add_user(user, message.from_user.username, message.from_user.first_name)
        final_status = True
        btn = types.InlineKeyboardMarkup(row_width=1)
        for channel in CHANNELS:
                status = await subscription.check(user_id=user,
                                                channel=channel)
                final_status *= status
                channel = await bot.get_chat(channel)
                if status:
                        invite_link = await channel.export_invite_link()
                        btn.add(types.InlineKeyboardButton(text=f"✅ {channel.title}", url=invite_link))
                if not status:
                        invite_link = await channel.export_invite_link()
                        btn.add(types.InlineKeyboardButton(text=f"{channel.title} 🚀 ", url=invite_link))
                        btn.add(types.InlineKeyboardButton(text="Obunani tekshirish", callback_data="check_subs"))
                if final_status:
                        return
                if not final_status:
                        await message.answer("Botdan foydalanish uchun quyidagi kanalga obuna bo'ling!", disable_web_page_preview=True, reply_markup=btn)
        raise CancelHandler()
    
