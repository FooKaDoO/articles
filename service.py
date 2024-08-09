import pandas as pd
import numpy as np
import requests

URL = lambda page_number : f"https://jsonmock.hackerrank.com/api/articles?page={page_number}"

page_number = 0
articles = pd.DataFrame()

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
    global replace_cols
    replace_cols = kwargs

"""
Gets the total pages count
"""
def get_total_pages():
    res = requests.get(URL(1))
    json = res.json()
    return json['total_pages']

"""
Gets the page data on given page number.
"""
def get_page(page_number: int):
    res = requests.get(URL(page_number))
    json = res.json()
    return json['data']

"""
Increments the page number, gets the data from that page
and appends the cleaned up data to the articles dataframe.
"""
def get_next_page():
    global page_number, articles
    page_number += 1

    next_page_data = get_page(page_number)
    df_next_page_data = pd.json_normalize(next_page_data)
    df_next_page_data = clean_up_data(df_next_page_data)
    
    articles = pd.concat([articles, df_next_page_data], 
                         ignore_index = True)

"""
Cleans up dataframe by values 
cols_to_return, cols_to_keep, replace_cols.
"""
def clean_up_data(df: pd.DataFrame):
    global cols_to_return, cols_to_keep, replace_cols
    
    df = df.replace(r'^\s*$', np.nan, regex=True)

    for col in cols_to_keep:
        if col not in df.columns:
            df[col] = np.nan
    
    for col, replace_col in replace_cols.items():
        if replace_col in df.columns:
            df[col] = df[col].fillna(value=df[replace_col])
    
    df = df[cols_to_keep]
    df = df.dropna(subset=cols_to_return)

    return df

"""
Checks the total pages number and updates data frame for
each remaining page.
"""
def get_remaining_pages():
    global page_number
    total_pages = get_total_pages()

    while page_number < total_pages:
        get_next_page()

"""
Using cols_to_return gets the top N entries ordered by ordered_by.
Does not update data.
Data has to be updated manually using get_remaining_pages() beforehand.
"""
def get_topN(N: int, ordered_by: str):
    global articles
    return articles.sort_values(ordered_by, ascending=False).head(N)[cols_to_return].to_html(index=False)