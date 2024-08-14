# articles
Five solutions for a simple Python project that finds and returns the titles of the 10 articles with the most comments from all available data, in descending order of the number of comments. If an article is missing the title field, then the story title will be used, if the story title is also missing, then such article will be discarded altogether.<br>
<br>
Data from:
https://jsonmock.hackerrank.com/api/articles?page={page_number}

## How to run the development app
For the application to work correctly, it is important to follow the installation instructions.

### Creating a Python virtual environment
Creating a Python virtual environment ([venv](https://docs.python.org/3/library/venv.html)) is important so that packages would only be installed for the project.
<br>
To create a Python virtual environment, go to the project folder in the terminal and run the following command:
```
python -m venv venv
```

### Installing necessary packages
Firstly, activate the venv.

<b>

Windows:
</b>
```
C:\project_dir> venv\Scripts\activate
```
<b>

Linux/Mac:
</b>
```
project_dir$ source venv/bin/activate
```

<br>

Next up install the necessary packages for the project:
```
$ pip install -r requirements.txt
```

### Runnning the development app
To run the app in the Python Virtual Environment, run the following command:

```
flask run
```

## Running unit tests
Unit tests are used to check that the application is working as intended.
<br>
To run unit tests in the Python Virtual Environment, run the following command:
```
python -m unittest discover -s tests -p 'test_*.py'
```

## Other solutions
There are 4 other solutions to this project, which do not have unit tests.
1. complicated - uses pandas, possible to choose sorting, return, saved, replace values.
2. semi_complicated - uses pandas
3. using_page_reader_class - uses an object for reading pages
4. using_page_reader_yield - uses yield to read pages
First 2 solutions were created before the main solution, are incomplete and could be improved on by taking inspiration from the main project.<br>
PageReader object has unittests for it in the corresponding directory.

### Running the solutions
Run in the Python Virtual Environment by moving to the solution directory and running: 

```
flask run
```
