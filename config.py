import os

API_ID = int(os.environ.get("API_ID", "24556417"))
API_HASH = os.environ.get("API_HASH", "24008c23b7506a0bd8821f19c19cd654")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6583287452:AAFmZlFTX0tFE7VhQ34zHigf_eIS3Tvw4D0")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID" "-1001627581573")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID" 6013634182))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '-1001977716290')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "6184029705").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
