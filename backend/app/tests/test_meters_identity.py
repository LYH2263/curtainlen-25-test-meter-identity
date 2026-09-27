import pytest

from app.engines.curtain_math import fabric_meters
from app.tests.assert_helpers import assert_meters_identity
from app.tests.fixtures_data import METER_IDENTITY_CASES


@pytest.mark.parametrize(
    "case",
    METER_IDENTITY_CASES,
    ids=[c["name"] for c in METER_IDENTITY_CASES],
)
def test_meters_identity(case):
    """每组组合：abs(meters - panels*cut_height) <= 0.011。"""
    result = fabric_meters(**case["inputs"])
    assert_meters_identity(result, case)


def test_reject_zero_fabric_width():
    """门幅为 0：拒绝，文案指向 zero。"""
    with pytest.raises(ValueError, match="zero"):
        fabric_meters(3.0, 2.6, 2.0, 0.10, 0.15, 0.0)


def test_reject_negative_fabric_width():
    """门幅为负：拒绝，文案指向 negative，与零门幅文案可区分。"""
    with pytest.raises(ValueError, match="negative"):
        fabric_meters(3.0, 2.6, 2.0, 0.10, 0.15, -1.4)
