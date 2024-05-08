# Copyright © 2024 Taoshi Inc

import requests


class TGBot:
    """
    Initializes the Telegram Bot with the API token, chat ID, and send URL.
    """

    def __init__(self):
        self._api_token = "xxxx"
        self._chat_id = "xxxx"
        self._send_url = f"https://api.telegram.org/bot{self._api_token}/sendMessage"

    def send_message(self, payload, logger):
        """
        Sends a message using the provided payload and logger.

        Args:
            payload: The message payload to send.
            logger: The logger instance for logging messages.

        Returns:
            self
        """

        payload_json = {"chat_id": self._chat_id, "parse_mode": "HTML", "text": payload}

        return_message = requests.post(self._send_url, json=payload_json)
        logger.info(str(return_message))
        return self
