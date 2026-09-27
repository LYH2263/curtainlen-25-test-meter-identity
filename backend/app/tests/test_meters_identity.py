"""米数恒等式测例包: 对每组夹具调用算料入口, 校验 meters == panels * cut_height。"""

import pytest

from app.engines.curtain_math import fabric_meters
from fixtures import CASES, inputs_of
from assert_helpers import assert_meters_identity


@pytest.mark.parametrize("case", CASES, ids=[c["name"] for c in CASES])
def test_meters_identity(case):
    result = fabric_meters(**inputs_of(case))
    assert_meters_identity(case, result)


@pytest.mark.parametrize("case", CASES, ids=[c["name"] for c in CASES])
def test_expected_golden_values(case):
    """手算对照: 夹具里的 expected 三字段必须与算料入口输出一致。"""
    result = fabric_meters(**inputs_of(case))
    expected = case["expected"]
    assert result["panels"] == expected["panels"]
    assert result["cut_height"] == expected["cut_height"]
    assert result["meters"] == expected["meters"]
