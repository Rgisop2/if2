from os import environ

API_ID = int(environ.get("API_ID", "27353035"))
API_HASH = environ.get("API_HASH", "cf2a75861140ceb746c7796e07cbde9e")
BOT_TOKEN = environ.get("BOT_TOKEN", "8298659033:AAEjD8TQsX7q3KTn-4xAwPxfcyZ4Ck08wrA")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002073865889"))
ADMINS = int(environ.get("ADMINS", "1327021082"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://poulomi6969:hello@cluster.pmevjiz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster") 
DB_NAME = environ.get("DB_NAME", "vjlinkchangerbot2")
