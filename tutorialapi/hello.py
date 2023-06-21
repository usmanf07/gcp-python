import flask
import json

app = flask.Flask(__name__)

tutorials = {
    1: "Tutorial 1",
    2: "Tutorial 2",
    3: "Tutorial 3"
}

@app.route('/tutorials', methods=['GET'])
def get_tutorials():
    """HTTP Cloud Function.
    
    Returns:
    - A JSON response containing the tutorial list with names and IDs
    """
    response = json.dumps(tutorials)
    
    return response

@app.route('/tutorials/<int:id>', methods=['GET'])
def get_tutorial_by_id(id):
    """HTTP Cloud Function.
    
    Returns:
    - A JSON response containing the tutorial with the specified ID
    - If the ID is not found, returns a JSON response with an error message
    """
    tutorial = tutorials.get(id)
    if tutorial:
        response = json.dumps({id: tutorial})
    else:
        response = json.dumps({"error": "Tutorial not found"})
    
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
