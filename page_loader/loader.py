import os
from page_loader.page_content import parse_images
from page_loader.generators import generate_name, create_dir
from page_loader.save_content import get_content, image


def download(url, output_dir=os.getcwd()):
    page_content = get_content(url)
    dir_to_save = create_dir(url, output_dir)
    filename = generate_name(url, ext='.html')
    path_to_save = os.path.join(output_dir, filename)
    html_to_save, images_to_save = parse_images(url,
                                                page_content.text,
                                                dir_to_save)
    image(images_to_save)
    with open(filename, 'w', encoding='UTF8') as file:
        file.write(html_to_save)
    return dir_to_save



