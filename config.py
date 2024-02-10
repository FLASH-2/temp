import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 20872837))

    API_HASH = os.environ.get("API_HASH", "f3e4b12f39e489ce895c18102732b54a")
