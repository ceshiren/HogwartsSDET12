import os
import shlex
import signal
import subprocess
from typing import List

import pytest


# @pytest.fixture(scope="class", autouse=True)
# def record():
#     cmd = shlex.split("scrcpy --record tmp.mp4")
#     p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     yield
#     os.kill(p.pid, signal.CTRL_C_EVENT)


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # 倒序执行 items里面的测试用例
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
