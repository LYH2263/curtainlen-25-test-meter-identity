"""服务层冒烟：脏窗 + save=false 预览必须失败且历史行数不变。"""
import pytest
from fastapi import HTTPException

from app.db import connect
from app.repositories import fabrics, windows
from app.seed import init_db
from app.services.estimate_service import run_estimate


@pytest.fixture()
def seeded_db(tmp_path, monkeypatch):
    """把 DB 指到临时文件并写入种子数据，避免碰真实库。"""
    db_file = tmp_path / "smoke.db"
    monkeypatch.setattr("app.db.DB_PATH", db_file)
    init_db()
    return db_file


def _history_count() -> int:
    c = connect()
    try:
        return c.execute("SELECT COUNT(*) AS n FROM calc_runs").fetchone()["n"]
    finally:
        c.close()


def test_dirty_window_preview_fails_and_keeps_history(seeded_db):
    dirty_window = next(w for w in windows.list_windows() if w["data_quality"] == "dirty")
    clean_fabric = next(f for f in fabrics.list_fabrics() if f["data_quality"] == "clean")

    before = _history_count()
    with pytest.raises(HTTPException) as exc_info:
        run_estimate(dirty_window["id"], clean_fabric["id"], save=False, note="冒烟:脏窗预览")

    assert exc_info.value.status_code == 422
    assert _history_count() == before
