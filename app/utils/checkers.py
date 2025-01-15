import base64
#

class Checkers:
    """
    A utility class for performing various validation checks.
    """

    @staticmethod
    def is_base64(string: str) -> bool:
        """
        Check if a given string is a valid Base64-encoded string.

        Args:
            string (str): The string to validate.

        Returns:
            bool: True if the string is a valid Base64-encoded string, False otherwise.

        Notes:
            - The method decodes the string and re-encodes it to ensure it matches the original.
            - Returns False if the string cannot be decoded as Base64 or if any error occurs during validation.
        """
        try:
            return base64.b64encode(base64.b64decode(string)) == string.encode()
        except Exception:
            return False
