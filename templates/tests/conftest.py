# tests/conftest.py

import os
import sys
from pathlib import Path

# プロジェクトルートディレクトリをPythonパスに追加
project_root = str(Path(__file__).parent.parent)
sys.path.insert(0, project_root)

# src ディレクトリをPYTHONPATHに追加
src_path = project_root / 'src'
if src_path not in sys.path:
    sys.path.insert(0, str(src_path))
