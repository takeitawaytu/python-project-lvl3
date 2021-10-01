from bs4 import BeautifulSoup
import re
from page_loader.generators import generate_url, \
    generate_path, parse_url


TAGS = IMAGE = 'img'
TAG_ATTRS = (SRC, HREF) = ('src', 'href')
PATTERN = r'^(([\/]|[^http|\/\/])[\w]*[\.|\/].+)'


def parse_html(url, page, dir_name):
    images_to_save = {}
    _, domain_name = parse_url(url)
    soup = BeautifulSoup(page, 'html.parser')
    for tag in soup.find_all(TAGS):
        if tag.name == IMAGE and tag.get(SRC):
            downloaded_images = re.match(PATTERN,
                                         parse_content_path(tag.get(SRC)))
            if downloaded_images:
                url_to_save = generate_url(domain_name,
                                           downloaded_images.group(0))
                path = generate_path(dir_name,
                                     downloaded_images.group(0))
                tag[SRC] = path
                images_to_save[url_to_save] = path
    return soup.prettify(), images_to_save


def parse_content_path(path):
    if str(path).startswith('/'):
        return path[1:]
    return path
