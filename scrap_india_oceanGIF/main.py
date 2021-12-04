import requests
from datetime import datetime
import os

OUTPUT_FOLDER = 'output'
class BaseOcean:
    def __init__(self):
        self.images_names: list = []
        self.url: str = ''
        self.timed_stamps = ['0230', '0530', '0830', '1130', '1430', '1730', '2030', '2330']

    @property
    def run(self):
        """Holds the logic to run the class"""
        pass

    # todo: Genearate the ocean current filenames.
    def generate_names(self):
        pass

    # todo: download the images with the created names.
    def download_images(self):
        pass

    # todo: saved the images in a folder.
    def saved_the_images(self):
        pass


class WaveForcast(BaseOcean):
    def __init__(self):
        BaseOcean.__init__(self)
        self.url = 'https://incois.gov.in/OSF_FILES/forecast/coastal/andhra/swh/'

    def generate_names(self):
        today_date = datetime.now().strftime(format='%d-%m-%Y')
        for i in self.timed_stamps:
            self.images_names.append(f"{today_date}--{i}.gif")

    def download_images(self, imagename: str):
        build_url = self.url + imagename
        with requests.get(build_url) as req_data:  # context manager type syntax
            if req_data.ok:
                with open(os.path.join(OUTPUT_FOLDER,imagename), 'bw') as file_data:
                    file_data.write(req_data.content)


    @property
    def run(self):
        self.generate_names()
        for i in self.images_names:
            self.download_images(imagename=i)


if __name__ == '__main__':
    var = WaveForcast()
    var.run
