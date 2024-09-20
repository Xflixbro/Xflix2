import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "7409495927:AAFdze2LfFFVDaoa3ItiecZPB5DLUmEeQ7c")
API_ID = int(os.environ.get("API_ID", "15529802"))
API_HASH = os.environ.get("API_HASH", "92bcb6aa798a6f1feadbc917fccb54d3")


OWNER_ID = int(os.environ.get("OWNER_ID", "821215952"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://SeriesXeonbot:SeriesXeonbot@cluster0.sxdov5x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "XFLIX")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002162795137"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002105815265"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001804728701"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1001690762284"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "-1001542373688"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "300")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[821215952]
    for x in (os.environ.get("ADMINS", "821215952 6048003536").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"

IMG_URL = os.environ.get("IMG_URL", "https://telegra.ph/file/7de5ca78e3963506bddfd.jpg")
                             







USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "ʜᴇʟʟᴏ {mention}\n\nɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ...")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel</b>")

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/52cd697e31b12fe66c184.jpg")

ABOUT_TXT = f"""<b><blockquote>╭───────────⍟
├➤ ᴄʀᴇᴀᴛᴏʀ  : <a href='t.me/InkaLinks'>ᴛʜɪs ᴘᴇʀsᴏɴ</a>
├➤ ʟɪʙʀᴀʀy : <a href=https://github.com/pyrogram>ᴘʏʀᴏɢʀᴀᴍ</a>
├➤ ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>ᴘʏᴛʜᴏɴ 3</a>
├➤ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href=https://t.me/outlawbots>ᴏᴜᴛʟᴀᴡ ʙᴏᴛs</a>
├➤ ᴘᴀɪᴅ ʙᴏᴛ : <a href=https://t.me/ifeelscam>ᯓ ɪɴᴠᴀʟɪᴅ ᡣ𐭩</a>
├➤ ᴅᴇᴠʟᴏᴘᴇʀ : <a href=https://t.me/HateXfree>ᯓ ʜᴀᴛᴇ ғʀᴇᴇ ᡣ𐭩</a>
╰───────────────⍟</blockquote></b>"""





ADMINS.append(OWNER_ID)
ADMINS.append(821215952)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
