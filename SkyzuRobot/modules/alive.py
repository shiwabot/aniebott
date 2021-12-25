import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SkyzuRobot.events import register
from SkyzuRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/fa109566a6983ff1b7173.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Anie Robot.** \n\n"
    TEXT += "⚪ **I'm Working Properly** \n\n"
    TEXT += f"⚪ **My Master : [Denvil](https://t.me/Denvil_pro)** \n\n"
    TEXT += f"⚪ **Library Version :** `{telever}` \n\n"
    TEXT += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
    TEXT += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
    TEXT += "**Thanks For Adding Me Here ❤️**"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", "https://t.me/Anierobot_bot?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/Aniebotsupports"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
