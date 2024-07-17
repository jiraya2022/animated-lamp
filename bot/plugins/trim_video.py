from pyrogram import filters
from pyrogram.types import ForceReply

from ..screenshotbot import ScreenShotBot
from ..config import Config


@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("trim"))
)
async def _(c, m):
    await m.answer()
    dur = m.message.text.markdown.split("\n")[-1]
    await m.message.delete(True)
    await c.send_message(
        m.from_user.id,
        f"#ᴛʀɪᴍ_ᴠɪᴅᴇᴏ\n\n{dur}\n\nNᴏᴡ sᴇɴᴅ ʏᴏᴜʀ sᴛᴀʀᴛ ᴀɴᴅ ᴇɴᴅ sᴇᴄᴏɴᴅs ɪɴ ᴛʜᴇ ɢɪᴠᴇɴ ғᴏʀᴍᴀᴛ ᴀɴᴅ sʜᴏᴜʟᴅ"
        f"ʙᴇ ᴜᴘᴛᴏ {Config.MAX_TRIM_DURATION}s. \n**sᴛᴀʀᴛ:ᴇɴᴅ**\n\nEg: `400:500` ==> Tʜɪs ᴛʀɪᴍs ᴠɪᴅᴇᴏ ғʀᴏᴍ 400s ᴛᴏ 500s",
        reply_to_message_id=m.message.reply_to_message.message_id,
        reply_markup=ForceReply(),
    )
