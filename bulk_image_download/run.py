import sys
import pathlib
import argparse
import requests
import uuid
import shutil
import os
from time import perf_counter_ns
from concurrent.futures import ThreadPoolExecutor
from typing import Union, List, ByteString


def timeit(method):
    def timed(*args, **kw):
        start = perf_counter_ns()
        result = method(*args, **kw)
        end = perf_counter_ns()
        print(end - start)
        return result

    return timed


def get_url_from_file(filepath: pathlib.Path) -> List[str]:
    with open(filepath) as urls:
        list_urls = urls.readlines()
        list_urls = [urls.rstrip() for urls in list_urls]
    return list_urls


def get_the_data(url: str) -> ByteString:
    data = requests.get(url, stream=True)
    return data


@timeit
def save_the_image(urls: List[str], output_path: pathlib.Path):
    # Threading
    with ThreadPoolExecutor() as exe:
        result = exe.map(get_the_data,urls)
    # for url in urls:
    for data in result:
        # data = requests.get(url, stream=True)
        # data = get_the_data(url)
        if data.status_code == 200:
            data.raw.decode = True
            image_path = os.path.join(output_path, f"{str(uuid.uuid4())}.jpg")
            with open(image_path, 'wb') as f:
                shutil.copyfileobj(data.raw, f)


def run(filename: pathlib.Path, output_path: pathlib.Path):
    print(filename)
    urls = get_url_from_file(filepath=filename)
    print(urls)
    save_the_image(urls, output_path)


def input_parsing() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str,
                        help="To get the urls from given path.")
    parser.add_argument("output", type=str,
                        help="folder path to save the images")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    file_path = input_parsing()
    run(file_path.input, file_path.output)
