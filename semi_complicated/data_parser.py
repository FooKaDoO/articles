import pandas as pd

"""
Cleans up DataFrame by values.
"""
def clean_up_data(df: pd.DataFrame):
    df = (df
            .reindex(columns=["title", "story_title", "num_comments"])
            .replace('', pd.NA))
    
    df.num_comments = (df.num_comments
                        .fillna(0))

    df.title = (df.title
                .fillna(df.story_title))
    
    return (df
            .dropna(subset="title")
            [["title", "num_comments"]])

"""
Processes page data into a cleaned-up Pandas DataFrame.
"""
def process_data(data: dict):
    new_df = pd.json_normalize(data)
    return clean_up_data(new_df)

"""

"""
def get_top10(df: pd.DataFrame):
    return (df
            .sort_values("num_comments", ascending=False)
            .head(10)
            .title
            .to_list())
