import os
import logging
from page_loader.page_content import parse_html
from page_loader.generators import generate_name, create_dir
from page_loader.get_and_save_content import get_content, write
from progress.bar import Bar


def download(url, output_dir=os.getcwd()):
    page_content = get_content(url)
    dir_to_save = create_dir(url, output_dir)
    filename = generate_name(url, ext='.html')
    path_to_save = os.path.join(output_dir, filename)
    try:
        (
            html_to_save,
            content_links
        ) = parse_html(url, page_content.text, dir_to_save)
    except AttributeError as e:
        logging.debug(e, exc_info=True)
        logging.error(f'Wrong URL. An error occurred: {e}')
    else:
        write(html_to_save, path_to_save)
        logging.debug(f'page {url} was written in {path_to_save}')
        bar = Bar(f'Loading: {url}', max=len(content_links))
        for link in content_links:
            (
                content_filename,
                content_url
            ) = list(link.keys())[0], list(link.values())[0]
            assets_full_path = os.path.join(dir_to_save, content_filename)
            assets = get_content(content_url).content
            write(assets, assets_full_path, is_assets=True)
            logging.info(f'content by {link} was written')
            bar.next()
        logging.info(
            f'\n Page was successfully downloaded into {path_to_save}'
        )
        bar.finish()
    return path_to_save
