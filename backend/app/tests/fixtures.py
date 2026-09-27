"""米数恒等式测例包的手写夹具数据。

每组字段:
    name         用例标识 (也作为 pytest 参数化 id)
    window_w     窗宽 (m)
    window_h     窗高 (m)
    fullness     褶量倍数
    hem_top      上折边 (m)
    hem_bottom   下折边 (m)
    fabric_width 门幅 (m)
    expected     手算对照值 (panels / cut_height / meters)

前两条取自 seed.py 的种子数据 (含必含的 客厅落地窗 × 遮光1.4m),
其余为手写组合, 覆盖窄窗、飘窗、大门幅、高褶量与门幅整数倍边界。
"""

INPUT_KEYS = ("window_w", "window_h", "fullness", "hem_top", "hem_bottom", "fabric_width")

CASES = [
    {
        # 种子: 客厅落地窗 × 遮光1.4m (seed.py 第一条窗 × 第一条布)
        "name": "living_room_seed_blackout_1.4m",
        "window_w": 3.0, "window_h": 2.6, "fullness": 2.0,
        "hem_top": 0.10, "hem_bottom": 0.15, "fabric_width": 1.4,
        "expected": {"panels": 5, "cut_height": 2.85, "meters": 14.25},
    },
    {
        # 种子: 卧室窗 × 纱帘2.8m
        "name": "bedroom_seed_sheer_2.8m",
        "window_w": 2.2, "window_h": 1.5, "fullness": 2.0,
        "hem_top": 0.08, "hem_bottom": 0.12, "fabric_width": 2.8,
        "expected": {"panels": 2, "cut_height": 1.7, "meters": 3.4},
    },
    {
        # 手写: 书房窄窗, 低褶量小门幅
        "name": "study_narrow_low_fullness",
        "window_w": 1.2, "window_h": 1.8, "fullness": 1.8,
        "hem_top": 0.10, "hem_bottom": 0.20, "fabric_width": 1.4,
        "expected": {"panels": 2, "cut_height": 2.1, "meters": 4.2},
    },
    {
        # 手写: 主卧飘窗, 高褶量大门幅
        "name": "master_bay_high_fullness",
        "window_w": 1.8, "window_h": 1.2, "fullness": 2.5,
        "hem_top": 0.08, "hem_bottom": 0.12, "fabric_width": 2.8,
        "expected": {"panels": 2, "cut_height": 1.4, "meters": 2.8},
    },
    {
        # 手写: 阳台落地窗, 大门幅少幅数
        "name": "balcony_wide_fabric",
        "window_w": 2.6, "window_h": 2.4, "fullness": 2.0,
        "hem_top": 0.10, "hem_bottom": 0.15, "fabric_width": 2.8,
        "expected": {"panels": 2, "cut_height": 2.65, "meters": 5.3},
    },
    {
        # 手写: 儿童房小窗, 3 倍褶量
        "name": "kids_room_triple_fullness",
        "window_w": 1.5, "window_h": 1.6, "fullness": 3.0,
        "hem_top": 0.12, "hem_bottom": 0.18, "fabric_width": 1.4,
        "expected": {"panels": 4, "cut_height": 1.9, "meters": 7.6},
    },
    {
        # 手写: 成品宽恰为门幅整数倍, 验证 ceil_units 的 epsilon 不多进一幅
        "name": "exact_width_multiple_edge",
        "window_w": 2.8, "window_h": 2.0, "fullness": 2.0,
        "hem_top": 0.10, "hem_bottom": 0.10, "fabric_width": 2.8,
        "expected": {"panels": 2, "cut_height": 2.2, "meters": 4.4},
    },
]


def inputs_of(case):
    """取出一组用例的算料入参, 可直接 ** 展开传给 fabric_meters。"""
    return {k: case[k] for k in INPUT_KEYS}
