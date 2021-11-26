import logging
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from pyrogram import Client as app
from KennedyMusic.helpers.filters import command
from KennedyMusic.config import BOT_USERNAME


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@app.on_message(command(["search", f"search@{BOT_USERNAME}"]))
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
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("🔎 **Saya Sedang Mencari Artis Yang Kamu Minta**")
        results = YoutubeSearch(query, max_results=5).to_dict()
        i = 0
        text = ""
        while i < 10:
            text += f"🆒 {results[i]['title']} __{results[i]['duration']}__ __{results[i]['views']}__\n"
            text += f"*{results[i]['channel']}**\n"
            text += f"Lihat Di YouTube : https://www.youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await m.edit(str(e))
