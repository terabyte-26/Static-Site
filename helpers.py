# Written by Hamza Farahat <farahat.hamza1@gmail.com>, 8/28/2025
# Contact me for more information:
# Contact Us: https://terabyte-26.com/quick-links/
# Telegram: @hamza_farahat or https://t.me/hamza_farahat
# WhatsApp: +212772177012

import requests

from consts import Consts


def get_ip_address_data(ip_address):

    print('ip_address', ip_address)

    resp = requests.get(f"https://freeipapi.com/api/json/{ip_address}")
    print('resp', resp.status_code)
    if resp.status_code == 200:
        return resp.json()
    else:
        return {"success": False}





def send_message(chat_id, text=None, message_thread_id=None, silent=False, ):
    """
    Sends a message to a chat using the Telegram Bot API. Optionally sends an image.

    Args:
        chat_id (int): The ID of the chat.
        text (str): The text of the message.
        message_thread_id (int, optional): The unique identifier of the message thread (topic). Defaults to None.
        silent (bool, optional): Whether to send the message silently. Defaults to False.

    Returns:
        Response: The response from the Telegram Bot API.
    """
    try:

        method = "sendMessage"

        # Define the standard data
        data: dict = {
            "chat_id": int(chat_id),
            "text": text,
            "parse_mode": "HTML",
            "disable_notification": silent,
            "message_thread_id": message_thread_id,
        }

        url = f"https://api.telegram.org/bot{Consts.Telegram.BOT_TOKEN}/{method}"
        resp = requests.post(url, data=data, timeout=3, verify=False)

        if resp.json()["ok"] is False:
            print(resp.json())

        return resp
    except BaseException as e:
        print(f"An error occurred: {e}")
        pass

