import os
from page_loader.page_content import parse_html
from page_loader.generators import generate_name, create_dir
from page_loader.save_content import get_content, save_images,\
    save_html_page


def download(url, output_dir=os.getcwd()):
    page_content = get_content(url)
    dir_to_save = create_dir(url, output_dir)
    filename = generate_name(url, ext='.html')
    path_to_save = os.path.join(output_dir, filename)
    html_to_save, images_to_save = parse_html(url,
                                              page_content.text,
                                              dir_to_save)
    save_images(images_to_save)
    save_html_page(html_to_save, path_to_save)
    return path_to_save
