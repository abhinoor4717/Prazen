from loguru import logger
import sys

class Logger:
    # Static class variables to store logger instances
    core_logger = None
    client_logger = None

    @staticmethod
    def setup_core_logger():
        # Initialize core logger only once
        if Logger.core_logger is None:
            # Only remove default logger once
            logger.remove()
            Logger.core_logger = logger.bind(logger_type="CORE")  # Bind extra information
            Logger.core_logger.add(
                sys.stdout,
                level="INFO",
                format="<green>{time:YYYY-MM-DD HH:mm:ss} {extra[logger_type]}: {message}</green>",
                colorize=True
            )
            Logger.core_logger.add(
                sys.stdout,
                level="WARNING",
                format="<yellow>{time:YYYY-MM-DD HH:mm:ss} {extra[logger_type]}: {message}</yellow>",
                colorize=True
            )

    @staticmethod
    def setup_client_logger():
        # Initialize client logger only once
        if Logger.client_logger is None:
            # Only remove default logger once
            logger.remove()
            Logger.client_logger = logger.bind(logger_type="Client")  # Bind extra information
            Logger.client_logger.add(
                sys.stdout,
                level="INFO",
                format="<green>{time:YYYY-MM-DD HH:mm:ss} {extra[logger_type]}: {message}</green>",
                colorize=True
            )
            Logger.client_logger.add(
                sys.stdout,
                level="WARNING",
                format="<yellow>{time:YYYY-MM-DD HH:mm:ss} {extra[logger_type]}: {message}</yellow>",
                colorize=True
            )

    @staticmethod
    def get_core_logger():
        # Ensure the core logger is set up
        Logger.setup_core_logger()
        return Logger.core_logger

    @staticmethod
    def get_client_logger():
        # Ensure the client logger is set up
        Logger.setup_client_logger()
        return Logger.client_logger


# Example usage
Logger.setup_core_logger()  # Set up core logger once
core_logger = Logger.get_core_logger()  # Get the core logger (will not reinitialize)

Logger.setup_client_logger()  # Set up client logger once
client_logger = Logger.get_client_logger()  # Get the client logger (will not reinitialize)

# Core logs
core_logger.info(10)
var = 100*2
core_logger.warning("Wanring {0}", var*2)