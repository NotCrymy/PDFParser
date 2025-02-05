import logging
import os

class ErrorHandler:
    def __init__(self, log_file: str = "logs/errors.log"):
        """
        Initializes the ErrorHandler and ensures the log directory exists.
        :param log_file: Path to the log file where errors will be stored.
        """
        self.log_file = log_file
        self._ensure_log_directory()

        logging.basicConfig(
            filename=self.log_file,
            level=logging.ERROR,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.error_log = []

    def _ensure_log_directory(self) -> None:
        """
        Ensures that the logs directory exists.
        """
        log_dir = os.path.dirname(self.log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)  # Creates logs/ directory automatically

    def log_error(self, error: str) -> None:
        """
        Logs an error message into the internal error list and writes it to the log file.
        :param error: The error message to log.
        """
        self.error_log.append(error)
        logging.error(error)
        print(f"Error logged: {error}")

    def get_errors(self) -> list[str]:
        """
        Returns all logged errors.
        :return: A list of error messages.
        """
        return self.error_log

    def handle_error(self, class_name: str, method_name: str, error: Exception) -> None:
        """
        Handles an error by logging it with additional context.
        :param class_name: The name of the class where the error occurred.
        :param method_name: The name of the method where the error occurred.
        :param error: The exception object.
        """
        error_message = f"[{class_name}.{method_name}] {str(error)}"
        self.log_error(error_message)