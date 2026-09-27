"""门幅非法值拒绝用例: 0 与负数是两条独立用例, 报错文案必须可区分。"""

import pytest

from app.engines.curtain_math import fabric_meters

BASE_INPUTS = dict(window_w=3.0, window_h=2.6, fullness=2.0, hem_top=0.10, hem_bottom=0.15)


def test_zero_fabric_width_rejected():
    with pytest.raises(ValueError) as exc_info:
        fabric_meters(**BASE_INPUTS, fabric_width=0)
    assert "zero" in str(exc_info.value)


def test_negative_fabric_width_rejected():
    with pytest.raises(ValueError) as exc_info:
        fabric_meters(**BASE_INPUTS, fabric_width=-1.4)
    assert "negative" in str(exc_info.value)


def test_reject_messages_are_distinguishable():
    messages = []
    for bad_width in (0, -1.4):
        with pytest.raises(ValueError) as exc_info:
            fabric_meters(**BASE_INPUTS, fabric_width=bad_width)
        messages.append(str(exc_info.value))
    assert messages[0] != messages[1]
