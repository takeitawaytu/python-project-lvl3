import os
import pytest
from pathlib import Path
import shutil
from page_loader.loader import download


def create_temp_dir():
    temp_path = str(os.getenv('SystemDrive')) + \
                r'\\Users\\' + \
                str(os.getenv("USERNAME")) + \
                r'\\AppData\\Local\\Temp\\tmpnb8t_y9s\\'
    Path(temp_path).mkdir(exist_ok=True)
    return temp_path


def remove_temp_dir(temp_dir):
    return shutil.rmtree(temp_dir)


@pytest.fixture()
def prepare_data():
    temp_dir = create_temp_dir()
    actual_filepath = download('https://www.tutorialspoint.com/html/html_images.htm',
                               temp_dir,
                               )
    exp_filepath = os.path.join(temp_dir,
                                'www-tutorialspoint-com-html-html-images-htm.html',
                                )
    exp_img_path = os.path.join(temp_dir,
                                'www-tutorialspoint-com-html-html-images-htm_files',
                                'html-images-test.png'
                                )
    yield (
        actual_filepath,
        exp_filepath,
        exp_img_path,
    )
    remove_temp_dir(temp_dir)


def test_structure(prepare_data):
    (
        actual_filepath,
        exp_filepath,
        exp_img_path,
    ) = prepare_data
    assert os.path.isfile(actual_filepath)
    assert exp_filepath == actual_filepath
    assert os.path.isfile(exp_filepath)
