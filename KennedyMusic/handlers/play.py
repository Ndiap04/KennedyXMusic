import os
from os import path
from typing import Callable
from asyncio.queues import QueueEmpty

import aiofiles
import aiohttp
from KennedyMusic.converter.converter import convert
import ffmpeg
import requests
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream
from KennedyMusic.cache.admins import admins as a
from KennedyMusic.callsmusic import callsmusic
from KennedyMusic.callsmusic.callsmusic import client as USER
from KennedyMusic.callsmusic.queues import queues
from KennedyMusic.config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    DURATION_LIMIT,
    GROUP_SUPPORT,
    THUMB_IMG,
    UPDATES_CHANNEL,
    que,
)
from KennedyMusic.downloaders.youtube import download
from KennedyMusic.helpers.admins import get_administrators
from KennedyMusic.helpers.channelmusic import get_chat_id
from KennedyMusic.helpers.chattitle import CHAT_TITLE
from KennedyMusic.helpers.decorators import authorized_users_only
from KennedyMusic.helpers.filters import command, other_filters
from KennedyMusic.helpers.gets import get_url, get_file_name
from PIL import Image, ImageDraw, ImageFont
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtube_search import YoutubeSearch
