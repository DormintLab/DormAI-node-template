# Telegram Bot for Message Handling

This Telegram bot reads messages from users, sends them to a remote API, and returns a response to the user. The bot is built using the [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library.

## Features
- Receives a message from the user and creates event with text of message as output and user tg_id as context 
- Receives a text as input and context with tg_id and sends message to user with such tg_id

## Requirements
- Python 3.7+
- Telegram Bot Token (get it from [BotFather](https://core.telegram.org/bots#botfather))
- `httpx` library for sending HTTP requests to the API.
- `python-telegram-bot` library.
