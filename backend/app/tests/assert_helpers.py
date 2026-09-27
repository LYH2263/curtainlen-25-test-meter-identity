"""算料结果断言辅助。"""

# 恒等式容差（米）：meters 保留 2 位、cut_height 保留 3 位，
#  rounding 误差上界约 0.005 + panels*0.0005，panels<=12 时 0.011 足够。
IDENTITY_TOLERANCE = 0.011


def assert_meters_identity(result, case, tol=IDENTITY_TOLERANCE):
    """校验恒等式 abs(meters - panels*cut_height) <= tol。

    失败时断言信息中打印该组输入与 meters/panels/cut_height 三字段。
    """
    meters = result["meters"]
    panels = result["panels"]
    cut_height = result["cut_height"]
    diff = abs(meters - panels * cut_height)
    msg = (
        f"米数恒等式不成立: |meters - panels*cut_height| = {diff:.6f} > {tol}\n"
        f"  用例: {case['name']} (source={case['source']})\n"
        f"  输入: {case['inputs']}\n"
        f"  三字段: meters={meters}, panels={panels}, cut_height={cut_height}"
    )
    assert diff <= tol, msg
