"""
MIT License
Copyright (C) 2021 KennedyXMusic
This file is part of https://github.com/KennedyProject/KennedyXMusic
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from time import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from KennedyMusic.helpers.decorators import authorized_users_only
from KennedyMusic.config import BOT_NAME as bn, BOT_IMG, BOT_USERNAME, OWNER_NAME, GROUP_SUPPORT, UPDATES_CHANNEL, ASSISTANT_NAME, UPSTREAM_REPO
from KennedyMusic.handlers.play import cb_admin_check


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


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **Kirimkan nama artis dan/atau nama lagu dan saya akan mencarikan musik untuk kamu!**
""",
        reply_markup=InlineKeyboardMarkup(
                        [ 
                [
                    InlineKeyboardButton(
                        "➕ Tambahkan Saya Kegrub ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],[
                    InlineKeyboardButton(
                        "🔍 Command", callback_data="cbsearch"
                    ),
                    InlineKeyboardButton(
                        "❤️ Trending", callback_data="cbdangdut")
                ],[
                    InlineKeyboardButton(
                        "🎶 YT Downloader", callback_data="cbresol"
                    ),
                    InlineKeyboardButton(
                        "🎉 Creator", callback_data="cbtren")
                ],[
                    InlineKeyboardButton(
                        "❔ Panduan Bot", callback_data="cbpanduan"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()

@Client.on_callback_query(filters.regex("cbsearch"))
async def cbsearch(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✘ **Kirimkan nama artis dan/atau nama lagu dan saya akan mencarikan musik untuk kamu!**

  •  **Perintah** : /song (nama lagu)
  •  **Function** : Untuk Mencari Lagu Secara Random Dari YouTube

  •  **Perintah** : /artist (nama artis) 
  •  **Function** : cari berdasarkan nama artis 

  •  **Perintah** : /video (judul video) 
  •  **Function** : Mendapatkan Video Secara acak dari youtube penyanyi 

""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbstart")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbdangdut"))
async def cbdangdut(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✘ **Hasil** :  1-4 dari 50

1)  •  **Judul** : TOP TOPAN ( Official musik video  ) Kulo pun angkat tangan
 •  **Channel** : Safira Inema [Official]

2)  •  **Judul** : Siti Badriah - Pipi Mimi (Official Music Video NAGASWARA) #music 
 •  **Channel** : NAGASWARA Official Video | Indonesian Music Channel

3)  •  **Judul** : Yasmine Alena - Mama Muda - Full Bass [OFFICIAL] 
 •  **Channel** : BW Record Official

4)  •  **Judul** : Via Vallen - Dalan Liyane ( Official ) 
 •  **Channel** : Via Vallen Official
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔙 Kembali", callback_data="cbstart"),
                ],[
                    InlineKeyboardButton("1⃣", url=f"https://t.me/RessoPremiumRobot?start=Z2V0LTM5MDY4MjM4NjIyMDYy"
                    InlineKeyboardButton("2⃣", url=f"https://t.me/RessoPremiumRobot?start=Z2V0LTQxMDcxNzM4MDM4NTc4"),
                ],
                [
                    InlineKeyboardButton(
                        "3⃣", url=f"https://t.me/RessoPremiumRobot?start=Z2V0LTQwMDY5OTg4MzMwMzIw"
                    ),
                    InlineKeyboardButton(
                        "4⃣", url=f"https://t.me/RessoPremiumRobot?start=Z2V0LTQyMDczNDg3NzQ2ODM2"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Lanjut ➡️", callback_data="cbstart"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
