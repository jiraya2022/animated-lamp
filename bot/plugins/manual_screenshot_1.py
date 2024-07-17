from pyrogram import filters
from pyrogram.types import ForceReply

from bot.screenshotbot import ScreenShotBot


@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("mscht"))
)
async def _(c, m):
    await m.answer()
    dur = m.message.text.markdown.split("\n")[-1]
    await m.message.delete(True)
    await c.send_message(
        m.from_user.id,
        f"#ᴍᴀɴᴜᴀʟ_sᴄʀᴇᴇɴsʜᴏᴛ\n\nNᴏᴡ sᴇɴᴅ ʏᴏᴜʀ ʟɪsᴛ ᴏғ sᴇᴄᴏɴᴅs sᴇᴘᴀʀᴀᴛᴇᴅ ʙʏ (ᴄᴏᴍᴍᴀ).\n\nEɢ: 0,10,40,60,120.\n\nTʜɪs ᴡɪʟʟ ɢᴇɴᴇʀᴀᴛᴇ sᴄʀᴇᴇɴsʜᴏᴛs ᴀᴛ 0, 10, 40, 60, ᴀɴᴅ 120 sᴇᴄᴏɴᴅs.\n\n1. Tʜᴇ ʟɪsᴛ ᴄᴀɴ ʜᴀᴠᴇ ᴀ ᴍᴀxɪᴍᴜᴍ ᴏғ 10 ᴠᴀʟɪᴅ ᴘᴏsɪᴛɪᴏɴs.\n2. Tʜᴇ ᴘᴏsɪᴛɪᴏɴ ʜᴀs ᴛᴏ ʙᴇ ɢʀᴇᴀᴛᴇʀ ᴛʜᴀɴ ᴏʀ ᴇᴏ̨ᴜᴀʟ ᴛᴏ 0, ᴏʀ ʟᴇss ᴛʜᴀɴ ᴛʜᴇ ᴠɪᴅᴇᴏ ʟᴇɴɢᴛʜ ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ʙᴇ ᴠᴀʟɪᴅ.",
        reply_to_message_id=m.message.reply_to_message.message_id,
        reply_markup=ForceReply(),
    )
