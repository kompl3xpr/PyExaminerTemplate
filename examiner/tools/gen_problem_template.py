import os

template = '''import os
import sys
grandparent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(grandparent_dir)

from examiner.testlib import TestFramework, TestSuite, Args # type: ignore
from definitions import *
import solution

tests = TestFramework()

# 在此处编写测试用例

tests.run_all()
'''

# 定义目标文件路径
file_path = "problem/src/tests.py"

# 检查文件是否存在
if not os.path.exists(file_path):
    # 确保目录存在
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # 创建文件并写入内容
    with open(file_path, "w") as file:
        file.write(template)
    print(f"File '{file_path}' has been created.")
else:
    print(f"File '{file_path}' already exists.")


file_path = "problem/src/definitions.py"
# 检查文件是否存在
if not os.path.exists(file_path):
    # 创建文件并写入内容
    with open(file_path, "w") as file:
        file.write('# 请在此处定义问题所需的类和函数\n')
    print(f"File '{file_path}' has been created.")
else:
    print(f"File '{file_path}' already exists.")
