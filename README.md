# Google Cloud Functions with Python Flask
## Steps for Configuration
- Step 1: Enable Cloud Functions API, Cloud Build API, Cloud Run API
- Step 2: Launch Google shell on cloud or cli
- Step 3: Put your code in main.py file: Calling function syntax
  ```
  def main(request):
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
  ```
  - A sample Routing synatx:
    ```
    from flask import Flask, request
    import json
    
    app = Flask("internal")
    #Define the internal path, idiomatic Flask definition
    @app.route('/getTutorials', methods=['GET'])
    def get_tutorials():
        response = json.dumps(tutorials)

    return (response, 200)
    ```
- Step 4: Run the command ```gcloud auth list``` for logging in
- Step 5: Select the project in gcloud using ```gcloud config list project```, if not assigned use ```gcloud config set project <projectname>```
- Step 6: Deploying command for gen2: ```gcloud functions deploy tutorialapi_new --gen2 --runtime=python311 --region=asia-east1 --source=. --entry-point=tutorialapi_new --trigger-http --max-instances=30 --allow-unauthenticated```
  - For gen1: Use the following: ```gcloud functions deploy tutorialapi_new --runtime=python311 --trigger-http --allow-unauthenticated```
