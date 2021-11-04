import os
import pytest
from page_loader.page_content import parse_html
from page_loader.generators import generate_name

URL1 = 'https://ru.hexlet.io/courses'
HTML1 = './tests/fixtures/test_page.html'
MODIFIED_HTML1 = 'tests/fixtures/modified_test_page.html'
URL2 = 'https://site.com/blog/about'
HTML2 = './tests/fixtures/hexlet_test_page.html'
MODIFIED_HTML2 = 'tests/fixtures/modified_hexlet_test_page.html'


def read_file(path):
    with open(path, 'r', encoding='UTF8') as _html:
        return _html.read()


class TestParseHtml:
    @pytest.mark.parametrize('url, html, exp_res',
                             [(URL1, HTML1, MODIFIED_HTML1),
                              (URL2, HTML2, MODIFIED_HTML2)])
    def test_parse_html_w_test_page(self, url, html, exp_res):
        test_html = read_file(html)
        dirname = generate_name(url, ext='_files')
        output_dir = os.path.join(os.getcwd(), dirname)
        actual_html, _ = parse_html(url, test_html, output_dir)
        print(_)
        expected_page_content = read_file(exp_res)
        assert actual_html == expected_page_content
