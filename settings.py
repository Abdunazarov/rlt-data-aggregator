import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

# ENVIRONMENT VARIABLES
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")


# MESSAGES
REPLY_TEXT = """Привет! Отправь мне JSON с данными для агрегации в следующем формате:\n
{"dt_from": "YYYY-MM-DDTHH:MM:SS", "dt_upto": "YYYY-MM-DDTHH:MM:SS", "group_type": "hour/day/month"}"""

# MOCK (DUMMY) DATA
EXAMPLE_DATA = [
    {"dt": datetime(2022, 9, 1, 8, 0), "value": 1000},
    {"dt": datetime(2022, 9, 1, 9, 0), "value": 1500},
    {"dt": datetime(2022, 9, 1, 10, 0), "value": 1200},
    {"dt": datetime(2022, 9, 1, 11, 0), "value": 1300},
    {"dt": datetime(2022, 9, 2, 8, 0), "value": 1400},
    {"dt": datetime(2022, 9, 2, 9, 0), "value": 1100},
    {"dt": datetime(2022, 9, 2, 10, 0), "value": 1600},
    {"dt": datetime(2022, 9, 2, 11, 0), "value": 1700},
    {"dt": datetime(2022, 9, 3, 12, 0), "value": 1800},
    {"dt": datetime(2022, 9, 4, 12, 0), "value": 1900},
    {"dt": datetime(2022, 9, 5, 12, 0), "value": 2000},
    {"dt": datetime(2022, 9, 6, 12, 0), "value": 2100},
    {"dt": datetime(2022, 9, 7, 12, 0), "value": 2200},
    {"dt": datetime(2022, 9, 8, 12, 0), "value": 2300},
    {"dt": datetime(2022, 9, 9, 12, 0), "value": 2400},
    {"dt": datetime(2022, 9, 10, 12, 0), "value": 2500},
    {"dt": datetime(2022, 10, 1, 12, 0), "value": 2600},
    {"dt": datetime(2022, 10, 2, 12, 0), "value": 2700},
    {"dt": datetime(2022, 10, 3, 12, 0), "value": 2800},
    {"dt": datetime(2022, 10, 4, 12, 0), "value": 2900},
    {"dt": datetime(2022, 10, 5, 12, 0), "value": 3000},
    {"dt": datetime(2022, 10, 6, 12, 0), "value": 3100},
    {"dt": datetime(2022, 10, 7, 12, 0), "value": 3200},
    {"dt": datetime(2022, 11, 1, 12, 0), "value": 3300},
    {"dt": datetime(2022, 11, 2, 12, 0), "value": 3400},
    {"dt": datetime(2022, 11, 3, 12, 0), "value": 3500},
    {"dt": datetime(2022, 11, 4, 12, 0), "value": 3600},
    {"dt": datetime(2022, 11, 5, 12, 0), "value": 3700},
    {"dt": datetime(2022, 11, 6, 12, 0), "value": 3800},
    {"dt": datetime(2022, 11, 7, 12, 0), "value": 3900},
    {"dt": datetime(2022, 12, 1, 12, 0), "value": 4000},
    {"dt": datetime(2022, 12, 2, 12, 0), "value": 4100},
    {"dt": datetime(2022, 12, 3, 12, 0), "value": 4200},
    {"dt": datetime(2022, 12, 4, 12, 0), "value": 4300},
    {"dt": datetime(2022, 12, 5, 12, 0), "value": 4400},
    {"dt": datetime(2022, 12, 6, 12, 0), "value": 4500},
    {"dt": datetime(2022, 12, 7, 12, 0), "value": 4600},
]