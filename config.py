import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "8c03cfc6e8be855de935ac61ac4047d7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6539803331:AAHLOjtJg74ehDrzwPZ5QKALLkXm7XeAwSk")
    TELEGRAM_API = os.environ.get("TELEGRAM_API", "28583769")
    OWNER = os.environ.get("OWNER", "6675988213")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "NoMoreFools")
    PASSWORD = os.environ.get("PASSWORD", "TomenMreger")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://More:More@cluster0.o1bykke.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "-1002120946369")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
