from flask import Flask, request
#Define an internal Flask app
app = Flask("internal")
#Define the internal path, idiomatic Flask definition
@app.route('/user/<string:id>', methods=['GET', 'POST'])
def users(id):
    print(id)
    return id, 200
#Comply with Cloud Functions code structure for entry point
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