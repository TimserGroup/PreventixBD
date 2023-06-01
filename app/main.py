from app import app
from pacientes import pacientes
import pandas as pd

app.register_blueprint(pacientes)

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)