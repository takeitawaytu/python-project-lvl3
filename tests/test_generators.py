from page_loader.generators import generate_name


URL = 'https://ru.hexlet.io/courses'
CONTENT = '/assets/professions/nodejs.png'
T = '/img/bulb.png'


def test_generate_name():
    expected_url = 'ru-hexlet-io-courses.html'
    expected_content = 'assets-professions-nodejs.png'
    assert generate_name(url=URL, ext='.html') == expected_url
    assert generate_name(url=CONTENT, ext='', is_link=True) == expected_content
