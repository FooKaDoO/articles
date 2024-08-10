# articles
An overly complicated solution for a simple Python project that finds and returns the titles of the 10 articles with the most comments from all available data, in descending order of the number of comments. If an article is missing the title field, then the story title will be used, if the story title is also missing, then such article will be discarded altogether.<br>
<br>
Data from:
https://jsonmock.hackerrank.com/api/articles?page={page_number}

## How to run the development app
Optional: create a Python virtual environment ([venv](https://docs.python.org/3/library/venv.html)) so packages would only be installed for the project.<br>
<br>
Installing the necessary packages for the project:
```
$ pip install -r requirements.txt
```
Running the development app:
```
$ flask run
```