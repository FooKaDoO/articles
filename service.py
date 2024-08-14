from page_reader import PageReader
import data_parser

# Initialization

#Initialize PageReader with data_parser.process_page
page_reader = PageReader(process_function=data_parser.process_page)

# End of initialization

"""
Returns top 10 titles by number of comments from "https://jsonmock.hackerrank.com/api/articles?page={pageNr}".
"""
def get_top10_titles():
    pages = (page_reader
             .update_pages_data()
             .get_pages_data())
    return data_parser.get_top_10_titles_by_num_of_comments(pages)