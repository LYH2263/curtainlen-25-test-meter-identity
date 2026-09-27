"""米数恒等式测例数据。

每个用例描述一组 窗宽/窗高/褶量/上折边/下折边/门幅 组合，
供 test_meters_identity.py 参数化调用算料入口 fabric_meters。

inputs 的键与 fabric_meters 的形参一一对应，可直接 **case["inputs"] 展开。
source 标记来源：
  - "seed"        取自 app/seed.py 的演示数据（窗 × 面料 配对）
  - "handwritten" 手工构造的常规/边界组合
"""

# 与 app/seed.py 中 "客厅落地窗"(3.0x2.6, 褶量2.0) × "遮光1.4m"(折边0.10/0.15) 一致
SEED_LIVING_ROOM_BLACKOUT = {
    "name": "客厅落地窗×遮光1.4m",
    "source": "seed",
    "inputs": {
        "window_w": 3.0,
        "window_h": 2.6,
        "fullness": 2.0,
        "hem_top": 0.10,
        "hem_bottom": 0.15,
        "fabric_width": 1.4,
    },
}

# 与 app/seed.py 中 "卧室窗"(2.2x1.5, 褶量2.0) × "纱帘2.8m"(折边0.08/0.12) 一致
SEED_BEDROOM_SHEER = {
    "name": "卧室窗×纱帘2.8m",
    "source": "seed",
    "inputs": {
        "window_w": 2.2,
        "window_h": 1.5,
        "fullness": 2.0,
        "hem_top": 0.08,
        "hem_bottom": 0.12,
        "fabric_width": 2.8,
    },
}

HANDWRITTEN_CASES = [
    {
        "name": "书房小窗×1.4m",
        "source": "handwritten",
        "inputs": {
            "window_w": 1.2,
            "window_h": 1.4,
            "fullness": 1.8,
            "hem_top": 0.05,
            "hem_bottom": 0.10,
            "fabric_width": 1.4,
        },
    },
    {
        "name": "主卧飘窗×2.8m",
        "source": "handwritten",
        "inputs": {
            "window_w": 1.8,
            "window_h": 0.9,
            "fullness": 2.5,
            "hem_top": 0.10,
            "hem_bottom": 0.20,
            "fabric_width": 2.8,
        },
    },
    {
        "name": "餐厅窗×1.4m低褶",
        "source": "handwritten",
        "inputs": {
            "window_w": 2.5,
            "window_h": 2.0,
            "fullness": 1.5,
            "hem_top": 0.12,
            "hem_bottom": 0.18,
            "fabric_width": 1.4,
        },
    },
    {
        "name": "阁楼斜窗×1.35m",
        "source": "handwritten",
        "inputs": {
            "window_w": 0.9,
            "window_h": 1.1,
            "fullness": 2.2,
            "hem_top": 0.07,
            "hem_bottom": 0.13,
            "fabric_width": 1.35,
        },
    },
    {
        # 4.2*2.0/1.4 = 6.0 恰好整幅，压 ceil_units 的 1e-9 边界
        "name": "整墙客厅×1.4m整幅边界",
        "source": "handwritten",
        "inputs": {
            "window_w": 4.2,
            "window_h": 2.7,
            "fullness": 2.0,
            "hem_top": 0.10,
            "hem_bottom": 0.15,
            "fabric_width": 1.4,
        },
    },
]

METER_IDENTITY_CASES = [
    SEED_LIVING_ROOM_BLACKOUT,
    SEED_BEDROOM_SHEER,
    *HANDWRITTEN_CASES,
]
