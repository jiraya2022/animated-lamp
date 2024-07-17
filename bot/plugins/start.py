from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m):

    await m.reply_text(
        text=f"I'ᴍ Sᴄʀᴇᴇɴsʜᴏᴛ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ. I ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ sᴄʀᴇᴇɴsʜᴏᴛs ғʀᴏᴍ"
        "ʏᴏᴜʀ ᴠɪᴅᴇᴏ ғɪʟᴇs ᴡɪᴛʜᴏᴜᴛ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇ ᴇɴᴛɪʀᴇ ғɪʟᴇ (ᴀʟᴍᴏsᴛ ɪɴsᴛᴀɴᴛʟʏ). Fᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs ᴄʜᴇᴄᴋ /ʜᴇʟᴘ.",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Dᴏɴᴀᴛᴇ", url="https://aslink.in/payy"
                    ),
                    InlineKeyboardButton("Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ", url="https://t.me/The_Happy_Hours"),
                ],
                [InlineKeyboardButton("Cᴏɴᴛᴇᴄᴛ Us", url="https://t.me/ThappyHour")],
            ]
        ),
    )
