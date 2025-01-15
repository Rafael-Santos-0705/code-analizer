__version__ = "0.0.1"

def create_app():
    from main import app

    app.version = __version__

    return app
