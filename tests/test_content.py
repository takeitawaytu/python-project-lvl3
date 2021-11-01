from page_loader.page_content import parse_html
from page_loader.generators import generate_name
import os

URL = 'https://ru.hexlet.io/courses'
HTML = './tests/fixtures/test_page.html'
MODIFIED_HTML = 'tests/fixtures/modified_test_page.html'


def read_file(path):
    with open(path, 'r', encoding='UTF8') as _html:
        return _html.read()


def test_parse_html():
    test_html = read_file(HTML)
    dirname = generate_name(URL, ext='_files')
    output_dir = os.path.join(os.getcwd(), dirname)
    expected_html, _ = parse_html(URL, test_html, output_dir)
    expected_page_content = read_file(MODIFIED_HTML)
    assert expected_page_content == expected_html
