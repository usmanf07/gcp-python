from typing import Any
import json


def hello_world(request: Any) -> Any:
    """HTTP Cloud Function.

    Returns:
    - "Hello World! 👋"
    """
    response = "Hello World! 👋"

    return response


def hello_name(request: Any) -> Any:
    """HTTP Cloud Function.

    Returns:
    - "Hello {NAME}! 🚀" if "name=NAME" is defined in the GET request
    - "Hello World! 🚀" otherwise
    """
    name = request.args.get("name", "World")
    response = f"Hello {name}! 🚀"

    return response


def python_powered(request: Any) -> Any:
    """HTTP Cloud Function.

    Returns:
    - The official "Python Powered" logo
    """
    # Load the binary image data from the file
    with open("python-powered.png", "rb") as image_file:
        image_data = image_file.read()

    return image_data
