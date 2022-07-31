# import logging
import os
API_ID = None
try:
    API_ID = os.environ['API_ID']
except:
    print(f"No value for API_ID provided!")
    # logging.info(f"No value for API_ID provided!")

API_HASH = None
try:
    API_HASH = os.environ['API_HASH']
except:
    print(f"No value for API_HASH provided!")
    # logging.info(f"No value for API_HASH provided!")

settings = {    
    'api_id': API_ID,
    'api_hash': f'{API_HASH}',
    'session': 'sessions/account1.session'
}