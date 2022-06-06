_dict = {'name': 'aaa',
         'age': 'bbb',
         'state': {'head quartres': 'name1', 'corporation': 'name2'}
         }


def there(key: str, data: dict):
    if data.get(key):
        return data[key]
    else:
        for second_key in data.keys():
            if isinstance(data[second_key], dict):
                return there(key, data[second_key])
        return None


def rev_dict(data: dict, temp: dict = {}):
    for k, v in data.items():
        if isinstance(v, dict):
            temp[str(v)] = k
            return rev_dict(v, temp)
        else:
            temp[v] = k

    return temp


give_input = input("provide key or value!")
var = there(give_input, _dict)
if not var:
    _rev_dict = rev_dict(_dict)
    var = there(give_input, _rev_dict)
    print(var)
else:
    print(var)
