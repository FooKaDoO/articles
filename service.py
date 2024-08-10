import pandas as pd
import numpy as np
import requests

URL = lambda page_number : f"https://jsonmock.hackerrank.com/api/articles?page={page_number}"

page_number = 0
articles = pd.DataFrame()
session = requests.Session()

cols_to_return = []
cols_to_keep = []
replace_cols = dict()

"""
Sets the columns to be returned from get_topN(N: int) to *args.
Adds the columns also to cols_to_keep.
"""
def set_cols_to_return(*args):
    global cols_to_return, cols_to_keep
    cols_to_return = list(args)
    cols_to_keep = list(set(args).union(cols_to_keep))

"""
Sets the columns to be kept after cleaning to the union of
*args and columns to be returned.
"""
def set_cols_to_keep(*args):
    global cols_to_keep, cols_to_return
    cols_to_keep = list(set(args).union(cols_to_return))

"""
Sets the replacement value columns in cleaning to **kwargs.
key: value to be replaced
value: replacement value
"""
def set_replace_cols(**kwargs):
    global replace_cols, cols_to_keep
    replace_cols = kwargs

"""
Gets the total pages count
"""
def get_total_pages():
    global session
    json = (session
            .get(URL(1))
            .json())
    return json['total_pages']

"""
Cleans up DataFrame by values 
cols_to_return, cols_to_keep, replace_cols.
"""
def clean_up_data(df: pd.DataFrame):
    global cols_to_return, cols_to_keep, replace_cols
    
    df[np.setdiff1d(cols_to_keep + list(replace_cols.values()),
                     df.columns)] = pd.NA
    
    for col1, col2 in replace_cols.items():
        df[col1] = (df[col1]
                    .replace(r'^\s*$', pd.NA, regex=True)
                    .fillna(df[col2]
                            .replace(r'^\s*$', pd.NA, regex=True)))
        df = df.dropna(subset=col1)
    return df[cols_to_keep]

"""
Processes page data into a cleaned-up Pandas DataFrame.
"""
def process_data(data):
    global articles
    articles = pd.concat(
        [articles, clean_up_data(
                    pd.json_normalize(data))
        ], ignore_index = True)

"""
Checks the total pages number and yields the remaining pages.
"""
def get_pages():
    global page_number, session
    total_pages = get_total_pages()

    while page_number < total_pages:
        page_number += 1
        yield (session
                .get(URL(page_number))
                .json())['data']

"""
Processes all remaining pages.
"""
def process_remaining_pages():
    remaining_data = []
    for page in get_pages():
        remaining_data.append(page)

    if len(remaining_data) > 0:
        process_data([x for y in remaining_data for x in y])

"""
Using cols_to_return gets the top N entries ordered by ordered_by.
Does not update data.
Data has to be updated manually using process_remaining_pages() beforehand.
"""
def get_topN(N: int, ordered_by: str):
    global articles
    return articles.sort_values(ordered_by, ascending=False).head(N)[cols_to_return].to_html(index=False)