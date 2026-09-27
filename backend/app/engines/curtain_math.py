from app.engines.helpers import ceil_units


def fabric_meters(
    window_w: float,
    window_h: float,
    fullness: float,
    hem_top: float,
    hem_bottom: float,
    fabric_width: float,
) -> dict:
    fw = float(fabric_width)
    if fw == 0:
        raise ValueError("fabric width must not be zero")
    if fw < 0:
        raise ValueError("fabric width must not be negative")
    finished_w = float(window_w) * float(fullness)
    panels = max(1, ceil_units(finished_w / fw))
    cut_h = float(window_h) + float(hem_top) + float(hem_bottom)
    meters = panels * cut_h
    return {
        "finished_width": round(finished_w, 3),
        "panels": panels,
        "cut_height": round(cut_h, 3),
        "meters": round(meters, 2),
        "fabric_width": fw,
    }
