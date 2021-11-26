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
                        "➕ Tambahkan Saya Kegrub ➕", callback_data="cbgroups")
                ],[
                    InlineKeyboardButton(
                        "🔍 Searching​​", callback_data="cbsearch"
                    ),
                    InlineKeyboardButton(
                        "❤️ Untuk Kamu", callback_data="cbfavorit")
                ],[
                    InlineKeyboardButton(
                        "🎶 Pilih Resolusi", callback_data="cbresol"
                    ),
                    InlineKeyboardButton(
                        "🎉 Trending", callback_data="cbtren")
                ],[
                    InlineKeyboardButton(
                        "♻ Update", callback_data="cbupdate")
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

@Client.on_callback_query(filters.regex("cbgroups"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""💁‍♂ **Kemungkinan Saya Belum Bisa Ditambahkan Kegrub**!
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("❌", callback_data="close")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsearch"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Kirimkan nama artis dan/atau nama lagu dan saya akan mencarikan musik untuk kamu!**

/song (nama lagu) - cari berdasarkan judul lagu ✓
/artis (nama artis) - cari berdasarkan nama artis ✓
/video (nama lagu) - secara acak dari youtube penyanyi ✓

""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbstart")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbfavorit"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🎉 **Silakan Pilih Favorit Kamu** ! Saya Akan Kasih Link Youtube Nya !
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("1⃣ Dangdut", callback_data="cbdangdut"),
                    InlineKeyboardButton("2⃣ Reggae Indonesia", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("3⃣ Remix DJ local", callback_data="cbadmin"),
                    InlineKeyboardButton("4⃣ Pop", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("5⃣ Islami", callback_data="cbowner")],
                [InlineKeyboardButton("🔙 Kembali", callback_data="cbstart")],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("cbdangdut"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f""Hasil 1-10 dari 10**

1) **Judul** : Rembulan Malam
Link : `(https://www.youtube.com/watch?v=oRbEEXN2xOk)`

2) **Judul** : Top Topan
Link : (https://www.youtube.com/watch?v=Yp0aCRvxQ6U)

3) **Judul** : Lungamu Tinggal Kenangan
Link : (https://youtu.be/OcLHeZow7x4)

4) **Judul** : Pingal
Link : (https://youtu.be/vPRyV1iMn9Y)

5) **Judul** : Sewu Kutho
Link : (https://youtu.be/YNnLBN--G-0)

6) **Judul** : Roso Atiku
Link : (https://youtu.be/NY5tCLt_QEc)

7) **Judul** : Angel
Link : (https://youtu.be/k-6gCAyDPaM)

8) **Judul** : Menung Tanpo Udan
Link : (https://youtu.be/ppjO2aYR4kQ)

9) **Judul** : Nutupi Laraku
Link : (https://youtu.be/0x2oKBhIGh8)

10) **Judul** : Beta Janji
Link : (https://youtu.be/EI-8lLlhaOo)
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbstart")]]
        ),
    )
