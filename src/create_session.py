from src.client import Client

from src.settings import settings

__all__ = ("client_account",)

client_account = Client(**settings, try_logging_in=True)