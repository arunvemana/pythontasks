import requests
import re
import os
import bs4
from datetime import datetime
import shutil

base_url = "https://www.regelleistung.net/ext/data/?lang=en"
output_path = 'output'


def download_file(tsoid: str, datatype: str):
    today_date = datetime.now().strftime(format='%d.%m.%Y')
    payload = {'from': today_date,
               'to': today_date,
               'download': 'true',
               '_download': 'on',
               'tsoId': tsoid,
               'dataType': datatype}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'}
    _response = requests.post(base_url, data=payload, headers=headers)
    print(_response.status_code)
    print(_response.headers['Content-Disposition'])
    filename = re.search(r'\".*\"', _response.headers['Content-Disposition']).group()
    print(filename)
    filename = filename.replace('"', "")
    if _response.status_code == 200:
        with open(os.path.join(output_path, filename), 'w') as f:
            f.write(_response.text)


def get_drop_down_details():
    raw_data = requests.get(base_url)
    if raw_data.status_code == 200:
        soup_data = bs4.BeautifulSoup(raw_data.text, 'html.parser')
        tso_drop_down = soup_data.find(id="form-tso")
        # print(tso_drop_down)
        _tso = {}
        for i in tso_drop_down.findAll('option'):
            _tso[i.text] = i['value']
        datatype_drop_down = soup_data.find(id="form-type")
        _datatype = {}
        for i in datatype_drop_down.findAll('option'):
            _datatype[i.text] = i['value']

        return _tso, _datatype


def what_to_download(tso: dict, datatype: dict):
    choices = input("auto or userchoice by 1 and 2 ")
    if choices == '1':
        for each_tso in tso:
            for each_type in datatype:
                download_file(tso.get(each_tso), datatype.get(each_type))

    elif choices == '2':
        print("Provide the dropdown details")
        _tso = input("enter the tso key")
        _datatype = input("enter the datatype key")
        if tso.get(_tso) and datatype.get(_datatype):
            download_file(tso.get(_tso), datatype.get(_datatype))


def merge_the_csv():
    files_list = os.listdir(os.path.join('output'))
    print(files_list)
    output_filename = f"Single_file_on_{datetime.now().strftime(format='%d.%m.%Y')}.csv"
    with open(output_filename, 'a') as main_file:
        for i in files_list:
            data = []
            with open(os.path.join(output_path, i), 'r') as sub_file:
                data = sub_file.readlines()

            main_file.writelines(data)
            main_file.write('\n')
    return os.path.abspath(output_filename)


def clear_the_folder():
    shutil.rmtree(os.path.join(output_path))


def create_the_folder():
    try:
        os.mkdir(os.path.join(output_path))
    except FileExistsError:
        pass


if __name__ == '__main__':
    create_the_folder()
    tso, datatype = get_drop_down_details()
    what_to_download(tso, datatype)
    where_is_saving = merge_the_csv()
    print(f"saved data path is {where_is_saving}")
    clear_the_folder()
