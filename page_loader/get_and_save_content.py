import requests
import logging
import os


class PageLoadError(Exception):
    pass


class WebError(PageLoadError):
    pass


class SysError(PageLoadError):
    pass


def get_content(url):
    try:
        content = requests.get(url)
        content.raise_for_status()
    except (
        requests.exceptions.ConnectionError,
        requests.exceptions.HTTPError,
        requests.exceptions.RequestException
    ) as e:
        logging.debug(e, exc_info=True)
        logging.error(f'An error occurred: {e}')
        raise WebError() from e
    else:
        return content


def write(data, filepath, is_assets=False):
    dir_path = os.path.dirname(filepath)
    if not os.path.exists(dir_path) and is_assets:
        try:
            os.mkdir(dir_path)
            logging.debug(f'directory {dir_path} was created')
        except PermissionError:
            logging.error(
                f'not enough rights to create the directory {dir_path}'
            )

    mode, encoding = ('w', 'utf8') if isinstance(data, str) else ('wb', None)
    with open(filepath, mode=mode, encoding=encoding) as f:
        try:
            f.write(data)
        except OSError as e:
            logging.debug(e, exc_info=True)
            logging.error(f'Can`t save {filepath}. An error occurred: {e}')
        finally:
            logging.info(f'\u2713 {filepath}')
