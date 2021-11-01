import re
import os
import logging
from urllib.parse import urlparse, urlunparse

PAGE_PATTERN = r'[\W_]'
LINK_PATTERN = r'[^a-zA-Z0-9\.]'


def generate_name(url, ext='.html', is_link=False):
    parsed_url = urlparse(url)
    if is_link:
        unformatted_filename = str(parsed_url[1] + parsed_url[2]).strip('/')
        filename = re.sub(LINK_PATTERN, '-', unformatted_filename)
        return filename
    unformatted_filename = str(parsed_url[1] + parsed_url[2].split('.')[0])\
        .strip('/')
    filename = re.sub(PAGE_PATTERN, '-', unformatted_filename)
    return filename + ext


def create_dir(url, path):
    dirname = generate_name(url, ext='_files')
    path_to_dir = os.path.join(path, dirname)
    try:
        os.makedirs(path_to_dir, exist_ok=True)
    except OSError as e:
        logging.debug(f'An error occurred: {e}', exc_info=True)
        logging.error(f'Can`t create directory {path_to_dir}, because {e}')
    else:
        return path_to_dir


def generate_url(url, filename):
    if os.name == 'nt':
        return str(url) + '/' + str(filename)
    return os.path.join(url, filename)


def generate_path(dir_name, filename):
    name, ext = os.path.splitext(filename)
    formatted_filename = generate_name(name, ext)
    if os.name == 'nt':
        return os.path.relpath(dir_name) + '/' + formatted_filename
    return os.path.relpath(os.path.join(dir_name, formatted_filename))


def parse_url(url):
    parsed_url = urlparse(url)
    domain_name = os.path.join('https://', parsed_url.netloc.strip('/'))
    if parsed_url.netloc == '':
        domain_name = os.path.join('https://', url)
        return url, domain_name, parsed_url.netloc, parsed_url.path
    elif parsed_url.netloc.startswith('www'):
        path = urlunparse(parsed_url._replace(
            scheme='',
            netloc=parsed_url.netloc[4:],
        ),
        ).strip('/')
        return path, domain_name, parsed_url.netloc, parsed_url.path
    path = urlunparse(parsed_url._replace(scheme='')).strip('/')
    return path, domain_name, parsed_url.netloc, parsed_url.path
