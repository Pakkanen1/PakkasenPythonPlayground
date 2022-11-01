"""Create an application instance."""
from pakkasboxi.app import create_app
from pakkasboxi.settings import DevConfig

CONFIG = DevConfig

app = create_app(CONFIG)
