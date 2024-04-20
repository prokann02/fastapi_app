import logging


# Define a formatter with green color
class GreenFormatter(logging.Formatter):
    GREEN = '\033[92m'
    RESET = '\033[0m'

    def format(self, record):
        message = super().format(record)
        return f"{self.GREEN}{message}{self.RESET}"


def set_logging():
    console_handler = None

    try:
        formatter = GreenFormatter('%(levelname)s:%(message)s')

        # Create a handler for console output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

    except ValueError:
        logging.info("Was chosen wrong format")

    # Get the root logger and add the console handler
    root_logger = logging.getLogger()
    if console_handler:
        root_logger.addHandler(console_handler)

    # Set logging level
    root_logger.setLevel(logging.INFO)

    return logging
