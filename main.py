import logging
from pyrogram import Client, filters, idle
from pyrogram.types import *
import requests
import os
import re
import asyncio
from datetime import datetime
from config import *

from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

API_ID = API_ID
API_HASH = API_HASH 
LOG_GROUP = LOG_GROUP
SUDO_USERS = SUDO_USERS
DB_URL = DB_URL


if not STRING_SESSION1:
    logging.error("No String Session Found! Exiting!")
    quit(1)

if not API_ID:
    logging.error("No Api-ID Found! Exiting!")
    quit(1)

if not API_HASH:
    logging.error("No ApiHash Found! Exiting!")
    quit(1)

if ALIVE_IMG:
    ALIVE_PIC = ALIVE_IMG
else: 
    ALIVE_PIC = 'https://te.legra.ph/file/a7c82fa1cb4c41097dadd.jpg'

if MONGO_DB:
    MONGO_DB = MONGO_DB
else: 
    MONGO_DB = "mongodb+srv://Zaid:Zaid@cluster0.4bszo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

if LOG_GROUP:
    Owner = LOG_GROUP
else:
    Owner = 777000


if STRING_SESSION1:
    bot1 = Client(session_name= STRING_SESSION1, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot1 = None
    
scheduler = AsyncIOScheduler()
CMD_HELP = {}
START_TIME = datetime.now()

if bot1:
    bot1.start()
    bot1.join_chat("XnKiT_K")

idle()

print("🎉 Successfully Deployed Palghar Project 🎉")
print("Palghar Project is ready do .alive or .ping to see the project is ready or not")
