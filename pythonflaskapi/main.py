import flask


def hello_world(request: flask.Request) -> flask.Response:
    """HTTP Cloud Function.

    Returns:
    - "Hello World! 👋"
    """
    response = "Hello World! 👋"

    return flask.Response(response, mimetype="text/plain")


def hello_name(request: flask.Request) -> flask.Response:
    """HTTP Cloud Function.

    Returns:
    - "Hello {NAME}! 🚀" if "name=NAME" is defined in the GET request
    - "Hello World! 🚀" otherwise
    """
    name = request.args.get("name", "World")
    response = f"Hello {name}! 🚀"

    return flask.Response(response, mimetype="text/plain")


def python_powered(request: flask.Request) -> flask.Response:
    """HTTP Cloud Function.

    Returns:
    - The official "Python Powered" logo
    """
    return flask.send_file("python-powered.png")
