from flask import Flask, request
import json 
app = Flask("internal")

tutorials = {
    1: "Tutorial 1",
    2: "Tutorial 2",
    3: "Tutorial 3",
    4: "Tutorial 4",
    5: "Tutorial 5"
}

@app.route('/tutorials', methods=['GET'])
def get_tutorials():

    response = json.dumps(tutorials)
    
    return flask.Response(response, mimetype="application/json")

@app.route('/tutorials/<string:id>', methods=['GET'])
def get_tutorials_id(id):

    tutorial = tutorials.get(id)
    if tutorial:
        response = json.dumps({id: tutorial})
    else:
        response = json.dumps({"error": "Tutorial not found"})
    
    return flask.Response(response, mimetype="application/json")

def my_function(request):
    #Create a new app context for the internal app
    internal_ctx = app.test_request_context(path=request.full_path,
                                            method=request.method)
    
    #Copy main request data from original request
    #According to your context, parts can be missing. Adapt here!
    internal_ctx.request.data = request.data
    internal_ctx.request.headers = request.headers
    
    #Activate the context
    internal_ctx.push()
    #Dispatch the request to the internal app and get the result 
    return_value = app.full_dispatch_request()
    #Offload the context
    internal_ctx.pop()
    
    #Return the result of the internal app routing and processing      
    return return_value