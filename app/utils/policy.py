import os
#

class Policy:
    """
    A utility class for managing policy-related operations, 
    such as retrieving allowed origins for an application.
    """

    @staticmethod
    def origins(app_url:str = None) -> list[str]:
        """
        Retrieve a list of allowed origins for the application.

        Args:
            app_url (str, optional): An optional URL to include in the origins list.

        Returns:
            list[str]: A list of origins. If the environment variable `APP_ORIGINS` 
            is defined, its value is split by ", " to create the list. If `app_url` 
            is provided, it is included at the start of the list.
        """
        origins_str = os.getenv("APP_ORIGINS")
        result = []

        if app_url:
            result.append(app_url)

        if isinstance(origins_str, str):
            result = origins_str.split(", ")

        return result
