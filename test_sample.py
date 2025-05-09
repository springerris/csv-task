import pytest

import main
from main import get_spaces, get_payout


def test_spaces():
    assert get_spaces(-1) == ""

def test_payout_file():
    with pytest.raises(SystemExit):
        get_payout("data.txt")

def test_payout_header():
    with pytest.raises(SystemExit):
        get_payout("data_noheader.csv")