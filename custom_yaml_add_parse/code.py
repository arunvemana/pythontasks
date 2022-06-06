import re
import sys


FORMATED_HOST = "\t- hostname:'{hostname}'\n\tlocations:\n"
FORMATED_PORTS = '\t\t{version}:"{port}"\n'


def find_position():
    with open("sample_in.yaml", "r") as stream:
        try:
            cp = 0
            while True:
                ret = next(stream)
                cp += ret.__len__()
                if re.match('^profile::antcandy::location:\n', ret):
                    break
            return cp

        except Exception as exc:
            print(exc)


def write_data(seek_bytes: int, input_str: str):
    with open("sample_in.yaml", "a+") as stream:
        stream.seek(seek_bytes)
        stream.write(input_str)


def process_args(hostname, ports):
    print(hostname, ports)
    str1 = FORMATED_HOST.format(hostname=hostname)
    str2 = ''
    for port in ports.split(','):
        version, port = port.split(':')
        str2 += FORMATED_PORTS.format(version=version, port=port)

    return str1+str2


if __name__ == '__main__':
    #  python .\code.py 'qcant.playerzpot.com' 'v1:3002, v2:3003'
    hostname = sys.argv[1]
    ports = sys.argv[2]
    o_p = process_args(hostname, ports)
    f_seek = find_position()
    write_data(f_seek, o_p)
