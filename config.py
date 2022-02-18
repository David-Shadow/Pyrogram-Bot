from os import environ as env

API_ID = int(env.get('API_ID', ''))
API_HASH = env.get('API_HASH', '')
BOT_TOKEN = env.get('BOT_TOKEN', '')
ADMINS = env.get('ADMINS', 1794161348)
ADMINS = [int(ADMINS) if (' ' not in ADMINS) else int(admin) for admin in str(ADMINS).split(' ')]
