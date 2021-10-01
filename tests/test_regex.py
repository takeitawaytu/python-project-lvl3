import re
from page_loader.page_content import PATTERN

PC_TEMPLATE1 = '/assets/professions/nodejs.png'
PC_TEMPLATE2 = 'assets/professions/nodejs.png'
PC_TEMPLATE3 = 'https://test.pattern.ru/assets/professions/nodejs.png'
PC_TEMPLATE4 = 'testpattern'


def test_pc_pattern():
    assert re.match(PATTERN, PC_TEMPLATE1) is not None
    assert re.match(PATTERN, PC_TEMPLATE2) is not None
    assert re.match(PATTERN, PC_TEMPLATE3) is None
    assert re.match(PATTERN, PC_TEMPLATE4) is None

