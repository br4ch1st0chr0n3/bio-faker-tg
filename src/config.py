CHECK_INTERVAL = 3

TIME_ZONE = "Etc/GMT-3"

INTERNET_CHECK_URL = "1.1.1.1"

LOG_FORMAT = "%(levelname) -10s %(asctime)s %(name) -15s %(funcName) -20s: %(message)s"

# import logging
import os

PERIOD = 1

try:
    PERIOD = int(os.environ['PERIOD'])

except Exception as e:
    print(f"Setting the default PERIOD: {PERIOD}")
    # logging.info(f"Setting the default PERIOD: {PERIOD}")