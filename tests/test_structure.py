import os
import pytest
import tempfile

from page_loader.loader import download


@pytest.fixture()
def prepare_data():
    with tempfile.TemporaryDirectory() as temp_dir:
        actual_filepath = download('https://tech-guide.ru/notebook/asus-notebook/',
                                   temp_dir,
                                   )
        exp_filepath = os.path.join(temp_dir,
                                    'tech-guide-ru-notebook-asus-notebook.html',
                                    )
        yield (
            actual_filepath,
            exp_filepath,
        )


def test_structure(prepare_data):
    (
        actual_filepath,
        exp_filepath,
    ) = prepare_data
    assert os.path.isfile(actual_filepath)
    assert exp_filepath == actual_filepath
