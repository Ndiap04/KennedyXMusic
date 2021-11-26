from asyncio.queues import QueueEmpty
from KennedyMusic.config import que
from pyrogram import Client, filters
from pyrogram.types import Message

from KennedyMusic.cache.admins import set
from KennedyMusic.helpers.channelmusic import get_chat_id
from KennedyMusic.helpers.decorators import authorized_users_only, errors
from KennedyMusic.helpers.filters import command, other_filters
from KennedyMusic.callsmusic import callsmusic


