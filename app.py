from flask import Flask
import service

# Initialization

service.set_cols_to_return(
            'title',
        )
service.set_cols_to_keep(
            'num_comments',
        )
service.set_replace_cols(
            title='story_title',
        )

how_many_to_keep = 10
order_by = 'num_comments'

# End of initialization

# REST API endpoints
app = Flask(__name__)

@app.route("/")
def get_all_data():
    service.process_remaining_pages()
    return service.get_topN(how_many_to_keep, order_by)