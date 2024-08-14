from page_reader import PageReader
import data_parser

# Initialization
page_reader = PageReader()

def get_top10_titles():
    pages = page_reader.get_updated_pages_data()
    df = data_parser.process_data(pages)
    return data_parser.get_top10(df)