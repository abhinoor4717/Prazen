from loguru import logger
import sys

from Settings import Settings

class CoreLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CoreLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized') and self._initialized:
            return

        logger.remove(0)

        # Bind logger_type
        core_logger = logger.bind(logger_type="CORE")

        # Add with a format that colors based on level

        core_logger.level("TRACE", color="<white>")
        core_logger.level("INFO", color="<green>")
        core_logger.level("SUCCESS", color="<light-blue>")

        core_logger.add(
            sys.stdout,
            level="TRACE",
            format="<level>{time:HH:mm:ss} {extra[logger_type]}: {message}</level>",
            colorize=True
        )

        self.Logger = core_logger
        self._initialized = True

    def Get(self):
        return self.Logger



class ClientLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ClientLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized') and self._initialized:
            return

        logger.remove(0)

        # Bind logger_type
        client_logger = logger.bind(logger_type="APP")

        # Add with a format that colors based on level

        client_logger.level("TRACE", color="<white>")
        client_logger.level("INFO", color="<green>")
        client_logger.level("SUCCESS", color="<light-blue>")

        client_logger.add(
            sys.stdout,
            level="TRACE",
            format="<level>{time:HH:mm:ss} {extra[logger_type]}: {message}</level>",
            colorize=True
        )

        self.Logger = client_logger
        self._initialized = True

    def Get(self):
        return self.Logger

def CORE_TRACE(*args):
    if Settings.DEBUG:
        CoreLogger().Get().trace(*args)
def CORE_INFO(*args):
    if Settings.DEBUG:
        CoreLogger().Get().info(*args)
def CORE_WARNING(*args):
    if Settings.DEBUG:
        CoreLogger().Get().warning(*args)
def CORE_SUCCESS(*args):
    if Settings.DEBUG:
        CoreLogger().Get().success(*args)
def CORE_CRITICAL(*args):
    if Settings.DEBUG:
        CoreLogger().Get().critical(*args)

def TRACE(*args):
    if Settings.DEBUG:
        ClientLogger().Get().trace(*args)
def INFO(*args):
    if Settings.DEBUG:
        ClientLogger().Get().info(*args)
def WARNING(*args):
    if Settings.DEBUG:
        ClientLogger().Get().warning(*args)
def SUCCESS(*args):
    if Settings.DEBUG:
        ClientLogger().Get().success(*args)
def CRITICAL(*args):
    if Settings.DEBUG:
        ClientLogger().Get().critical(*args)

__all__ = [
    # "CORE_TRACE",
    # "CORE_INFO",
    # "CORE_WARNING",
    # "CORE_SUCCESS",
    # "CORE_CRITICAL",
    "TRACE",
    "INFO",
    "WARNING",
    "SUCCESS",
    "CRITICAL"
]