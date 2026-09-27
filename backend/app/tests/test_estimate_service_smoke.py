"""服务层冒烟: 脏窗走 save=False 预览路径必须失败, 且历史行数不变。"""

import pytest
from fastapi import HTTPException

from app import seed
from app.db import connect
from app.repositories import fabrics, windows
from app.services import estimate_service


def _history_count():
    c = connect()
    try:
        return c.execute("SELECT COUNT(*) AS c FROM calc_runs").fetchone()["c"]
    finally:
        c.close()


def test_dirty_window_preview_fails_and_history_unchanged(monkeypatch, tmp_path):
    # 隔离数据库: 本用例在临时文件上重建种子数据, 不碰真实 app.db
    monkeypatch.setattr("app.db.DB_PATH", tmp_path / "smoke.db")
    seed.init_db()

    dirty_window = next(w for w in windows.list_windows() if w["data_quality"] == "dirty")
    clean_fabric = next(f for f in fabrics.list_fabrics() if f["data_quality"] == "clean")

    before = _history_count()
    with pytest.raises(HTTPException) as exc_info:
        estimate_service.run_estimate(dirty_window["id"], clean_fabric["id"], save=False, note="smoke")
    assert exc_info.value.status_code == 422
    assert _history_count() == before
