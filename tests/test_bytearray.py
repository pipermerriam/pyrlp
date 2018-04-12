# -*- coding: utf8 -*-
import pytest
from rlp import (
    encode,
    decode,
    decode_lazy,
)


def test_bytearray():
    e = encode(b'abc')
    expected = decode(e)
    actual = decode(bytearray(e))
    assert actual == expected


@pytest.mark.skip()
def test_bytearray_lazy():
    e = encode(b'abc')
    expected = decode(e)
    actual = decode_lazy(bytearray(e))
    assert expected == actual


def test_encoding_bytearray():
    s = b'abcdef'
    direct = encode(s)
    from_bytearray = encode(bytearray(s))
    assert direct == from_bytearray
    assert decode(direct) == s


def encode_empty():
    s = encode(b'')
    actual = decode(s)
    assert actual == b''


def test_encoding_lists():
    value = [b'arst', b'tsra', b'a', b'']
    s = encode(value)
    actual = decode(s)
    assert actual == value
