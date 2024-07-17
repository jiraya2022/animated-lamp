from pyrogram import filters

from bot.screenshotbot import ScreenShotBot
from bot.config import Config


HELP_TEXT = """Wᴇʟᴄᴏᴍᴇ ᴛᴏ Sᴄʀᴇᴇɴsʜᴏᴛ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ. Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ:

    1. Sᴄʀᴇᴇɴsʜᴏᴛs.
    2. Sᴀᴍᴘʟᴇ Vɪᴅᴇᴏ.
    3. Tʀɪᴍ Vɪᴅᴇᴏ.

Sᴇᴇ /sᴇᴛᴛɪɴɢs ᴛᴏ ᴄᴏɴғɪɢᴜʀᴇ ʙᴏᴛ's ʙᴇʜᴀᴠɪᴏʀ.
Usᴇ /sᴇᴛ_ᴡᴀᴛᴇʀᴍᴀʀᴋ ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ᴡᴀᴛᴇʀᴍᴀʀᴋs ᴛᴏ ʏᴏᴜʀ sᴄʀᴇᴇɴsʜᴏᴛs."""
ADMIN_NOTIFICATION_TEXT = (
    "Sɪɴᴄᴇ ʏᴏᴜ ᴀʀᴇ ᴏɴᴇ ᴏғ ᴛʜᴇ ᴀᴅᴍɪɴs, ʏᴏᴜ ᴄᴀɴ ᴄʜᴇᴄᴋ /ᴀᴅᴍɪɴ ᴛᴏ ᴠɪᴇᴡ ᴛʜᴇ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs."
)


@ScreenShotBot.on_message(filters.private & filters.command("help"))
async def help_(c, m):

    await m.reply_text(
        text=HELP_TEXT.format(
            mention=m.from_user.mention,
            admin_notification=ADMIN_NOTIFICATION_TEXT
            if m.from_user.id in Config.AUTH_USERS
            else "",
        ),
        quote=True,
    )
