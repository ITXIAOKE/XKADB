# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 15:17
# @Author  : xiaoke
# @Email   : 976249817@qq.com
# @File    : app_adb_power.py

import os
from utils.operate_log_util import logger
from utils.operate_system_search import get_system_use_search

find = get_system_use_search()


@logger('获取电量信息')
def collect_power():
    # 设置手机进入非充电的状态
    os.popen("adb shell dumpsys battery set status 1")
    # 执行获取电量的命令
    result = os.popen("adb shell dumpsys battery")
    # 获取电量的level
    for line in result:
        if "level" in line:
            power = line.split(":")[1]
    return power


if __name__ == '__main__':
    print(collect_power())
