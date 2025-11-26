"""Example of flask main file."""
from flask import Flask
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
# Configure log level
app.logger.setLevel(logging.INFO)

# Create file handler with rotation
file_handler = RotatingFileHandler('/tmp/logs/app.log', maxBytes=10240, backupCount=5)
file_handler.setLevel(logging.INFO)

@app.route('/api/hello')
def hello_world():
    """Returns Hello, EDP!"""
    return 'Hello, EDP!'


if __name__ == '__main__':
    app.run()
