import page_reader
import data_parser

"""
Returns top 10 titles by number of comments from "https://jsonmock.hackerrank.com/api/articles?page={pageNr}".
"""
def get_top10_titles():
    return (data_parser
            .get_top_10_titles_by_num_of_comments(
                    page_reader.get_pages_data()
                ))