import pandas as pd
import io
import logging

from util import get_child

logger = get_child(__name__)


# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)


class DataProcess:
    def __init__(self, file: io.BytesIO | str):
        # self.file = '../resources/test_data.xls'
        self.required_columns = ['TICKET_ID', 'TMPLT_ID', 'STS', 'ADDED_DT']
        self.datetime_column_name = 'ADDED_DT'
        self.df: pd.DataFrame = self.load_file(file)

    # ['TICKET_ID', 'TICKET_CD', 'TMPLT_ID', 'TMPLT_NAME', 'STS', 'STG','ADDED_DT']
    @staticmethod
    def load_file(file: io.BytesIO | str) -> pd.DataFrame:
        df = pd.read_excel(file)
        logger.info("file was loaded")
        return df

    def check_column_datetime(self, _column_name: str):
        if not pd.api.types.is_datetime64_ns_dtype(self.df[_column_name]):
            logger.info("Converting the datetime column to proper format")
            self.df[_column_name] = pd.to_datetime(self.df[_column_name])

    def required_data(self, _required_columns: list[str]):
        logger.info(f"taking only required columns:{_required_columns}")
        self.df[_required_columns]

    def add_necessary_columns(self):
        self.df['year'] = self.df[self.datetime_column_name].dt.year
        self.df['month'] = self.df[self.datetime_column_name].dt.month_name()
        self.df['quarter'] = self.df[self.datetime_column_name].dt.quarter.map(lambda x:f"Q{x}")
        logger.info("Adding the year, Month, quarter")

    @property
    def process(self):
        self.check_column_datetime(self.datetime_column_name)
        self.required_data(_required_columns=self.required_columns)
        self.add_necessary_columns()
        return self.df


class GraphProcess:

    @staticmethod
    def column_labeling(monthly_counts, quarterly_counts):
        # Combine monthly and quarterly data into a single DataFrame
        monthly_counts['type'] = 'Monthly'
        quarterly_counts['type'] = 'Quarterly'

        return monthly_counts, quarterly_counts

    def grouping(self, df) -> pd.concat:
        # monthly_counts = df.groupby(['year', 'month']).size().reset_index(name='count')
        monthly_counts = df.groupby(['year', 'month']).agg(Count=('TICKET_ID', 'count'))
        # quarterly_counts = df.groupby(['year', 'quarter']).size().reset_index(name='count')
        quarterly_counts = df.groupby(['year', 'quarter','month']).agg(Count=('TICKET_ID', 'count'))
        monthly_counts, quarterly_counts = self.column_labeling(monthly_counts, quarterly_counts)
        combined_counts = pd.concat([monthly_counts,
                                     quarterly_counts])
        return combined_counts, monthly_counts, quarterly_counts

# file = '../resources/test_data.xls'
# _df = DataProcess(file).process
#
# print(_df)
