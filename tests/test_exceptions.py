import tempfile
import pytest
from page_loader import download
from page_loader.get_and_save_content import WebError, SysError


def test_connection_problems():
    with tempfile.TemporaryDirectory() as temp_dir:
        pytest.raises(
            WebError,
            download,
            'https://www.some-page-test123.com/',
            temp_dir,
        )


def test_bad_http_response():
    with tempfile.TemporaryDirectory() as temp_dir:
        pytest.raises(
            WebError,
            download,
            'https://www.youtube.com/asdf68asdfy',
            temp_dir,
        )
