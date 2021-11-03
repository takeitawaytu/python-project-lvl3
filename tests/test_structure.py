import os
import pytest
import tempfile
from page_loader.loader import download


@pytest.fixture()
def prepare_data():
    with tempfile.TemporaryDirectory() as temp_dir:
        actual_filepath = download('https://www.tutorialspoint.com/html/html_images.htm',
                                   temp_dir,
                                   )
        exp_html_filepath = os.path.join(temp_dir,
                                         'www-tutorialspoint-com-html-html-images.html',
                                         )
        exp_img_path = os.path.join(
                                    'www-tutorialspoint-com-html-html-images_files',
                                    'html-images-logo.png'
                                    )
        exp_links_path = os.path.join(
                                      'www-tutorialspoint-com-html-html-images_files',
                                      'themes-js-script-min-v1.js'
                                      )
        exp_scripts_path = os.path.join(
                                        'www-tutorialspoint-com-html-html-images_files',
                                        'themes-css-style-min-v1.css'
                                        )
        yield (
            actual_filepath,
            exp_html_filepath,
            exp_img_path,
            exp_links_path,
            exp_scripts_path
        )


def test_structure(prepare_data):
    (
        actual_filepath,
        exp_html_filepath,
        exp_img_path,
        exp_links_path,
        exp_scripts_path,
    ) = prepare_data
    assert os.path.isfile(actual_filepath)
    assert exp_html_filepath == actual_filepath
    assert os.path.isfile(exp_html_filepath)
    assert os.path.isfile(exp_img_path)
    assert os.path.isfile(exp_links_path)
    assert os.path.isfile(exp_scripts_path)
