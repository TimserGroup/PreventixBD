from flask import Flask

from pacientes import pacientes
import pandas as pd

# Application initializations
app = Flask(__name__)

# settings
app.secret_key = "mysecretkey"

app.register_blueprint(pacientes)

# starting the app
if __name__ == "__main__":
    app.run(port=5000, debug=False)
