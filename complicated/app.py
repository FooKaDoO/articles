from flask import Flask
import service as service



# REST API endpoints
app = Flask(__name__)

@app.route("/")
def get_all_data():
    return service.get_top_10_titles_by_num_comments()