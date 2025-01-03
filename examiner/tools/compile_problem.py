import os
import py_compile
import subprocess
from pathlib import Path
import shutil


def compile_problem():
    # 定义路径
    base_path = Path("problem/src")
    dist_path = Path("problem/dist")

    # 确保 dist 目录存在
    dist_path.mkdir(parents=True, exist_ok=True)

    # 获取 src 目录下的所有 Python 文件
    python_files = list(base_path.glob("*.py"))

    # 编译每个 Python 文件为 .pyc 并生成 .pyi
    for py_file in python_files:
        # 编译为 .pyc 文件
        compiled_path = dist_path / (py_file.stem + ".pyc")
        py_compile.compile(py_file, cfile=compiled_path)
        print(f"Compiled {py_file} to {compiled_path}")

        # 使用 stubgen 生成 .pyi 文件
        if py_file.stem == 'tests':
            continue
        subprocess.run(["stubgen", "-o", str(dist_path), str(py_file)], check=True)
        print(f"Generated .pyi for {py_file} in {dist_path}")

    # 移动生成的 .pyi 文件到 dist 目录（stubgen 会生成一个子目录）
    for pyi_file in dist_path.glob("**/*.pyi"):
        target_path = dist_path / pyi_file.name
        pyi_file.rename(target_path)
        print(f"Moved {pyi_file} to {target_path}")
        
    # 清理 .mypy_cache 文件夹（如果有残留）
    cache_path = Path(".mypy_cache")
    if cache_path.exists():
        shutil.rmtree(cache_path)
        print(f"Removed cache directory: {cache_path}")


SURE = True
if __name__ == '__main__':
    if SURE:
        compile_problem()