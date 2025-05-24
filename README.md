# Telegram Bot in aiogram

A simple Telegram bot written in Python using the [aiogram](https://docs.aiogram.dev/en/latest/) library. The bot greets the user by sending a message with the user's name.

---

## Features

- Replies to the `/start` command by greeting the user by name.

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/mikhailshubin26/SiGameBot.git
cd SiGameBot
```

2. Create and activate a virtual environment (recommended):

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
3. Install the dependencies

```
pip3 install -r requirements.txt  # Linux/macOS
pip install -r requirements.txt   # Windows
```

4. Add token

Create an .env file in the root of your project and add your bot token there:
```
BOT_TOKEN=place_your_token_here

```

You can get token here - https://t.me/BotFather

## Launch

```
python3 main.py  # Linux/MacOs
py main.py       # Windows
```

## Project Structure
+ main.py - main file with bot logic.
+ config.py - loading configuration from .env.
+ get_username.py - function to get username.
+ .env - file with environment variables (should not be included in the repository).

## Example Usage

After launching the bot, it will respond to the /start command with the following message:
```
Hello, <Your Name> 👋
```

## License

MIT License

## Contact

If you have any questions or suggestions, feel free to contact me via email: mishaelshubin@gmail.com

## Support

If you'd like to support this project, you can donate cryptocurrency:

Bitcoin (BTC): bc1qllfd0zxmk45j3x53d5dnu9y0ls7vdx60yyk3u4

Ethereum (ETH): 0x480468BbB77ef4a4abed20e81656e4CFBcc1C055

Tether (USDT TRC-20): TVrv9eQp4cvQ71NhE2uypCksjR9qQZBHcZ

*Your support is appreciated ❤️*
