from nmr.__main__ import nmr_main
from nmr._main import Main
import io
import random
import pytest


@pytest.fixture
def main(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO(''))
    return capsys.readouterr


def test_number_to_name(main):
    Main(arguments=('14', '2342'))()
    assert main().out == 'it\nthe ear\n'


def test_empty_main(main):
    random.seed(0)
    Main()()
    assert main().out.strip() == EXPECTED.strip()


def DISABLED_test_type_to_name(main):
    Main(arguments=('1/2',))()
    res = main().out.strip()
    print(res)
    assert main().out.strip() == EXPECTED_JSON


EXPECTED_JSON = ""
EXPECTED = """
1663767269021425042401656039815989744893952: and end go entry laser later lawn font cuba pride each than cow focus
79016929042850258990298283431820263424: race plain watch see frank did what enter head hero again korea
1068019154206270291968: his usage earn foul per cove rod
8827495699269: the jump dana twice lip
36621494906468431285977088: drive giant law const boost shift hall gang
176484623393291927552: that calm flux void rome bell lean
1548565044347556799526789169587846905856: to peas early globe sean here lost meant can how ward chile east
1464321044699587: key pass the cache heard
675845937528049326096384: your fate lap pants strip gays major ice
147605307123570253828307550208: the kelly eat sip emma life logic court doll cook
"""