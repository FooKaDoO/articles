from flask import Flask
import service

# REST API endpoints
app = Flask(__name__)

@app.route("/")
def get_all_data():
    return service.get_top10_titles()