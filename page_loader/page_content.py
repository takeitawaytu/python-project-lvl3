from bs4 import BeautifulSoup
import re
from page_loader.generators \
    import get_new_name, generate_url, \
    generate_path, parse_url


TAGS = ('script', 'link', 'img')
PATTERN = r'^([^http|\/\/][\w]*[\.|\/].+)'


def parse_html(url, page, dir_name, tag_name, tag_attr):
    content_to_save = {}
    _, domain_name = parse_url(url)
    soup = BeautifulSoup(page, 'html.parser')
    print(soup)
    for tag in soup.find_all(tag_name):
        data = re.match(PATTERN, tag.get(tag_attr))
        if data:
            url_to_save = generate_url(url, data.group(0))
            path = generate_path(url, dir_name)
            tag[tag_attr] = path
            content_to_save[url_to_save] = path
    print(domain_name)

    print(content_to_save)
    return content_to_save


def parse_images(url, page, dir_name):
    return parse_html(url, page, dir_name, tag_name='img', tag_attr='src')

