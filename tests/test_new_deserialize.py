import pytest
import rlp
from rlp.codec import encode_raw, to_serial


EMPTY = b''
SINGLE = b'a'
SHORT = b'arst'
LONG = b'arst' * 256


@pytest.mark.parametrize(
    'value',
    (
        EMPTY,
        SINGLE,
        SHORT,
        LONG,
        #
        [EMPTY],
        [SINGLE],
        [SHORT],
        [LONG],
        #
        [EMPTY, EMPTY],
        [SHORT, EMPTY],
        [SHORT, LONG, EMPTY],
        [[EMPTY], [EMPTY]],
        [[SINGLE], [SINGLE]],
        [[SHORT], [SHORT]],
        [[LONG], [LONG]],
        [[SHORT, LONG], [SINGLE, LONG]],
        [
            [[SHORT, LONG], [SINGLE, LONG]],
            [[SHORT, LONG], [SINGLE, LONG]],
        ],
    )
)
def test_it(value):
    if isinstance(value, bytes):
        expected = encode_raw(value)
    elif isinstance(value, list):
        expected = [encode_raw(item) for item in value]
    raw_value = encode_raw(value)
    as_serial = to_serial(raw_value)
    assert as_serial == expected
