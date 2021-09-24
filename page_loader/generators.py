from urllib.parse import urlparse, urlunparse
from bs4 import BeautifulSoup
import re
import os

CONTENT_TYPES = ('page', 'image')
PAGE_PATTERN = r'[\W_]'


def get_new_name(url, ext='.html'):
    parsed_url = urlparse(url)
    unformatted_filename = str(parsed_url[1] + parsed_url[2]).strip('/')
    filename = re.sub(PAGE_PATTERN, '-', unformatted_filename)
    return filename + ext


def create_dir(url, path):
    dirname = get_new_name(url, ext='_files')
    path_to_dir = os.path.join(path, dirname)
    os.makedirs(path_to_dir, exist_ok=True)
    return path_to_dir


def generate_url(url, filename):
    return os.path.join(url, filename)


def generate_path(dir_name, filename):
    name, ext = os.path.splitext(filename)
    filename = get_new_name(name, ext)
    return os.path.join(dir_name, filename)


def parse_url(url):
    parsed_url = urlparse(url)
    domain_name = os.path.join('https://', parsed_url.netloc.strip('/'))
    if parsed_url.netloc == '':
        domain_name = os.path.join('https://', url)
        return url, domain_name
    elif parsed_url.netloc.startswith('www'):
        path = urlunparse(parsed_url._replace(
            scheme='',
            netloc=parsed_url.netloc[4:],
        ),
        ).strip('/')
        return path, domain_name
    path = urlunparse(parsed_url._replace(scheme='')).strip('/')
    return path, domain_name
