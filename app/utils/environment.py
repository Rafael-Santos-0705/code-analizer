import os
import re
import yaml
import json
import base64
from typing import Union, Any, List, Optional
#
from .checkers import Checkers

class Environment:
    """
    A utility class for managing environment variables, configuration files, and their associated values.
    """

    @staticmethod
    def is_development_mode() -> bool:
        """
        Check if the application is running in development mode based on the environment variable `NODE_ENV`.

        Returns:
            bool: True if the environment variable `NODE_ENV` starts with "dev" (case-insensitive), False otherwise.
        """
        mode = str(Environment.get("NODE_ENV", default=""))

        return mode.lower().startswith("dev")

    @staticmethod
    def value_to_dict(value: Union[str, bytes]) -> dict:
        """
        Convert a string or base64-encoded string to a dictionary.

        Args:
            value (Union[str, bytes]): The string or base64-encoded string to convert.

        Returns:
            dict: The resulting dictionary.

        Raises:
            ValueError: If the string cannot be converted to JSON.
        """
        try:
            if isinstance(value, bytes):
                value = value.decode('utf-8')

            if Checkers.is_base64(value):
                decoded_bytes = base64.b64decode(value)
                value = decoded_bytes.decode('utf-8')

            return json.loads(value)

        except Exception as e:
            raise ValueError(f"Error converting to a JSON dictionary: {e}")

    @staticmethod
    def get(name: str, default: Any = None, dict_obj: bool = False) -> Any:
        """
        Retrieve the value of an environment variable, with optional dictionary conversion.

        Args:
            name (str): The name of the environment variable.
            default (Any): The default value to return if the environment variable is not found.
            dict_obj (bool): If True, attempts to convert the value to a dictionary.

        Returns:
            Any: The value of the environment variable, or the default value if not found.

        Raises:
            ValueError: If the value cannot be converted to a dictionary when `dict_obj` is True.
        """
        buffer = os.getenv(name, default)

        if dict_obj and buffer:
            try:
                return Environment.value_to_dict(buffer)
            except Exception as e:
                raise ValueError(f"Error converting environment variable '{name}' to dictionary: {e}")

        return buffer

    @staticmethod
    def get_list(name: str, joker: Optional[str] = None) -> List[str]:
        """
        Retrieve a list of values from a comma-separated environment variable.

        Args:
            name (str): The name of the environment variable.
            joker (Optional[str]): An optional prefix to segregate values into two lists.

        Returns:
            List[str] or Tuple[List[str], List[str]]: A list of values if `joker` is not provided, or a tuple with two lists if `joker` is provided.
        """
        value = os.getenv(name)

        if value:
            values = value.split(',')

            if joker:
                low = [item for item in values if not item.startswith(joker)]
                high = [item[len(joker):] for item in values if item.startswith(joker)]

                return low, high

            return values

        return []

    @staticmethod
    def get_config(name: str) -> Optional[Any]:
        """
        Retrieve a JSON configuration from a file or environment variable.

        Args:
            name (str): The name of the environment variable containing the file path or raw JSON string.

        Returns:
            Any: The parsed JSON object, or None if the file doesn't exist or is not valid.

        Raises:
            ValueError: If the JSON cannot be parsed from the file or string.
        """
        filename = os.getenv(name)

        if filename is None:
            return Environment.get(f"{name}_RAW", dict_obj=True)

        if not os.path.exists(filename):
            return None

        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error parsing the JSON file '{filename}': {e}")
        except Exception as e:
            raise ValueError(f"Error loading the configuration file '{filename}': {e}")

    @staticmethod
    def path_exists(name: str) -> bool:
        """
        Check if a file path exists based on the value of an environment variable.

        Args:
            name (str): The name of the environment variable containing the file path.

        Returns:
            bool: True if the file path exists, False otherwise.
        """
        filename = os.getenv(name)

        return filename and os.path.exists(filename)

    @staticmethod
    def parse_yaml(file_path: str) -> dict:
        """
        Load a YAML file and replace placeholders with environment variables.

        Args:
            file_path (str): Path to the YAML file.

        Returns:
            dict: The YAML content with environment variables interpolated.

        Raises:
            FileNotFoundError: If the YAML file does not exist.
            ValueError: If the YAML file cannot be parsed or contains invalid variables.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The YAML file '{file_path}' does not exist.")

        env_var_pattern = re.compile(r"\$\{(\w+)\}")

        def replace_env_vars(value: str) -> str:
            """
            Replace placeholders in the format ${VAR_NAME} with the corresponding environment variable.

            Args:
                value (str): The string value to process.

            Returns:
                str: The processed string with environment variables replaced.
            """
            if isinstance(value, str):
                return env_var_pattern.sub(
                    lambda match: os.getenv(match.group(1), match.group(0)), value
                )

            return value

        with open(file_path, "r") as file:
            content = yaml.safe_load(file)

        def process_node(node):
            if isinstance(node, dict):
                return {key: process_node(val) for key, val in node.items()}
            elif isinstance(node, list):
                return [process_node(val) for val in node]
            else:
                return replace_env_vars(node)

        return process_node(content)
