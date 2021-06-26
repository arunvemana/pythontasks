from pathlib import Path
import pandas as pd
import pycountry
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Union, NoReturn
from report_generator import Report,full_path





class Run:
    """
    Functionality:
    1. Read the data from the given input data set.
    2. Generate of two predefined graphs save as `test`, `test2` in png format.
    """
    def __init__(self, file_path: Union[Path, str]):
        try:
            self.data = pd.read_csv(file_path)
            self.formatting_data()
        except FileNotFoundError as e:
            raise FileNotFoundError(
                f"Please check the given filepath of dataset:{file_path}") \
                from e

    @staticmethod
    def country_there(country: str) -> bool:
        """
        Take the country as str and return Bool depends that str is actually
        Country or not
        :param country: str
        :return: Bool
        """
        try:
            pycountry.countries.search_fuzzy(country)
            return True
        except LookupError:
            return False

    def formatting_data(self) -> NoReturn:
        """
        Changes/modification in the dataset which was read from the file,

        :return: None
        """
        self.data = pd.melt(
            frame=self.data,
            id_vars=['Country'],
            var_name='Year',
            value_name='Emission'
        )
        # Todo: taking more time to figure out country is actual country or not
        _country_there = [value for value in self.data['Country'].unique() if
                          not self.country_there(value)]
        self.data = self.data[~self.data['Country'].isin(_country_there)]
        self.data['Year'] = pd.to_datetime(self.data['Year'])

    def graph_emission_years(self) -> NoReturn:
        """
        Generation of graph for years of emission.
        and saved as test.png
        :return: None
        """
        df_temp = self.data.copy()
        plt.figure(figsize=(20, 15))
        sns.set_theme(style="whitegrid")
        sns.lineplot(
            data=df_temp,
            x='Year',
            y='Emission'
        )
        plt.savefig(full_path('./output/test.png'), bbox_inches='tight')

    def graph_top10_emissions(self) -> NoReturn:
        """
        Generation of graph for top10 country vs emission,
        and saved as test2.png
        :return:
        """
        df_temp = self.data.copy()
        # save the top 10 most polluting countries in a new list
        top_10 = \
            df_temp.groupby('Country')[
                'Emission'].sum().reset_index().sort_values(
                by=['Emission'], ascending=False).head(10)['Country'].to_list()
        for country in top_10:
            plt.plot(df_temp[df_temp['Country'] == country]['Year'],
                     df_temp[df_temp['Country'] == country]['Emission'],
                     label=country)
        plt.legend()
        plt.savefig(full_path('./output/test2.png'), bbox_inches='tight')


if __name__ == '__main__':
    _run = Run(file_path=full_path('./data/emission data.csv'))
    _run.graph_emission_years()
    _run.graph_top10_emissions()
    var = Report()
    var.cover_page()
    var.graphs("Emission through out years", "test.png")
    var.graphs("Top 10 Emission amount by Country", "test2.png")
    var.output(full_path('./output/test.pdf'))
