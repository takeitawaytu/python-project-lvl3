import os
from page_loader.page_content import parse_html
from page_loader.generators import generate_name, create_dir
from page_loader.get_and_save_content import get_content, write


def download(url, output_dir=os.getcwd()):
    page_content = get_content(url)
    dir_to_save = create_dir(url, output_dir)
    filename = generate_name(url, ext='.html')
    path_to_save = os.path.join(output_dir, filename)
    (
        html_to_save,
        content_links
    ) = parse_html(url, page_content.text, dir_to_save)
    write(html_to_save, path_to_save)
    for link in content_links:
        (
            content_filename,
            content_url
        ) = list(link.keys())[0], list(link.values())[0]
        assets_full_path = os.path.join(dir_to_save, content_filename)
        assets = get_content(content_url).content
        write(assets, assets_full_path)
    return path_to_save
