import os

API_ID = os.environ['API_ID']
API_HASH = os.environ['API_HASH']

credentials = {    
    'api_id': API_ID,
    'api_hash': f'{API_HASH}',
    'session': 'sessions/account1.session'
}