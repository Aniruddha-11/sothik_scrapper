from flask import Flask
from file_api import file_api
import os

# Create the main Flask app
app = Flask(__name__)

# Register blueprints
app.register_blueprint(file_api)


if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)