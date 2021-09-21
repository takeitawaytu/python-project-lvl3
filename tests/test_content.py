import tempfile

from page_loader.loader import download

HTML1 = 'tests/fixtures/test_page.html'
URL1 = 'https://ru.hexlet.io/courses'
HTML2 = 'tests/fixtures/google-com.html'
URL2 = 'https://google.com/'


def get_actual_file_content(url):
    with tempfile.TemporaryDirectory() as temp_dir:
        actual_file_path = download(url, temp_dir)
        with open(actual_file_path, 'r', encoding='UTF8') as actual_file:
            actual_file_content = actual_file.read()
            return actual_file_content


def get_exp_file_content(filepath):
    with open(filepath, 'r', encoding='UTF8') as exp_file:
        exp_file_content = exp_file.read()
        return exp_file_content


def test_html_file_content():
    assert True



