from page_loader.generators import generate_name
from page_loader.page_content import get_url_to_save


URL1 = 'https://ru.hexlet.io/courses'
CONTENT1 = '/assets/professions/nodejs.png'
URL2 = 'https://site.com/blog/about'
CONTENT2 = 'https://site.com/photos/me.jpg'


def test_generate_name():
    expected_url = 'ru-hexlet-io-courses.html'
    expected_content = 'assets-professions-nodejs.png'
    assert generate_name(url=URL1, ext='.html') == expected_url
    assert generate_name(url=CONTENT1, ext='', is_link=True) == expected_content


def test_get_url_to_save():
    expected_content1 = 'site-com-photos-me.jpg'
    expected_content2 = 'site-com-blog-about.html'
    actual_content1 = list(get_url_to_save(URL2, CONTENT2).keys())[0]
    actual_content2 = list(get_url_to_save(URL2, URL2).keys())[0]
    assert actual_content1 == expected_content1
    assert actual_content2 == expected_content2
