import logging

from requests import request
import telethon

from asyncio import sleep
from datetime import timedelta

# sync is a magical module!
# don't remove it
from telethon import TelegramClient, sync
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.tl.functions.account import UpdateProfileRequest

from src.quotes import yoda

import datetime
import pytz
import secrets

from src.config import PERIOD, TIME_ZONE


def get_now() -> datetime.datetime:
    return datetime.datetime.now(pytz.timezone(TIME_ZONE))


class Client:
    def __init__(self, session, api_id, api_hash, try_logging_in=False):
        self.session = session
        self.api_id = api_id
        self.api_hash = api_hash
        self.account = TelegramClient(session, api_id, api_hash)
        self.account.connect()
        self.lastupdate = get_now() - timedelta(minutes=PERIOD)
        if try_logging_in:
            self.account.start()

    async def edit_bio(self, new_bio):
        logging.debug("check for changing bio")
        try:
            if get_now().minute - self.lastupdate.minute >= PERIOD:
                logging.info(f"Change bio to `{new_bio}`")
                await self.account(
                    UpdateProfileRequest(
                        about=new_bio,
                    )
                )
                self.lastupdate = get_now()
        except FloodWaitError as e:
            logging.warning(f"Got flood message: {e}. sleep for {e.seconds}")
            await sleep(e.seconds)

    async def set_new_phrase(self):
        try:
            await self.edit_bio(self.new_phrase())
        except telethon.errors.rpcerrorlist.AboutTooLongError:
            pass

    def new_phrase(self):
        return secrets.choice(yoda)

    def __str__(self):
        me = self.account.get_me()
        return f"TelegramClient({me.first_name} {me.last_name}, @{me.username})"
