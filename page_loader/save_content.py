import requests


def get_content(url):
    content = requests.get(url)
    return content


def save_html_page(page_content, path):
    with open(path, 'w', encoding='UTF8') as _html:
        _html.write(page_content)
    return path


def download_image(image_data, path_to_file):
    with open(path_to_file, 'wb') as _image:
        for chunk in image_data.iter_content(chunk_size=128):
            _image.write(chunk)
        return path_to_file


def save_images(images):
    for url_to_save, full_file_path in images.items():
        src_data = get_content(url_to_save)
        download_image(src_data, full_file_path)
