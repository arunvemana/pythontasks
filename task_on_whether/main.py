import requests
import json
from typing import Union, Dict, List, Type, Tuple
from enum import Enum
import pandas as pd
from datetime import datetime

TypeJSON = Union[Dict[str, 'JSON'], List['JSON'], int, str, float, bool, Type[None]]


class WeHaveIssue(Exception):
    pass


class CapitalTODivision(Enum):
    london = 'england-and-wales'
    belfast = 'northern-ireland'
    edinburgh = 'scotland'
    cardiff = 'england-and-wales'


class Main:
    def __init__(self):
        self.base_url = "https://www.metaweather.com/api/"
        self.bank_url = "https://www.gov.uk/bank-holidays.json"
        self.location, self.year = self.ask_input()
        self.weoid: int = 0
        self.collected_dataframe = self.process_data()

    def get_request(self, endpoint: str, params: dict = None) -> List[TypeJSON]:
        data = requests.get(self.base_url + endpoint, params=params)
        return data.json()

    def get_holidays_list(self, division: str) -> dict:
        try:
            data = requests.get(self.bank_url)
            data = data.json()[division]
            return data['events']
        except KeyError as _:
            raise WeHaveIssue("Given division not present in the response!")

    def ask_input(self) -> Tuple[str]:
        """
        locaton : get's the woeid to call for remaning api's
        """
        location = input('which location?->')
        year = input("which year u want to look at?-->")
        return location, year

    def load_holidays_to_df(self, data: List[dict]):
        df = pd.DataFrame(data)
        return df

    def get_max_min_temp_for_a_date(self, date) -> Tuple[float, float]:
        endpoint = f"/location/{self.weoid}/{date.replace('-', '/')}"
        whether_data = self.get_request(endpoint)
        high_low_list = [(i.get('max_temp', None), i.get('min_temp', None)) for i in whether_data]
        try:
            high, low = list(zip(*high_low_list))
        except ValueError as _:
            raise WeHaveIssue(f"Api endpoint doesn't have data for this date{date} or some issue here ")
        return max(high), min(low)

    def process_data(self):
        try:
            division = CapitalTODivision[self.location].value
            holidays_data = self.get_holidays_list(division)
        except KeyError as e:
            raise WeHaveIssue("we can't figure the division of given capital name, check it", e)
        data = self.get_request("/location/search/?", {'query': self.location})
        self.weoid = data[0]['woeid']  # take location id from the api
        holidays_data: pd.DataFrame = self.load_holidays_to_df(holidays_data)
        holidays_data = holidays_data.iloc[:, :-2]
        for index, row in holidays_data.iterrows():
            max_temp, min_temp = None, None
            if datetime.strptime(row['date'], '%Y-%m-%d') <= datetime.now():
                max_temp, min_temp = self.get_max_min_temp_for_a_date(row['date'])
            holidays_data.loc[index, "max_temp"] = max_temp
            holidays_data.loc[index, "min_temp"] = min_temp

        print(holidays_data)
        holidays_data.to_csv("each_holiday with temps.csv")
        return holidays_data


if __name__ == '__main__':
    try:
        fireit = Main()
    except WeHaveIssue as e:
        print(e)
