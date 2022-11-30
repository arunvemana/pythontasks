import bs4.element
import requests
from bs4 import BeautifulSoup as BS
import pandas as pd

url = "https://www.moneycontrol.com/stocks/marketstats/bsetopdiv/"


def get_html_content(url: str):
    data = requests.get(
        url=url
    )
    if data.status_code == 200:
        raw_data = BS(data.content, 'html.parser')
        parser_data = raw_data.find('div', class_='columnst FR wbg brdwht').find('table')
        print(parser_data)
        dataframe = pd.read_html(str(parser_data))
        dataframe[0].to_csv('test.csv')
        print(dataframe[0].columns)
    else:
        print(data.status_code, "error")


if __name__ == '__main__':
    get_html_content(url)
