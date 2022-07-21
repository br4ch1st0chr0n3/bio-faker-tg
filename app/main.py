import logging

from asyncio import get_event_loop, sleep

import socket
from src.config import INTERNET_CHECK_URL, CHECK_INTERVAL, LOG_FORMAT
from src.create_session import client_account

def is_connected():
    """
    Return true if script
    has connection to the Internet
    """
    try:
        socket.create_connection((INTERNET_CHECK_URL, 53))
        return True
    except OSError:
        return False


async def poll_inernet(function, interval, **kwargs):
    max_sleep = 15 * 60
    sleep_if_no_internet = interval

    while 1:
        logging.debug(f"Run function {function.__name__}")
        if is_connected():
            sleep_if_no_internet = interval
            await function(**kwargs)
            await sleep(interval)
        else:
            logging.error(
                f"No internet connection. sleep for {sleep_if_no_internet} seconds"
            )
            await sleep(min(sleep_if_no_internet, max_sleep))
            sleep_if_no_internet += interval


# if __name__ == "__main__":
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

print(client_account)

loop = get_event_loop()

future = poll_inernet(
    function=client_account.set_new_phrase,
    interval=CHECK_INTERVAL,
)

loop.run_until_complete(future)
