from decouple import config

BOT_TOKEN = config('BOT_TOKEN', default='')
USERNAME = config('USERNAME', default='')
TMDB_API_KEY = config('TMDB_API_KEY', default='')


# Check if any required variable is missing
if BOT_TOKEN is None or USERNAME is None or TMDB_API_KEY is None:
    raise ValueError("One or more required environment variables are missing. Please check your .env file.")