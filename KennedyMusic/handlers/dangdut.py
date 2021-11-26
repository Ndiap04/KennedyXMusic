import logging
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from pyrogram import Client as app
from KennedyMusic.helpers.filters import command
from KennedyMusic.config import BOT_USERNAME
from time import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from KennedyMusic.helpers.decorators import authorized_users_only
from KennedyMusic.config import BOT_NAME as bn, BOT_IMG, BOT_USERNAME, OWNER_NAME, GROUP_SUPPORT, UPDATES_CHANNEL, ASSISTANT_NAME, UPSTREAM_REPO
from KennedyMusic.handlers.play import cb_admin_check


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_callback_query(filters.regex("cbpop"))
async def ytsearch(_, message: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🗑 Close", callback_data="close",
                )
            ]
        ]
    )

    try:
        if len(message.command) < 2:
            await message.reply_text("💁 Saya Belum Paham Apa maksudmu!\n")
            return
        query = message.text.split(Dangdut, 1)[1]
        m = await message.reply_text("🔎 **Saya Sedang Mencari Artis Yang Kamu Minta!**")
        results = YoutubeSearch(query, max_results=5).to_dict()
        i = 0
        text = ""
        while i < 5:
            text += f"🆒 {results[i]['title']} __{results[i]['duration']}__ __{results[i]['views']}__\n"
            text += f"**{results[i]['channel']}**\n"
            text += f"Lihat Di YouTube : https://www.youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await m.edit(str(e))
