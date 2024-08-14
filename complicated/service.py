from page_reader import PageReader
from data_parser import DataParser


# Initialization
page_reader = PageReader(lambda page_number : f"https://jsonmock.hackerrank.com/api/articles?page={page_number}")
# End of initialization

def get_top_10_titles_by_num_comments():
    pages = page_reader.get_updated_pages_data()
    data_parser = DataParser()
    data_parser.set_cols_to_return(
                'title',
            )
    data_parser.set_cols_to_keep(
                'num_comments',
            )
    data_parser.set_replace_cols(
                title='story_title',
            )
    df = data_parser.process_data(pages)
    return data_parser.get_topN(df, 10, 'num_comments')