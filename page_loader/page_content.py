import os
from bs4 import BeautifulSoup
from page_loader.generators import generate_url, \
    generate_path, parse_url, generate_name, modify_content_path


tags = {
    "img": "src",
    "link": "href",
    "script": "src",
}


def parse_html(url, page, dir_name):
    content_links = []
    soup = BeautifulSoup(page, 'html.parser')
    for tag, attr in tags.items():
        for link in [node.get(attr) for node in soup.find_all(name=tag)]:
            if link is not None:
                if parse_url(url)[1] == parse_url(link)[1] \
                        or parse_url(link)[2] == '':
                    url_to_save = get_url_to_save(url,
                                                  modify_content_path(link))
                    content_links.append(url_to_save)
                    path = generate_path(dir_name,
                                         link)
                    original_tag = soup.find(name=tag, **{attr: link})
                    original_tag[attr] = path
    return soup.prettify(), content_links


def get_url_to_save(url, link):
    url, ext = os.path.splitext(url)
    ext = '.html' if ext == '' else ext
    if parse_url(url)[1] == parse_url(link)[1]:
        return {
            generate_name(parse_url(link)[3], ext=ext, is_link=True):
                link
        }
    elif parse_url(link)[2] == '':
        return {
            generate_name(parse_url(link)[3], ext=ext, is_link=True):
                generate_url(parse_url(url)[1], parse_url(link)[3])
        }
