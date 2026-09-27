import os
import tempfile

# 测试期间把 SQLite 数据目录指到临时位置, 避免在仓库里生成 data/ 目录。
# 必须在任何 app.* 模块被导入之前设置: app.config 在导入时读取 DATA_DIR。
os.environ.setdefault("DATA_DIR", tempfile.mkdtemp(prefix="curtainlen-test-"))
