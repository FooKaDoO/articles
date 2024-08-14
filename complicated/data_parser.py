import pandas as pd
import numpy as np

class DataParser:
    def __init__(self):
        self.cols_to_return = []
        self.cols_to_keep = []
        self.replace_cols = dict()

    """
    Sets the columns to be returned from get_topN(N: int) to *args.
    Adds the columns also to cols_to_keep.
    """
    def set_cols_to_return(self, *args):
        self.cols_to_return = list(args)
        self.cols_to_keep = list(set(args).union(self.cols_to_keep))

    """
    Sets the columns to be kept after cleaning to the union of
    *args and columns to be returned.
    """
    def set_cols_to_keep(self, *args):
        self.cols_to_keep = list(set(args).union(self.cols_to_return))

    """
    Sets the replacement value columns in cleaning to **kwargs.
    key: value to be replaced
    value: replacement value
    """
    def set_replace_cols(self, **kwargs):
        self.replace_cols = kwargs


    """
    Cleans up DataFrame by values.
    """
    def clean_up_data(self, df: pd.DataFrame):        
        df[np.setdiff1d(self.cols_to_keep + list(self.replace_cols.values()),
                        df.columns)] = pd.NA
        
        for col1, col2 in self.replace_cols.items():
            df[col1] = (df[col1]
                        .replace(r'^\s*$', pd.NA, regex=True)
                        .fillna(df[col2]
                                .replace(r'^\s*$', pd.NA, regex=True)))
            df = df.dropna(subset=col1)
        
        return df[self.cols_to_keep]

    """
    Processes page data into a cleaned-up Pandas DataFrame.
    """
    def process_data(self, data_to_parse: dict):
        df = pd.json_normalize(data_to_parse)
        return self.clean_up_data(df)
    
    """
    Using cols_to_return gets the top N entries ordered by ordered_by.
    Does not update data.
    Data has to be updated manually using process_remaining_pages() beforehand.
    """
    def get_topN(self, df: pd.DataFrame, N: int, ordered_by: str):
        return df.sort_values(ordered_by, ascending=False).head(N)[self.cols_to_return].to_html(index=False)






