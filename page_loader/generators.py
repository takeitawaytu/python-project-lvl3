from urllib.parse import urlparse, urlunparse
import re
import os

PAGE_PATTERN = r'[\W_]'


def generate_name(url, ext='.html'):
    parsed_url = urlparse(url)
    print(url)
    unformatted_filename = str(parsed_url[1] + parsed_url[2]).strip('/')
    print(unformatted_filename)
    filename = re.sub(PAGE_PATTERN, '-', unformatted_filename)
    print(filename)
    return filename + ext


def create_dir(url, path):
    dirname = generate_name(url, ext='_files')
    path_to_dir = os.path.join(path, dirname)
    os.makedirs(path_to_dir, exist_ok=True)
    return path_to_dir


def generate_url(url, filename):
    if os.name == 'nt':
        return str(url) + '/' + str(filename)
    return os.path.join(url, filename)


def generate_path(dir_name, filename):
    name, ext = os.path.splitext(filename)
    filename = generate_name(name, ext)
    if os.name == 'nt':
        return os.path.relpath(os.path.join(dir_name, filename))
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
