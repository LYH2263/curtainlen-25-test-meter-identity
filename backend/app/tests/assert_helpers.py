"""算料结果断言辅助: 米数恒等式 |meters - panels * cut_height| <= 0.011。"""

IDENTITY_TOL = 0.011


def format_case_inputs(case):
    """把一组用例的入参格式化成单行, 供失败报告使用。"""
    return (
        f"window_w={case['window_w']} window_h={case['window_h']} "
        f"fullness={case['fullness']} hem_top={case['hem_top']} "
        f"hem_bottom={case['hem_bottom']} fabric_width={case['fabric_width']}"
    )


def assert_meters_identity(case, result, tol=IDENTITY_TOL):
    """断言算料结果满足米数恒等式。

    失败时打印该组输入与三字段 (panels / cut_height / meters) 再抛出 AssertionError。
    返回实际偏差, 便于调用方做额外检查。
    """
    panels = result["panels"]
    cut_height = result["cut_height"]
    meters = result["meters"]
    diff = abs(meters - panels * cut_height)
    if diff > tol:
        report = (
            f"\n[meters-identity FAILED] case={case['name']}\n"
            f"  inputs: {format_case_inputs(case)}\n"
            f"  panels={panels} cut_height={cut_height} meters={meters}\n"
            f"  |meters - panels*cut_height| = {diff:.6f} > tol {tol}"
        )
        print(report)
        raise AssertionError(report)
    return diff
