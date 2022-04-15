import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/63ab246410bb5c3998b2b.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
 𝙃𝙚𝙡𝙡𝙤, 𝙄 𝘼𝙢 𝙌𝙐𝙀𝙀𝙉 🧚‍♀️ 𝙎𝙪𝙥𝙚𝙧 𝙁𝙖𝙨𝙩 𝙈𝙪𝙨𝙞𝙘 𝙋𝙡𝙖𝙮𝙚𝙧
𝘽𝙤𝙩 𝙁𝙤𝙧 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙂𝙧𝙤𝙪𝙥𝙨 ...
┏━━━━━━━━━━━━━━━━━┓
┣★𝗖𝗵𝗮𝗻𝗻𝗲𝗹: [𝙆𝙄𝙉𝙂 𝘽𝙄𝙊𝙯](https://t.me/king_bioz)
┣★𝗦𝘂𝗽𝗽𝗼𝗿𝘁: [𝙏𝘼𝙈𝙄𝙇 𝘾𝙃𝘼𝙏𝘽𝙊𝙓](https://t.me/tamil_chatbox)
┣★𝗢𝘄𝗻𝗲𝗿 : [𝙄𝙈 𝙆𝙄𝙉𝙂](https://t.me/imzaynking)
┗━━━━━━━━━━━━━━━━━┛
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🧚‍♀ ❰ 𝗔𝗱𝗱 𝗠𝗲 𝗜𝗻 𝗚𝗿𝗼𝘂𝗽 ❱ 🧚‍♀", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "owner"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7e97fc89a25512e007156.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⭕𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url=f"https://t.me/tamil_chatbox")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["QUEEN", "Group", "@Channel", "/Channel", "Channel"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/63ab246410bb5c3998b2b.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💙𝗖𝗛𝗔𝗡𝗡𝗘𝗟❤️", url=f"https://t.me/king_bioz")
                ]
                
            ]
        ),
    )
