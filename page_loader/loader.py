import os
import requests
from urllib.parse import urlparse
import re

DOMAIN_PATTERN = r'^([^http|\/\/][\w]*[\.|\/].+)'


def download(url, output_dir, ext='.html'):
    filename = get_output_filename(url)
    page_content = requests.get(url)
    dir_to_save = os.path.join(output_dir, filename + ext)
    with open(dir_to_save, 'w', encoding='UTF8') as file:
        file.write(page_content.text)
    return dir_to_save


def get_output_filename(url):
    parse_url = urlparse(url)
    unformatted_filename = str(parse_url[1] + parse_url[2]).strip('/')
    filename = re.sub(r'[\W_]', '-', unformatted_filename)
    return filename
