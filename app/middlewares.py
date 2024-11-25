from starlette.middleware.exceptions import ExceptionMiddleware
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

def page_not_found_middleware(app):
    """
    Adds custom middleware to the Starlette app to handle undefined routes
    with a 404 response.
    """
    
    # for allowing requests from a different host
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # for giving 404 to unknown routess
    app.add_middleware(ExceptionMiddleware, handlers={
        404: lambda request: JSONResponse({"error": "Page not found"}, status_code=404),
    })
