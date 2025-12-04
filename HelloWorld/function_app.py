import azure.functions as func


app = func.FunctionApp()


@app.function_name("HelloWorld")
@app.route(route="hello")
def hello_world(req: func.HttpRequest) -> func.HttpResponse:
    """
    Azure Function that returns a Hello World message.
    
    Args:
        req: HttpRequest object
        
    Returns:
        HttpResponse with a greeting message
    """
    name = req.params.get('name', 'World')
    
    return func.HttpResponse(
        f"Hello, {name}!",
        status_code=200
    )
