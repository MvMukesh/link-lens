### test only
class InvalidURLException(Exception):
    def __init__(self, message: str="Invalid URL"):
        self.message = message
        super().__init__(self.message)

### More Production centric 
# class InvalidURLException(Exception):
#     """
#     Exception raised for invalid URLs.

#     Attributes:
#         message (str): The specific error message describing the invalid URL.
#     """

#     def __init__(self, message="URL is invalid"):
#         """
#         Initializes the exception with a descriptive error message.

#         Args:
#             message (str, optional): The specific error message. Defaults to "URL is invalid".
#         """
#         self.message = message
#         super().__init__(self.message)

#         # Additional attributes for logging or error handling in production:
#         self.url: str = None  # Store the invalid URL if available
#         self.error_code: int = None  # Optionally capture an error code

#     def set_url(self, url: str):
#         """
#         Sets the invalid URL associated with the exception.

#         Args:
#             url (str): The invalid URL.
#         """
#         self.url = url

#     def set_error_code(self, error_code: int):
#         """
#         Sets an error code associated with the exception.

#         Args:
#             error_code (int): The error code.
#         """
#         self.error_code = error_code

#     def __str__(self):
#         """
#         Provides a user-friendly string representation of the exception.

#         Returns:
#             str: The error message, optionally including the invalid URL and code.
#         """
#         error_message = self.message
#         if self.url:
#             error_message += f" (URL: {self.url})"
#         if self.error_code:
#             error_message += f" (Error code: {self.error_code})"
#         return error_message