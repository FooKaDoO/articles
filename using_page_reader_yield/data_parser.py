"""
Returns article title.
Input article must be of type dict.

If article does not have title, uses article story_title.
If article does not have story_title, return None.
"""
def get_title(article: dict):
    assert isinstance(article, dict)
    if (article.get("title") != '' and 
        isinstance(article.get("title"), str)):
        return article["title"]
    
    if (article.get("story_title") != '' and 
        isinstance(article.get("story_title"), str)):
        return article["story_title"]
    return None

"""
Returns article's number of comments.
Input article must be of type dict.

If number of comments is not int type, return 0.
"""
def get_num_comments(article: dict):
    assert isinstance(article, dict)
    if isinstance(article.get("num_comments"), int):
        return article["num_comments"]
    return 0

"""
Returns cleaned up article data.
Input article must be a dictionary.

Returns a dictionary with 2 key-value pairs:
"title": None | str
"num_comments": int
"""
def clean_up_data(article: dict):
    assert isinstance(article, dict)
    return {
        "title": get_title(article),
        "num_comments": get_num_comments(article),
    }

"""
Returns the result of cleaning up a page's articles and 
filtering out articles with no title.

Input is a page which is a list of articles.
Each article must be a dictionary.
"""
def process_page(page: list):
    assert isinstance(page, list)
    return list(filter(
            lambda article: article["title"] != None,
            [clean_up_data(article) for article in page]
        ))

"""
Returns top 10 articles by number of comments.
Input data is a list of articles, where each article must have 2 key-value pairs:
"title": <any_type>
"num_comments": <type_of_int>
"""
def get_top_10_titles_by_num_of_comments(data: list):
    assert isinstance(data, list)
    data.sort(
        key=lambda article: article["num_comments"],
        reverse=True
    )
    return [article["title"] for article in data][:10]