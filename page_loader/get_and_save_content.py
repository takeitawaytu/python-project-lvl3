import requests


def get_content(url):
    content = requests.get(url)
    return content


def write(data, filepath):
    mode, encoding = ('w', 'utf8') if isinstance(data, str) else ('wb', None)
    with open(filepath, mode=mode, encoding=encoding) as f:
        f.write(data)
