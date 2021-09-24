import os
import requests
from urllib.parse import urlparse
import re
from page_loader.page_content import parse_images
from page_loader.generators import get_new_name, create_dir
DOMAIN_PATTERN = r'^([^http|\/\/][\w]*[\.|\/].+)'


def download(url, output_dir=os.getcwd()):
    page_content = get_content(url)
    dir_to_save = create_dir(url, output_dir)
    filename = get_new_name(url, ext='.html')
    path_to_save = os.path.join(output_dir, filename)
    with open(filename, 'w', encoding='UTF8') as file:
        file.write(page_content.text)
    images_to_save = parse_images(url, page_content.text, dir_to_save)
    image(images_to_save)
    return dir_to_save


def save_image(image_data, path_to_file):
    with open(path_to_file, 'wb') as image:
        for chunk in image_data.iter_content(chunk_size=128):
            image.write(chunk)
        return path_to_file


def image(images):
    for url_to_save, full_file_path in images.items():
        src_data = get_content(url_to_save)
        save_image(src_data, full_file_path)


def get_content(url):
    content = requests.get(url)
    return content


def get_output_filename(url):
    parse_url = urlparse(url)
    unformatted_filename = str(parse_url[1] + parse_url[2]).strip('/')
    filename = re.sub(r'[\W_]', '-', unformatted_filename)
    return filename
