from page_loader.page_content import parse_html


URL = 'https://ru.hexlet.io/courses'
HTML = './tests/fixtures/test_page.html'
MODIFIED_HTML = 'tests/fixtures/modified_test_page.html'
OUTPUT_DIR = r'C:\\JOB\\PycharmProjects\\hexlet_project_3\\python-project-lvl3\\ru-hexlet-io-courses_files'


def read_file(path):
    with open(path, 'r', encoding='UTF8') as _html:
        return _html.read()


def test_parse_html():
    test_html = read_file(HTML)
    expected_html, _ = parse_html(URL, test_html, OUTPUT_DIR)
    expected_page_content = read_file(MODIFIED_HTML)
    assert expected_page_content == expected_html
