from page_loader.page_content import parse_html

HTML1 = './tests/fixtures/test_page.html'
HTML2 = 'tests/fixtures/google-com.html'


def test_parse_html():
    with open(HTML1, 'r', encoding='UTF8') as _html:
        test_html = _html.read()
        print(test_html)
    expected_images = {
        'https://test.download.com/assets/professions/nodejs.png':
            r'test-download-com-test-html_files\assets-professions-nodejs.png'
    }
    _, images = parse_html(
        'https://test.download.com/test.html',
        test_html,
        r'C:\JOB\PycharmProjects\hexlet_project_3\python-project-lvl3\test-download-com-test-html_files',
    )
    assert images == expected_images



