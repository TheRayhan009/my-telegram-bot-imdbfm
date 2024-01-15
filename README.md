# IMDBFM

Movie Info Bot is a Telegram bot that provides information about movies and series using data from IMDb.

## Features

- Get details about a movie or series by sending its name to the bot.
- Fast and efficient information retrieval with response times displayed.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- [Telebot](https://pypi.org/project/pyTelegramBotAPI/) library installed. You can install it using `pip install pyTelegramBotAPI`.
- API key/token for the bot obtained from the [BotFather](https://core.telegram.org/bots#botfather).
- The PyMovieDb library for IMDb information. Install it with `pip install PyMovieDb`.

## Configuration

Rename the `.env-example` to `.env` file in the project directory.

```bash
# .env

BOT_TOKEN = actual_bot_token


```

Replace `"YOUR_BOT_TOKEN"` with the actual token obtained from the BotFather.

## Usage

1. Start the bot by running `bot.py`.
2. Open a chat with the bot on Telegram.
3. Send the name of the movie or series you want information about.
4. Wait for the bot to reply with details, including a poster image.

## Commands

- **/start**: Displays a welcome message.
- **/help**: Provides information on how to use the bot.

## Author

[@TheRayhan009](https://github.com/TheRayhan009)
[@MudabbirulSaad](https://github.com/mudabbirulsaad)

## Acknowledgements

- [Telebot Library](https://github.com/eternnoir/pyTelegramBotAPI)
- [PyMovieDb Library](https://github.com/itsmehemant7/PyMovieDb)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
