import re
import os
import logging
from urllib.parse import urlparse, urlunparse
from page_loader.get_and_save_content import SysError

PAGE_PATTERN = r'[\W_]'
LINK_PATTERN = r'[^a-zA-Z0-9]'
URL_PATTERN = re.compile(r'^https?://')


def generate_name(url, ext='.html', is_link=False):
    parsed_url = urlparse(url)
    if is_link:
        parsed_url = parse_url(url)[0]
        unformatted_filename, ext = os.path.splitext(parsed_url)
        ext = '.html' if ext == '' else ext
        filename = re.sub(
            LINK_PATTERN,
            '-',
            modify_content_path(unformatted_filename)
        )
        return filename + ext
    unformatted_filename = str(parsed_url[1] + parsed_url[2].split('.')[0])\
        .strip('/')
    filename = re.sub(
        PAGE_PATTERN,
        '-',
        unformatted_filename
    )
    return filename + ext


def modify_content_path(path):
    if str(path).startswith('/'):
        return path[1:]
    return path


def create_dir(url, path):
    dirname = generate_name(url, ext='_files')
    path_to_dir = os.path.join(path, dirname)
    try:
        os.mkdir(path_to_dir)
        logging.debug(f'directory {path_to_dir} was created')
    except (
            OSError,
            PermissionError,
    ) as e:
        logging.debug(f'An error occurred: {e}', exc_info=True)
        logging.error(f'Can`t create directory {path_to_dir}, because {e}')
        raise SysError() from e
    else:
        return path_to_dir, dirname


def generate_url(url, filename):
    if os.name == 'nt':
        return str(url) + '/' + str(filename)
    return os.path.join(url, filename)


def generate_path(dir_name, filename):
    if os.name == 'nt':
        return os.path.relpath(dir_name) + '/' + filename
    return os.path.relpath(os.path.join(dir_name, filename))


def parse_url(url):
    parsed_url = urlparse(url)
    domain_name = os.path.join('http://', parsed_url.netloc.strip('/'))
    if parsed_url.netloc == '':
        domain_name = os.path.join('http://', url)
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
