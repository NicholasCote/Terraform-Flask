# Import the flask python module
from flask import Flask

# Define the Flask constructor
app = Flask(__name__)

from tf_flask.k8s import views