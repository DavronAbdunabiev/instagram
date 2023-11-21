import logging
from aiogram import types
from data.config import ADMINS, CHANNELS
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from loader import bot, dp, db
from utils.misc import subscription
import time

text = '''
👋 Assalomu alaykum. Men Instagram Video Yuklovchi Telegram Botman!\n
- Men sizga videolarni yuklashga yordam beraman.\n
📤 Shunchaki kerakli videoni havola(linkini yuboring) menga yuboring.
-----------------------------------------
👋 Здравствуйте. Я Telegram-бот для загрузки видео из Instagram!\n
- Я помогу вам загрузить видео.\n
📤 Просто пришлите мне ссылку на желаемое видео
'''


@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):

        await message.answer(text)


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
                await call.answer()
                result = str()
                btn = InlineKeyboardMarkup()
                final_status = True
                for channel in CHANNELS:
                        status = await subscription.check(user_id=call.from_user.id,
                                                        channel=channel)
                final_status *=status
                channel = await bot.get_chat(channel)
                if not status:
                        invite_link = await channel.export_invite_link()
                        btn.add(InlineKeyboardButton(text=f"❌ {channel.title}", url=invite_link))
                btn.add(InlineKeyboardButton(text="Obunani tekshirish", callback_data="check_subs"))
                if final_status:
                        await call.message.answer("Siz kanalga a'zo bo'lgansiz!")
                        await call.message.answer(text)

                if not final_status:
                        await call.answer(cache_time=60)
                        await call.message.answer("Siz quyidagi kanal(lar)ga obuna bo'lmagansiz!",reply_markup=btn)
                await call.message.delete()
                print(final_status)



@dp.message_handler(commands="insta", user_id=ADMINS)
async def send_file(message: types.Message):
        text = """
✅ Botdagi nosozliklar bartaraf etildi, bot oldingidek ishlamoqda\nAgarda sizda avval yaxshi ishlamagan bo’lsa, /start tugmasini bosib qayta ishlatib yuboring."""
    
        users = db.all_users()
        spam = 0
        notspam = 0
        for i in users:
                try:
                        await dp.bot.send_message(i[0],text,parse_mode="HTML")
                        notspam += 1
                        time.sleep(0,5)
                        
                except:
                        spam += 1
        info = f"Xabar yetib borgan foydalanuvchilar soni: {notspam}\nQolganlar soni: {spam}"
        await admin_sms(info)


async def admin_sms(text):
	for admin in ADMINS:
		await dp.bot.send_message(admin,text,parse_mode="HTML")




@dp.message_handler(text="/baza", user_id=ADMINS)
async def send_file(message: types.Message):
    file_path = "data/class.db"
    await message.answer_document( document=open(file_path, 'rb'))



@dp.message_handler(text="/statis", user_id=ADMINS)
async def send_file(message: types.Message):
    users = db.count_users()
    info  = f"<b>Botdagi foydalanuvchilar soni: {users[0]} ta</b>"
    await message.answer(info)
