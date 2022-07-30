from src.client import Client

from src.credentials import credentials

__all__ = ("client_account",)

client_account = Client(**credentials, try_logging_in=True)