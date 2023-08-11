# Demo app to demonstrate how to set up maintenance mode in a web application


## This demo uses a simple, yet effective, Django application

The end user will be directed to a maintenance page if maintenance mode is turned on, or the home page if otherwise.

All the logic is handled using a custom middleware (maintenance/middleware.py) file. Then the middleware is registered in the settings.py file.