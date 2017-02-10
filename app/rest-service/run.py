import sys
from app import app
import config

if (len(sys.argv) >=2):
    debug = sys.argv[1]
else:
    debug = True
app.run(
    debug=debug,
    host=config.host,
    port=config.port
)
