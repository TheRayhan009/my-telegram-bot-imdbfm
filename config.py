from decouple import config

BOT_TOKEN = config('BOT_TOKEN', default='')



# Check if any required variable is missing
if BOT_TOKEN is None:
    raise ValueError("One required environment variables are missing. Please check your .env file.")