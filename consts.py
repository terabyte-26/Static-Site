# Written by Hamza Farahat <farahat.hamza1@gmail.com>, 8/28/2025
# Contact me for more information:
# Contact Us: https://terabyte-26.com/quick-links/
# Telegram: @hamza_farahat or https://t.me/hamza_farahat
# WhatsApp: +212772177012
import os


class Consts(object):
    """
    This class holds configuration constants related to the database connection and server settings.

    It uses environment variables (loaded from a `.env` file) to populate values for database credentials,
    connection string, and server-related flags.
    """

    class Telegram(object):

        BOT_TOKEN: str = "7442633036:AAF0Tfi-vFtn2PCOzCRw4F5mrtNL2L1wUtk"  # os.environ.get('BOT_TOKEN')
        CHI_SMIA_X_TOPIC_ID: int = 48747
        Z2U_MARKET_KINGS_CHAT_ID: int = -1002223580315

