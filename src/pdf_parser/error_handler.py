class ErrorHandler:
    def __init__(self):
        """
        Initializes the ErrorHandler with an empty error log.
        """
        self.error_log = []

    def log_error(self, error: str) -> None:
        """
        Logs an error message into the error log.
        :param error: The error message to log.
        """
        self.error_log.append(error)
        print(f"Error Logged: {error}")

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
